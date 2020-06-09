from django.conf.urls import url
from ttc_blog import views

urlpatterns = [
    url(r'^webboard/welcome/?$', views.render_index),
    url(r'^webboard/login/?$', views.render_login),
    url(r'^webboard/logout/?$', views.render_webboard),
    url(r'^webboard/sign-up/?$', views.render_sign_up),
    url(r'^webboard/?$', views.render_webboard),
    
]
