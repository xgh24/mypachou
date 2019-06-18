from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from web import views


urlpatterns = [
    url('^table/$',views.table),
    path('admin/', admin.site.urls),

]
