from rest_framework import routers
from api.pytest_django_project.companies.views import CompanyViewSet

companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")
