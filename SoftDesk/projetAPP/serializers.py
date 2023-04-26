from rest_framework import serializers

from .models import Contributors, Projects, Issues, Comments


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["user_id", "project_id", "permission", "role"]


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ["project_id", "title", "description", "type", "author_user_id"]


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
