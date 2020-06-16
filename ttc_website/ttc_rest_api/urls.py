
from django.conf.urls import url
from ttc_rest_api import views

"""
/ttc-api/posts: GET, PUT
/ttc-api/post/:id: GET, DELETE, UPDATE
"""
urlpatterns = [
    url(r'^posts/?$', views.post_all),
    url(r'^users/?$', views.user_all),
    url(r'^posts/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', views.post_info),
    url(r'^users/(?P<username>.+)/?$', views.user_info),

]
