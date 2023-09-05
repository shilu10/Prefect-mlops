from prefect import flow, task
from prefect.deployments import Deployment
from prefect.filesystems import S3, GitHub
#from prefect.task_runners import SequentialTaskRunner, DaskTaskRunner

storage = GitHub.load("file-storage") # load a pre-defined block

@task(name="task_1")
def task_1(name="task_1"):
	print(name)

@flow(log_prints=True, name="flow_1")
def hello_world(task_id: int = 1):
    if task_id == 1:
    	task_1()

deployment = Deployment.build_from_flow(
	flow=hello_world,
	name="s3-example",
	version="2",
	tags=["github"],
	storage=storage,)

deployment.apply()
