from .types import IngredientType
from .models import Ingredient
import graphene

class EditIngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class EditIngredientMutation(graphene.Mutation):
    class Arguments:
        input = EditIngredientInput(required=True)
    ok = graphene.Boolean()
    ingredient = graphene.Field(IngredientType)

    @staticmethod
    def mutate(self, info, input):
        print("input", input)
        ingredient = Ingredient.objects.get(pk = input.id)
        ingredient.name = input.name
        try:
            ingredient.save()
        except:
             return EditIngredientMutation(ok=False, ingredient = None)
        return EditIngredientMutation(ok=True, ingredient = ingredient)