from django.urls import path

from .views import CardStatView

urlpatterns = [
  path(r'cardStat/', CardStatView.as_view()),
]