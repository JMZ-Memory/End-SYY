from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),  # 获取Token的接口
    path('admin/', admin.site.urls),
    path('Users/', include('Users.urls')),
    path('Literature/', include('Literature.urls')),
]
