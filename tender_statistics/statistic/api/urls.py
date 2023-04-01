from django.urls import path

from .views import PredictOKVEDView, PredictCompanyView

app_name = "statistics"

urlpatterns = [
    path("region", PredictOKVEDView.as_view()),
    path("company", PredictCompanyView.as_view()),
]
