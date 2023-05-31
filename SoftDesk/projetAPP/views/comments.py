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

class CommentsAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les commentaires, ou de créer un nouveau commentaire.

    Récupère tous les commentaires en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = CommentsListSerializer

    detail_serializer_class = CommentsDetailSerializer

    # ------------------------------------------------------------------
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def perform_create(self, serializer):

        issue_id = self.kwargs['issue_pk']
        issues = Issues.objects.get(id=issue_id)
        print("perform print")

        serializer.save(author_user_id=self.request.user, issue_id=issues)

    def perform_update(self, serializer):
        serializer.save(author_user_id=self.request.user)

    # -------------------------------------------------------------------

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