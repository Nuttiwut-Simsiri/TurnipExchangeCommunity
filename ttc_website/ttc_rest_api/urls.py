
from django.conf.urls import url
from ttc_rest_api import views

"""
/ttc-api/posts: GET, PUT
/ttc-api/post/:id: GET, DELETE, UPDATE
"""
urlpatterns = [
    url(r'^posts/?$', views.post_all),
    url(r'^users/?$', views.user_all),
    url(r'^posts/(?P<post_id>[0-9]+)/?$', views.post_info),
    url(r'^users/(?P<username>.+)/?$', views.user_info),

]
