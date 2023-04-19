from django.urls import path, include, re_path
from Users import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register),
    path('email_check/', views.email_check),
    path('userinfo/<str:pk>/', views.UserList.as_view()),
    path('userdetail/<str:pk>/', views.UserDetailView.as_view()),
    path('docs', include_docs_urls(title='DRF API文档', description='Django REST framework快速入门')),
    path('text/', views.test)

]
