from django.urls import path
from . import views
from django.contrib import admin
from news.views import scrape, news_list
urlpatterns = [
  path('scrape/<str:name>', scrape, name="scrape"),
  path('', news_list, name="home"),
  #path('', views.news_list, name='news_list'),
  path('admin/', admin.site.urls),
]
admin.autodiscover()
