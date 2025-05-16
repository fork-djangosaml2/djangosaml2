from django.conf.urls import include
from django.urls import re_path

from django.contrib import admin

urlpatterns = [
    re_path(r'^saml2/', include('djangosaml2.urls')),
    re_path(r'^admin/', admin.site.urls),
]
