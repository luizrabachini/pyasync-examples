from diagrams import Diagram, Cluster
# Developed with diagrams
# https://diagrams.mingrammer.com/
from diagrams.aws.compute import EKS
from diagrams.aws.integration import SQS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.onprem.database import MongoDB, MySQL
from diagrams.onprem.inmemory import Redis


with Diagram("Simple Service", direction='LR') as diag:
    dns = Route53("DNS")
    load_balancer = ELB("Load Balancer")

    client_k8s = EKS("Client API")
    admin_k8s = EKS("Service Admin")
    service_k8s = EKS("Service API")
    workers_k8s = EKS("Service Workers")

    cache = Redis("Cache")
    admin_db = MySQL("Admin")
    with Cluster("Data Cluster"):
        service_db = [
            MongoDB("Primary"),
            MongoDB("Secondary 1"),
            MongoDB("Secondary 2")
        ]

    events_queue = SQS("Events")

    client_k8s >> dns

    dns >> load_balancer >> service_k8s
    service_k8s >> cache
    service_k8s >> service_db

    cache << workers_k8s
    events_queue << workers_k8s
    service_db << workers_k8s

    admin_k8s >> admin_db
    admin_k8s >> events_queue

diag
