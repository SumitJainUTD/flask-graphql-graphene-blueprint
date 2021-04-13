import graphene

from company.graphql.query import Query

schema = graphene.Schema(query=Query)