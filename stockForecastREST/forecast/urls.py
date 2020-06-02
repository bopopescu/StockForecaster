from django.conf.urls import url, include
from forecast import views

urlpatterns =[
    url(r'^api/forecast/historical/(?P<symbol>[\w-]+)/$',views.historical),
]

