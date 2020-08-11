from django.conf.urls import url
from . import views


urlpatterns = [
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
