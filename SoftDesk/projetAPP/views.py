from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from projetAPP.models import Contributors, Projects, Issues, Comments
from projetAPP.serializers import (
    ContributorsSerializer,
    ProjectsDetailSerializer,ProjectsListSerializer,
    IssuesSerializer,
    CommentsSerializer,
)


class ContributorsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les contributeurs, ou de créer un nouveau contributeur.

    Récupère tous les contributeurs en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = ContributorsSerializer

    def get_queryset(self):
        """
        Récupère tous les contributeurs en utilisant l'ORM de Django.
        """
        # # Récupération de tous les contributors dans une variable nommée queryset
        # queryset = Contributors.objects.filter(active=True)

        return Contributors.objects.all()


class ProjectsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les projets, ou de créer un nouveau projet.

    Récupère tous les projets en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = ProjectsListSerializer

    detail_serializer_class = ProjectsDetailSerializer


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
