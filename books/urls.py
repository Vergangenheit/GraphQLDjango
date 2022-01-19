from django.urls import path
from graphene_django.views import GraphQLView
from books.schema import schema

urlpatterns = [
    # only a single URl to access GraphQL
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
]