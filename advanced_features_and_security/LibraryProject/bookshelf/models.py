from django.db import models
<<<<<<< HEAD
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, date_of_birth =None, profile_photo = None ):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, password=None, date_of_birth =None, profile_photo =None ):
        user = self.create_user(username, email, password, date_of_birth, profile_photo)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user      
        
class CustomUser(AbstractUser):
     
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'date_of_birth', 'profile_photo']
    
    def __str__(self):
        return self.username


# Create your models here.
=======
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

<<<<<<< HEAD
class Meta:
        permissions = (
            ("can_create", "Can create a books"),
            ("can_view", "Can view books"),
            ("can_edit", "can edit books"),
            ("can_delete", "Can delete books"),
        )


=======
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, profile_photo, password=None):        
        pass

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        pass
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()
>>>>>>> 100fafa8c433f18a4f4d04a8da6a7d3056d4d76d
    

