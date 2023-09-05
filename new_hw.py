from prefect import flow, task
from prefect.deployments import Deployment
from prefect.filesystems import S3, GitHub
#from prefect.task_runners import SequentialTaskRunner, DaskTaskRunner

#storage = GitHub.load("file-storage") # load a pre-defined block



#deployment = Deployment.build_from_flow(
#	flow=hello_world,
#	name="python_api",
#	version="2",
#	tags=["github"],
#	storage=storage,)

#deployment.apply()
#deployment.run_deployment(
#	name="flow_1/python_api ",

#)

from prefect import task, flow
from prefect import get_run_logger
from typing import Any


@task
def say_hi(user_name: str, question: str, answer: Any) -> None:
    logger = get_run_logger()
    logger.info("Hello from Prefect, %s! 👋", user_name)
    logger.info("The answer to the %s question is %s! 🤖", question, answer)


@flow
def parametrized(
    user: str = "Marvin", question: str = "ultimate", answer: Any = 42
) -> None:
    say_hi(user, question, answer)


if __name__ == "__main__":
    parametrized(user="World")
