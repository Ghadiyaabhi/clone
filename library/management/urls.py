from management.views import libraryBookView,libraryBorrowerView,returningBookView,ReservationView,BookRequestView,SearchBookView
from django.urls import path


urlpatterns = [
    path("reading/",libraryBookView.as_view()),
    path('borrow/', libraryBorrowerView.as_view()),
    path('return/', returningBookView.as_view()),
    path('reservation',ReservationView.as_view()),
    path('request',BookRequestView.as_view()),
    path('search',SearchBookView.as_view()),
]
