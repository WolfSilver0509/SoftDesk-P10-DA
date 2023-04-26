from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentification.views import UserCreateAPIView

from projetAPP.views import ContributorsAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("signup/", UserCreateAPIView.as_view(), name="signup"),
    path("api/contributors/", ContributorsAPIView.as_view(), name="contributors"),
]
