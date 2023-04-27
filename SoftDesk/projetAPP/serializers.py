from rest_framework import serializers

from .models import Contributors, Projects, Issues, Comments


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["user_id", "project_id", "permission", "role"]


class ProjectsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["project_id", "title", "description", "type", "author_user_id"]

class ProjectsDetailSerializer(serializers.ModelSerializer):

    contributors = serializers.SerializerMethodField()

    class Meta:
        model = Projects
        fields = ["project_id", "title", "description", "type", "author_user_id", "contributors"]

    def get_contributors(self, instance):

        serializer = ContributorsSerializer(many=True, read_only=True)
        # la propriété .data permet de récupérer les données sérialisées
        return serializer.data




class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = [
            "title",
            "desc",
            "tag",
            "priority",
            "project_id",
            "status",
            "author_user_id",
            "assignee_user_id",
            "created_time",
        ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "comment_id",
            "description",
            "author_user_id",
            "issue_id",
            "created_time",
        ]
