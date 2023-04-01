from django.urls import path

from .views import (
    PredictOKVEDView,
    PredictCompanyView,
    PredictOKVEDCharView,
    PredictMultipleOKVEDView,
)

app_name = "statistics"

urlpatterns = [
    path("region", PredictOKVEDView.as_view()),
    path("region-multiple", PredictMultipleOKVEDView.as_view()),
    path("region-str", PredictOKVEDCharView.as_view()),
    path("company", PredictCompanyView.as_view()),
]
