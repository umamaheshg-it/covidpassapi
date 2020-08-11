from django.conf.urls import url
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views
from .views import PendingPassViewSet,OutstandingPassViewSet
from rest_framework import renderers
router = DefaultRouter()
router.register(r'pass/pending', views.PendingPassViewSet)
router.register(r'pass/outstanding', views.OutstandingPassViewSet)

urlpatterns = [
    path('',include(router.urls)),
    url(
        r'^api/v1/(?P<pk>[0-9]+)$',
        views.get_update_pass,
        name='get_update_pass'
    ),
    url(
        r'^api/v1/getoutstanding',
        views.get_pending_pass,
        name='get_pending_pass'
    ),
url(
        r'^api/v1/getissued',
        views.get_issued_pass,
        name='get_issued_pass'
    ),
url(
        r'^api/v1/insertpass',
        views.insert_pass_data,
        name='insert_pass_data'
    )
]
