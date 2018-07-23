from django.conf.urls import url, include
from django.contrib import admin

from planning import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Указываем файл отвечающий за маршрутизацию в нашем приложении
    url(r'^', include(urls)),
]
