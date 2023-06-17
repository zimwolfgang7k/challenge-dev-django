from django.urls import path
from .views import create_proposal, get_proposal

urlpatterns = [
    path("proposals/", create_proposal, name="create_proposal"),
    path("proposals/get_proposals", get_proposal, name="get_proposal"),
]
