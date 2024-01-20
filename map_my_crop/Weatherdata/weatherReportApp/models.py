# # user_registration/models.py
# from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group
from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(username, password, **extra_fields)

# class CustomUser(AbstractUser):
#     user_id = models.CharField(max_length=30, unique=True)

#     objects = CustomUserManager()

#     def save(self, *args, **kwargs):
#         if not self.user_id:
#             self.user_id = self.username
#         super().save(*args, **kwargs)

#     # Add related_name to avoid clashes
#     groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)
