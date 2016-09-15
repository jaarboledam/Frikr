from django.conf.urls import url

from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView

urlpatterns = [
    # WEB URLS
    url(r'^login/$', LoginView.as_view(), name='users_login'),
    url(r'^logout/$', LogoutView.as_view(), name='users_logout'),

    # API URLS
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='api_user_list'),
    url(r'^api/1.0/users/(?P<pk>\d+)$', UserDetailAPI.as_view(), name='api_user_detail'),

]
