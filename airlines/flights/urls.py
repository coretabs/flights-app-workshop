from django.contrib import admin
from django.urls import path
from travel.views import SearchResultView , HomePageView
from travel import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name="home"),
    path('search/', SearchResultView.as_view(), name='search_results'),
  
]
