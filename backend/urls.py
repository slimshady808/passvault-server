
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls')),
    path('password/',include('password.urls'))
]

urlpatterns +=staticfiles_urlpatterns()