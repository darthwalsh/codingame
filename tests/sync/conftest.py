import os
import pytest

import dotenv

from codingame import Client

dotenv.load_dotenv()


@pytest.fixture(name="client", scope="function")
def create_client() -> Client:
    with Client() as client:
        yield client


@pytest.fixture(name="auth_client")
def create_logged_in_client() -> Client:
    with Client() as client:
        client.login(
            os.environ.get("TEST_LOGIN_EMAIL"),
            os.environ.get("TEST_LOGIN_PASSWORD"),
        )
        yield client