from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from projetAPP.models import Contributors, Projects, Issues, Comments
from projetAPP.serializers import (
    ContributorsDetailSerializer, ContributorsListSerializer,
    ProjectsDetailSerializer,ProjectsListSerializer,
    IssuesDetailSerializer, IssuesListSerializer,
    CommentsDetailSerializer, CommentsListSerializer)

from projetAPP.permissions import AuthorOrReadOnly

class ProjectsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les projets, ou de créer un nouveau projet.

    Récupère tous les projets en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = ProjectsListSerializer

    detail_serializer_class = ProjectsDetailSerializer

    permission_classes = [IsAuthenticated , AuthorOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(author_user_id=self.request.user)

    def perform_update(self, serializer):

        serializer.save(author_user_id=self.request.user)


    def get_queryset(self):
        """
        Récupère tous les projets en utilisant l'ORM de Django.
        """
        # # Récupération de tous les projects dans une variable nommée queryset
        # queryset = Projects.objects.filter(active=True)

        return Projects.objects.all()

    def get_serializer_class(self):
        """
        Récupère tous les projets en utilisant l'ORM de Django.
        """
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

