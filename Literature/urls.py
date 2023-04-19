from django.urls import path, include
from Literature import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(prefix="NovelChapterViewSet", viewset=views.NovelChapterViewSet)
# router.register(prefix="LiteratureViewSet", viewset=views.LiteratureViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("literatureList/", views.literature_list),
    path("literatureDetail/<str:pk>/", views.literature_detail),
    path("literatureModern/", views.LiteratureModern.as_view()),
    path("literatureModernDetail/<int:pk>/", views.LiteratureModernDetail.as_view()),
    path("literatureAncient/", views.LiteratureAncient.as_view()),
    path("literatureAncientDetail/<int:pk>/", views.LiteratureAncientDetail.as_view()),
    path("literatureNovel/", views.LiteratureNovel.as_view()),
    path("literatureNovelDetail/<int:pk>/", views.LiteratureNovelDetail.as_view()),
]
