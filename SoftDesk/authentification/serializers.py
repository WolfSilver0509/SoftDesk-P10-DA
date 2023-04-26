from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Cette class permet de définir les champs à afficher dans
    l'API pour les utilisateurs et de définir les champs obligatoires.

    Convertit les objets User en données JSON et vice versa.

    id(int): identifiant de l'utilisateur
    email(str): email de l'utilisateur
    first_name(str): prénom de l'utilisateur
    last_name(str): nom de l'utilisateur
    is_active(bool): si l'utilisateur est actif ou non
    is_staff(bool): si l'utilisateur est un membre du staff ou non
    is_admin(bool): si l'utilisateur est un administrateur ou non
    password(str): mot de passe de l'utilisateur
    """

    class Meta:
        model = User
        fields = ["user_id", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        """
        Cette méthode permet de créer un utilisateur.

        Args:
            validated_data (dict): Données validées pour la création d'un nouvel utilisateur.
         Returns:
            CustomUser: L'utilisateur créé.

        """
        return User.objects.create_user(**validated_data)
