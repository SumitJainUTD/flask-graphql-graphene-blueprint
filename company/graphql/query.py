import graphene
from graphene import relay
from ..graphql.object import Company


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    companies = graphene.List(Company)

    def resolve_companies(self, info):
        query = Company.get_query(info=info)
        print(self)
        return query.all()
