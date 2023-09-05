from new_hw import hello_world 

from prefect.deployments import Deployment


deployment = Deployment.build_from_flow(flow=hello_world, name="example", version="1",  tags=["demo"])
deployment.apply()
