from django.db import models

from authentification.models import User




class Projects(models.Model):
    choice_type = [("Web", "Web"), ("IOS", "IOS"), ("Android", "Android")]

    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=300, choices=choice_type)
    author_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="projects"
    )

class Contributors(models.Model):
    choice = [("Oui", True), ("Non", False)]
    user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="contributors"
    )
    project_id = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, related_name="contributors"
    )
    permission = models.CharField(max_length=5, choices=choice)
    role = models.CharField(max_length=128)


class Issues(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=1000)
    tag = models.CharField(max_length=128)
    priority = models.CharField(max_length=128)
    project_id = models.ForeignKey(
        to=Projects, on_delete=models.CASCADE, related_name="issues"
    )
    status = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="issues"
    )
    assignee_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="assigned_issues"
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=1000)
    author_user_id = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="comments"
    )
    issue_id = models.ForeignKey(
        to=Issues, on_delete=models.CASCADE, related_name="comments"
    )
    created_time = models.DateTimeField(auto_now_add=True)
