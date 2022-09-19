clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".cache" -type d | xargs rm -rf

run-target-service:
	@uvicorn target-service.main:app --reload --port 8000

run-async-service:
	@uvicorn async-service.main:app --reload --port 8001

run-sync-service:
	@gunicorn sync-service.main:app --bind 127.0.0.1:8002 --reload --workers 1

test-async-service:
	@ab -n 5 -c 5 -g results/result_async.csv http://127.0.0.1:8001/api/async/resource
	@echo "=== Result ==="
	@cat results/result_async.csv

test-sync-service:
	@ab -n 5 -c 5 -g results/result_sync.csv http://127.0.0.1:8002/api/sync/resource
	@echo "=== Result ==="
	@cat results/result_sync.csv

test-async-block-service:
	@ab -n 5 -c 5 -g results/result_async_block.csv http://127.0.0.1:8001/api/async/block/resource
	@echo "=== Result ==="
	@cat results/result_async_block.csv
