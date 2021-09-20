import graphene
import ingredients.schema

class Query(ingredients.schema.Query, graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

class Mutation(ingredients.schema.Mutation, graphene.ObjectType):
    edit_ingredient = ingredients.schema.Mutation.edit_ingredient

schema = graphene.Schema(query=Query, mutation=Mutation)
