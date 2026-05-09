import pytest
import requests
import logging
import sys
import allure
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"
AUTH_URL = f"{BASE_URL}/auth"
CARS_URL = f"{BASE_URL}/cars"

USERNAME = "test_user"
PASSWORD = "test_pass"

# Logging setup
logger = logging.getLogger("cars_tests")
logger.setLevel(logging.INFO)
logger.handlers.clear()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def session_with_token():
    session = requests.Session()

    with allure.step("Authorize and obtain access token"):
        logger.info("Authorization")
        response = session.post(
            AUTH_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
        response.raise_for_status()
        token = response.json()["access_token"]
        session.headers.update({"Authorization": f"Bearer {token}"})
        logger.info("Token added to session headers")

    yield session
    session.close()


@allure.feature("Car Search and Filtering")
@pytest.mark.usefixtures("session_with_token")
class TestCarsSearch:

    @allure.title("Search Test: Sort by {sort_by}, Limit {limit}")
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
        if sort_by: params["sort_by"] = sort_by
        if limit: params["limit"] = limit

        with allure.step(f"Send GET request to {CARS_URL} with params: {params}"):
            response = session_with_token.get(CARS_URL, params=params)
            logger.info(f"Status code: {response.status_code}")

        with allure.step("Verify response status code is 200"):
            assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

        data = response.json()

        # Optional: Attach raw data to the Allure report for easier debugging
        allure.attach(str(data), name="Response Body", attachment_type=allure.attachment_type.JSON)

        if limit is not None:
            with allure.step(f"Verify that the number of records is {limit}"):
                actual_len = len(data)
                logger.info(f"Received records: {actual_len}")
                assert actual_len == limit

        if sort_by is not None:
            with allure.step(f"Verify that data is correctly sorted by: {sort_by}"):
                sorted_data = sorted(
                    data,
                    key=lambda x: x.get(sort_by, 0)
                )
                assert data == sorted_data, f"Data is not sorted by {sort_by}"

        logger.info("Test passed successfully\n")