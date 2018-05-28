from django.conf.urls import url,include
from weixin.views import index
urlpatterns = [
               url(r'^$', index),
]