from django.urls import path

from . import views

urlpatterns = [
    path("players", views.PlayerViewSet.as_view(), name="players"),
]
