from django.urls import path

from .views import ListRegionView, ListOKVEDView, TopCompaniesView

app_name = "purchases"

urlpatterns = [
    path("regions", ListRegionView.as_view()),
    path("okved", ListOKVEDView.as_view()),
    path("top-companies", TopCompaniesView.as_view()),
]
