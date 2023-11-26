from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from api.pytest_django_project.companies.models import Company
from api.pytest_django_project.companies.serializers import CompanySerializer


# Create your views here.
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
