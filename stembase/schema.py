import graphene
import stembase.api.schema as SCM

class Query(SCM.Query, graphene.ObjectType):
    pass

class Mutation(SCM.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query = Query, mutation=Mutation)