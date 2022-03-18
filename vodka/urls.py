from django.urls import path
from .views import VodkaList, VodkaDetail

urlpatterns = [
    path("", VodkaList.as_view(), name="thing_list"),
    path("<int:pk>/", VodkaDetail.as_view(), name="thing_detail"),
]
