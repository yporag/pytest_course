import json
import pytest

from django.urls import reverse
from api.pytest_django_project.companies.models import Company

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db  # all tests in the file are marked


# ------------ Test Get Companies ------------


def test_zero_companies_should_return_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []





def test_one_company_exists_should_succeed(client, amazon) -> None:
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == amazon.name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


# ------------ Test Post Companies ------------


def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(path=companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}


def test_create_existing_company_should_fail(client) -> None:
    test_company_name = "apple"
    payload = {"name": test_company_name}

    Company.objects.create(name=test_company_name)
    response = client.post(path=companies_url, data=payload)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["company with this name already exists."]
    }


def test_create_company_with_only_name_should_succeed(client) -> None:
    test_company_name = "test_company"
    payload = {"name": test_company_name}

    response = client.post(path=companies_url, data=payload)
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == test_company_name
    assert response_content.get("status") == "Hiring"
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_layoffs_should_succeed(client) -> None:
    test_company_name = "test_company"
    status = "Layoffs"
    payload = {"name": test_company_name, "status": status}

    response = client.post(path=companies_url, data=payload)
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == test_company_name
    assert response_content.get("status") == status
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""


def test_create_company_with_wrong_status_should_fail(client) -> None:
    test_company_name = "test_company"
    status = "wrong_status"
    payload = {"name": test_company_name, "status": status}

    response = client.post(path=companies_url, data=payload)
    response_content = json.loads(response.content)
    assert response.status_code == 400
    assert status in str(response_content)
    assert "is not a valid choice" in str(response_content)


@pytest.mark.xfail
def test_ok_if_fails() -> None:
    assert 1 == 2


@pytest.mark.skip
def test_should_be_skipped() -> None:
    pass


# ------------ Test Exception Handling ------------


def test_raise_covid19_exceptions_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        _raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)


def _raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")


# ------------ Test logging ------------

import logging

logger = logging.getLogger("CORONA_LOGS")


def test_logged_warning_level(caplog) -> None:
    _function_that_logs_something()
    assert "I am logging CoronaVirus Exception" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text


def _function_that_logs_something() -> None:
    try:
        raise ValueError("CoronaVirus Exception")
    except ValueError as e:
        logger.warning(f"I am logging {str(e)}")


# ------------ learn about fixtures and tests ------------

@pytest.mark.parametrize(
    "companies",
    [["Twitch", "TikTok", "Test Company INC"], ["Facebook", "Instagram"]],
    ids = ["3T companies","Meta companies"],
    indirect=True
)
def test_multiple_companies_exists_should_succeed(client, companies) -> None:
    company_names = set(map(lambda x: x.name, companies))
    response_companies = client.get(companies_url).json()

    assert len(company_names) == len(response_companies)

    response_company_names = set(
        map(lambda company: company.get("name"), response_companies)
    )
    assert company_names == response_company_names
