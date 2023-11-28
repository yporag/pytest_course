import pytest
from typing import List

from api.pytest_django_project.companies.models import Company

@pytest.fixture
def amazon() -> Company:
    return Company.objects.create(name="Amazon")

@pytest.fixture
def companies(request, company) -> List[Company]:
    company_list = []
    names = request.param #if hasattr(request, 'param') else ["Test Company INC"]
    for company_name in names:
        company_list.append(company(name=company_name))

    return company_list


@pytest.fixture()
def company(**kwargs):
    def _company_factory(**kwargs) -> Company:
        company_name = kwargs.pop("name", "Test Company INC")
        return Company.objects.create(name=company_name, **kwargs)

    return _company_factory