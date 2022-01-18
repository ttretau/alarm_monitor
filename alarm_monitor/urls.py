from django.urls import path, re_path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from alarm.urls import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^api/token/', obtain_auth_token, name='api-token'),
    re_path(r'^api/', include(router.urls)),
    url('^$', TemplateView.as_view(template_name='index.html')),
]
