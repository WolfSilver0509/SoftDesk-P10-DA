from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response

from projetAPP.models import Contributors, Projects, Issues, Comments
from projetAPP.serializers import (
    ContributorsDetailSerializer, ContributorsListSerializer,
    ProjectsDetailSerializer,ProjectsListSerializer,
    IssuesDetailSerializer, IssuesListSerializer,
    CommentsDetailSerializer, CommentsListSerializer
)


class ContributorsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les contributeurs, ou de créer un nouveau contributeur.

    Récupère tous les contributeurs en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = ContributorsListSerializer

    detail_serializer_class = ContributorsDetailSerializer

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


class IssuesAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les issues, ou de créer une nouvelle issue.

    Récupère tous les issues en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = IssuesListSerializer

    detail_serializer_class = IssuesDetailSerializer

    def get_queryset(self):
        """
        Récupère tous les issues en utilisant l'ORM de Django.
        """
        # # Récupération de tous les issues dans une variable nommée queryset
        queryset = Issues.objects.filter(project_id=self.kwargs['project_pk'])
        ##
        ## project viens du lookup url router drf + pk

        return queryset

    def get_serializer_class(self):
        """
        On se sert de l'action retrieve pour déterminer quel serializer utiliser.

        """
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les commentaires, ou de créer un nouveau commentaire.

    Récupère tous les commentaires en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = CommentsListSerializer

    detail_serializer_class = CommentsDetailSerializer

    def get_queryset(self):
        """
        Récupère tous les commentaires en utilisant l'ORM de Django.
        """
        # # Récupération de tous les comments dans une variable nommée queryset
        # queryset = Comments.objects.filter(active=True)

        # # Récupération de tous les commentaires dans une variable nommée queryset
        queryset = Comments.objects.filter(issue_id=self.kwargs['issue_pk'])

        return queryset

    def get_serializer_class(self):
        """
        On se sert de l'action retrieve pour déterminer quel serializer utiliser.

        """
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()