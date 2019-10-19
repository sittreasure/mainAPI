from django.urls import path

from .views import CardStatView, ChartStatView

urlpatterns = [
  path(r'cardStat/', CardStatView.as_view()),
  path(r'chartStat/', ChartStatView.as_view()),
]