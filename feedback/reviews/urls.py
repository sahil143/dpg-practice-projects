from django.urls import path
from .views import AddFavoriteView, ReviewListView, ReviewView, SingleReviewView, ThankYouView

urlpatterns = [
    path("", ReviewView.as_view()),
    path("thank-you", ThankYouView.as_view()),
    path("reviews", ReviewListView.as_view()),
    path("reviews/favorite", AddFavoriteView.as_view()),
    path("reviews/<int:pk>", SingleReviewView.as_view())
]

