from django.db import models
from graphene_django.types import DjangoObjectType 
from django.contrib.auth.models import User
from .models import Category, Ingredient

class UserType(DjangoObjectType):
    class Meta:
        model = User

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category