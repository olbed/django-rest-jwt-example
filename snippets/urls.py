from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("snippets", views.SnippetViewSet)
router.register("users", views.UserViewSet)

urlpatterns = router.urls
