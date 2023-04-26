from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from projetAPP.models import Contributors, Projects, Issues, Comments
from projetAPP.serializers import (
    ContributorsSerializer,
    ProjectsSerializer,
    IssuesSerializer,
    CommentsSerializer,
)


class ContributorsAPIView(APIView):
    """
    API endpoint qui permet de lister tous les contributeurs, ou de créer un nouveau contributeur.

    Récupère tous les contributeurs en utilisant l'ORM de Django.
    Sérialise les données en utilisant le serializer de Django REST Framework.
    Renvoie les données sérialisées en JSON.
    """

    def get(self, *args, **kwargs):
        """
        Récupère tous les contributeurs en utilisant l'ORM de Django.
        """
        contributors = Contributors.objects.all()
        serializer = ContributorsSerializer(contributors, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        """
        Crée un nouveau contributeur en utilisant le serializer de Django REST Framework.

        """
        serializer = ContributorsSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
