from django.urls import path

from .views import ListRegionView, ListOKVEDView, TopCompaniesView
from tender_statistics.statistic.api.views import GlobalView

app_name = "purchases"

urlpatterns = [
    path("global", GlobalView.as_view()),
    path("regions", ListRegionView.as_view()),
    path("okved", ListOKVEDView.as_view()),
    path("top-companies", TopCompaniesView.as_view()),
]
