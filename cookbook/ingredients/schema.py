from .mutation import EditIngredientMutation
from .types import IngredientType
from .models import Ingredient
import graphene

class Query(graphene.ObjectType):
    ingredients = graphene.List(IngredientType)
    ingredient = graphene.Field(IngredientType, id = graphene.Int())

    def resolve_ingredients(self, info, **kwargs):
        return Ingredient.objects.all()
    
    def resolve_ingredient(self, info, **kwargs):
        ingredient_id = kwargs.get('id')
        if ingredient_id:
            return Ingredient.objects.get(pk=ingredient_id)
        return None

class Mutation(graphene.ObjectType):
	edit_ingredient = EditIngredientMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)