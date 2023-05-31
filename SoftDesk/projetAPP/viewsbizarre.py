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






