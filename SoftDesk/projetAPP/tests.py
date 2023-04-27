from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from projetAPP.models import Projects
from authentification.models import User

class TestCategory(APITestCase):
    # Nous stockons l’url de l'endpoint dans un attribut de classe pour pouvoir l’utiliser plus facilement dans chacun de nos tests
    url = reverse_lazy('projet-list')

    def format_datetime(self, value):
        # Cette méthode est un helper permettant de formater une date en chaine de caractères sous le même format que celui de l’api
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        # Créons deux projets dont une seule est active
        user = User.objects.create(username='author2')
        projet = Projects.objects.create(title='projet2', description='description 2', type='WEB', author_user_id=user)
        # Projects.objects.create(title='projet3', description='description 3', type='WEB', author_user_id=user)

        # On réalise l’appel en GET en utilisant le client de la classe de test
        response = self.client.get(self.url)
        # Nous vérifions que le status code est bien 200
        # et que les valeurs retournées sont bien celles attendues
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'project_id': projet.pk,
                'title': projet.title,
                'description': projet.description,
                'type': projet.type,
                'author': projet.author,

            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        # Nous vérifions qu’aucun projet n'existe avant de tenter d’en créer un
        self.assertFalse(Projects.objects.exists())
        response = self.client.post(self.url, data={'name': 'Nouveaux projet '})
        # Vérifions que le status code est bien en erreur et nous empêche de créer un projet
        self.assertEqual(response.status_code, 405)
        # Enfin, vérifions qu'aucun nouveau projet n’ai été créée malgré le status code 405
        self.assertFalse(Projects.objects.exists())