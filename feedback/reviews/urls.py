from django.urls import path
from .views import ReviewView, review, thank_you

urlpatterns = [
    path("", ReviewView.as_view()),
    path("thank-you", thank_you)
]

