from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, profile_photo, password=None):
        # Custom user creation logic
        pass

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        # Logic for creating a superuser
        pass