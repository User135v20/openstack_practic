import create_session
from neutronclient.v2_0 import client
from novaclient.client import Client as _nova


def delete_networks(sess):
    neutron = client.Client(session=sess)
    networks = neutron.list_networks()["networks"]
    for network in networks:
        if network["name"].startswith("test"):
            neutron.delete_network(network["id"])


def delete_servers(sess):
    nova = _nova("2", session=sess)
    servers = nova.servers.list()
    for server in servers:
        nova.servers.delete(server)


sess = create_session.create()
delete_servers(sess)
delete_networks(sess)
