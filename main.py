import time
from neutronclient.v2_0 import client
from novaclient.client import Client as _nova

import create_session


def create_network(sess):
    neutron = client.Client(session=sess)
    # print(neutron.list_networks())

    body_sample = {"network": {"name": "test"}}
    netw = neutron.create_network(body=body_sample)
    net_dict = netw["network"]
    network_id = net_dict["id"]
    print("Network %s created" % network_id)

    body_create_subnet = {"subnets": [{"cidr": "192.168.199.0/24", "ip_version": 4, "network_id": network_id}]}
    subnet = neutron.create_subnet(body=body_create_subnet)
    print("Created subnet %s" % subnet)
    subnet_id = subnet.get("id")
    return network_id, subnet_id


def create_server(sess, network_id):
    server_name = str(input("Please enter server name: "))
    nova = _nova("2", session=sess)
    flavor_id = "c1"
    image_id = "e207ec98-21d4-47d7-b491-384ca824631f"
    server = nova.servers.create(server_name, image_id, flavor_id, nics=[{"net-id": network_id}])
    return server


print("application for creating a server\n")
sess = create_session.create()
network_id, subnet_id = create_network(sess)
server = create_server(sess, network_id)
print("server's status")
for i in range(5):
    print(server.status)
    time.sleep(5)
