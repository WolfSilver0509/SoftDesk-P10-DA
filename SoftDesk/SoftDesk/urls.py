from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentification.views import UserCreateAPIView

from projetAPP.views import ContributorsAPIView, ProjectsAPIView, IssuesAPIView , CommentsAPIView


# Création d'un router pour les vues basées sur les views
router = routers.SimpleRouter()


# Déclaration des routes pour les vues basées sur les views


router.register("projects", ProjectsAPIView, basename="projects")
project_router = routers.NestedSimpleRouter(router, r'projects', lookup='project')
project_router.register(r'issues', IssuesAPIView, basename='projects_issues')

# router.register("issues", IssuesAPIView, basename="issues")
router.register("comments", CommentsAPIView, basename="comments")
router.register("contributors", ContributorsAPIView, basename="contributors")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("signup/", UserCreateAPIView.as_view(), name="signup"),
    # path("api/contributors", ContributorsAPIView.as_view(), name="contributors"),
    # path("api/projects/", ProjectsAPIView.as_view(), name="projects"),
    path("api/", include(router.urls)),
    path("api/", include(project_router.urls)),
]
