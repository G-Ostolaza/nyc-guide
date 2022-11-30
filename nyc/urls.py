from django.urls import path

from nyc.views import CityView, BoroughView, ActivityView, VenueView

urlpatterns = [
    # all the urls are for free
    # Path to all URLS as they relate to their view Classes in the views.py file
    path('', CityView.as_view(), name='city'),
    path('<str:borough>', BoroughView.as_view(), name='borough'),
    path('<str:borough>/<str:activity>', ActivityView.as_view(), name='activity'),
    path('<str:borough>/<str:activity>/<str:venue>', VenueView.as_view(), name='venue')
]
