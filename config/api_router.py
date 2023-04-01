from django.urls import path, include

app_name = "api"
urlpatterns = [
    path("data/", include("tender_statistics.purchases.api.urls")),
    path("statistics/", include("tender_statistics.statistic.api.urls")),
]
