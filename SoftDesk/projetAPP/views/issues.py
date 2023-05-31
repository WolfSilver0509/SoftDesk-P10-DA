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

class IssuesAPIView(ModelViewSet):
    """
    API endpoint qui permet de lister tous les issues, ou de créer une nouvelle issue.

    Récupère tous les issues en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """
    serializer_class = IssuesListSerializer

    detail_serializer_class = IssuesDetailSerializer
#------------------------------------------------------------------
    permission_classes = [IsAuthenticated, AuthorOrReadOnly]

    def perform_create(self, serializer):

        project_id = self.kwargs['project_pk']
        project = Projects.objects.get(project_id=project_id)

        serializer.save(author_user_id=self.request.user, project_id=project)


    # def perform_update(self, serializer):
    #
    #     serializer.save(author_user_id=self.request.user,project_id=project)
#-------------------------------------------------------------------
    def get_queryset(self):
        """
        Récupère toutes les issues en utilisant l'ORM de Django.
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
