from django.conf.urls import url
from app.views import home

urlpatterns = [
     url(r"^$", home, name="home"),
]
