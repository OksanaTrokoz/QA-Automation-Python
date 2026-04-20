import pytest
import requests
import logging
import sys
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"
AUTH_URL = f"{BASE_URL}/auth"
CARS_URL = f"{BASE_URL}/cars"

USERNAME = "test_user"
PASSWORD = "test_pass"


logger = logging.getLogger("cars_tests")
logger.setLevel(logging.INFO)

logger.handlers.clear()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler = logging.FileHandler(
    "test_search.log",
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def session_with_token():
    session = requests.Session()

    logger.info("Authorization")

    response = session.post(
        AUTH_URL,
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )
    response.raise_for_status()

    token = response.json()["access_token"]

    session.headers.update({
        "Authorization": f"Bearer {token}"
    })

    logger.info("Token added")

    yield session
    session.close()



@pytest.mark.usefixtures("session_with_token")
class TestCarsSearch:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("price", 10),
            ("year", 7),
            ("engine_volume", 8),
            ("brand", 6),
            (None, 5),
            ("price", None),
        ]
    )
    def test_search_cars(self, session_with_token, sort_by, limit):

        params = {}

        if sort_by is not None:
            params["sort_by"] = sort_by

        if limit is not None:
            params["limit"] = limit

        logger.info(f"GET /cars params: {params}")

        response = session_with_token.get(CARS_URL, params=params)

        logger.info(f"Status code: {response.status_code}")
        assert response.status_code == 200

        data = response.json()
        logger.info(f"Received records: {len(data)}")


        if limit is not None:
            assert len(data) == limit


        if sort_by is not None:
            sorted_data = sorted(
                data,
                key=lambda x: x.get(sort_by, 0)
            )
            assert data == sorted_data

        logger.info("Test passed\n")