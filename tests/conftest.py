import pytest
import docker
from os.path import dirname, abspath


DEFAULT_PORT = 8000
IMAGE_DIR_PATH = dirname(dirname(abspath(__file__)))


@pytest.fixture
def base_url():
    return f"http://localhost:{DEFAULT_PORT}/"


@pytest.fixture
def docker_client():
    return docker.from_env()


@pytest.yield_fixture(autouse=True)
def unit_service(docker_client):
    containers = docker_client.containers.list()
    runner_container = [*filter(lambda item: "runner" in item.name, containers)]
    network = (
        "host" if not runner_container else f"container:/{runner_container[0].name}"
    )

    image, _ = docker_client.images.build(path=IMAGE_DIR_PATH)
    container = docker_client.containers.create(
        image=image, network=network, auto_remove=True
    )
    container.start()
    yield container
    container.stop()
