from rest_framework import permissions

from projetAPP.models import Issues, Contributors, Projects

class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """ lecture seule """
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """ Je peut intéragir avec l'objet """
        if obj.author_user_id == request.user:
            return True
        elif view.action == "retrieve":
            return True
        return False


class ProjectAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        """ lecture seule """

        project_id = view.kwargs.get('project_pk')

        author = Projects.objects.filter(author_user_id=request.user, project_id=project_id)
        if author:
            return True
        elif view.action in ["retrieve", "list"] :
            return True
        return False






class IsContributor(permissions.BasePermission):
    """
    Permission personnalisée qui permet uniquement aux contributeurs d'accéder aux issues qui leur sont assignées.
    Ils ne peuvent pas accéder aux issues auxquelles ils ne sont pas assignés,
    ni aux projets associés à ces issues.
    """
    def has_permission(self, request, view):
        # Vérifie si l'utilisateur est un contributeur
        if request.user and request.user.is_authenticated:
            # Récupère l'identifiant de l'issue depuis la requête

            project_id = view.kwargs.get('project_pk')

            contributor = Contributors.objects.filter(user_id = request.user , project_id = project_id)

            author =  Projects.objects.filter(author_user_id = request.user, project_id = project_id )

            if contributor or author:
                return True
            return False

        return False
