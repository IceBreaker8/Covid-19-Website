from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="covid19-home"),
    path('overview/', views.overview, name="covid19-overview"),
    path('map/overview/', views.overview, name="covid19-map-overview"),
    path('map/', views.map, name="covid19-map"),
    path('map/statistics/<slug:country_id>/', views.stats, name="covid19-stats"),
    path('subscription/', views.subs, name="covid19-subs"),
    path('about/', views.about, name="covid19-about"),

]
