from keystoneauth1 import identity, session


def create():
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
