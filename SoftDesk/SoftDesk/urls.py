from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentification.views import UserCreateAPIView

from projetAPP.views import ContributorsAPIView, ProjectsAPIView


# Création d'un router pour les vues basées sur les views
router = routers.SimpleRouter()
# Déclaration des routes pour les vues basées sur les views
router.register("contributors", ContributorsAPIView, basename="contributors")
router.register("projects", ProjectsAPIView, basename="projects")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("signup/", UserCreateAPIView.as_view(), name="signup"),
    # path("api/contributors", ContributorsAPIView.as_view(), name="contributors"),
    # path("api/projects/", ProjectsAPIView.as_view(), name="projects"),
    path("api/", include(router.urls)),
]
