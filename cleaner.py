import time
import sys

from glanceclient.client import Client as _glance
from keystoneauth1 import identity, session
from neutronclient.v2_0 import client
from novaclient.client import Client as _nova


def delete_networks(sess):
    neutron = client.Client(session=sess)
    networks = neutron.list_networks()["networks"]
    for network in networks:
        if network["name"].startswith("test"):
            neutron.delete_network(network["id"])


def create_session():
    username = "demo"
    password = "secret"
    project_name = "demo"
    project_domain_id = "default"
    user_domain_id = "default"
    auth_url = "http://10.0.2.15/identity"
    auth = identity.Password(
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        project_domain_id=project_domain_id,
        user_domain_id=user_domain_id,
    )
    sess = session.Session(auth=auth)
    return sess


def delete_servers(sess):
    nova = _nova("2", session=sess)
    servers = nova.servers.list()
    for server in servers:
        nova.servers.delete(server)


sess = create_session()
delete_servers(sess)
delete_networks(sess)