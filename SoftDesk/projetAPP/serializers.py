from rest_framework import serializers

from .models import Contributors, Projects, Issues, Comments


class ContributorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ["user_id", "project_id", "permission", "role"]

class ContributorsDetailSerializer(serializers.ModelSerializer):

    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Contributors
        fields = ["user_id", "project_id", "permission", "role"]

    def get_user_id(self, instance):

        serializer = ContributorsListSerializer(many=True, read_only=True)
        # la propriété .data permet de récupérer les données sérialisées
        return serializer.data

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

        serializer = ContributorsListSerializer(many=True, read_only=True)
        # la propriété .data permet de récupérer les données sérialisées
        return serializer.data




class IssuesListSerializer(serializers.ModelSerializer):
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

class IssuesDetailSerializer(serializers.ModelSerializer):

        comments = serializers.SerializerMethodField()

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
                "comments",
            ]

        def get_comments(self, instance):

            serializer = CommentsListSerializer(many=True, read_only=True)
            # la propriété .data permet de récupérer les données sérialisées
            return serializer.data

class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            "comment_id",
            "description",
            "author_user_id",
            "issue_id",
            "created_time",
        ]

class CommentsDetailSerializer(serializers.ModelSerializer):

    author_user_id = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = [
            "comment_id",
            "description",
            "author_user_id",
            "issue_id",
            "created_time",
        ]

    def get_author_user_id(self, instance):

            serializer = CommentsListSerializer(many=True, read_only=True)
            # la propriété .data permet de récupérer les données sérialisées
            return serializer.data