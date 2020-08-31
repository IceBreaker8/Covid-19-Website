from django.urls import path
from . import views

urlpatterns = [


    path('overview/', views.overview, name="covid19-map-overview"),
    path('', views.map, name="covid19-map"),
    path('statistics/<slug:country_id>/', views.stats, name="covid19-stats"),
    path('subscription/', views.subs, name="covid19-subs")


]
