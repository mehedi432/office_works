from django.urls import path
from .views import EligibilityCreateView


urlpatterns = [
    path("", EligibilityCreateView.as_view(), name="eligibility-index")
]