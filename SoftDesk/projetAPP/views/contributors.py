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
    CommentsDetailSerializer, CommentsListSerializer
)

from projetAPP.permissions import ProjectAuthor

class ContributorsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les contributeurs, ou de créer un nouveau contributeur.

    Récupère tous les contributeurs en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = ContributorsListSerializer

    detail_serializer_class = ContributorsDetailSerializer

    permission_classes = [IsAuthenticated, ProjectAuthor]

    def perform_create(self, serializer):

        project_id = self.kwargs['project_pk']
        project = Projects.objects.get(project_id=project_id)

        serializer.save(project_id=project)

    def get_queryset(self):
        """
        Récupère tous les contributeurs en utilisant l'ORM de Django.
        """
        # # Récupération de tous les contributors dans une variable nommée queryset
        # queryset = Contributors.objects.filter(active=True)

        # # Récupération de tous les issues dans une variable nommée queryset
        queryset = Contributors.objects.filter(project_id=self.kwargs['project_pk'])

        return queryset

    def get_serializer_class(self):
        """
        Récupère tous les contributeurs en utilisant l'ORM de Django.
        """
        if self.action == 'retrieve' and self.detail_serializer_class:
            return self.detail_serializer_class
        return super().get_serializer_class()

