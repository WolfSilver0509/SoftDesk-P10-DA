from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from projetAPP.models import Contributors, Projects, Issues, Comments
from projetAPP.serializers import (
    ContributorsSerializer,
    ProjectsSerializer,
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
        return Contributors.objects.all()


class ProjectsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les projets, ou de créer un nouveau projet.

    Récupère tous les projets en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        """
        Récupère tous les projets en utilisant l'ORM de Django.
        """
        return Projects.objects.all()