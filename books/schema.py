import graphene
from graphene import List, Schema
from graphene_django import DjangoObjectType
from .models import Books
from django.db.models import QuerySet


class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")


class Query(graphene.ObjectType):

    all_books: List = graphene.List(BooksType)

    def resolve_all_books(self, info) -> QuerySet:
        return Books.objects.filter(title='12 rules for life')


schema: Schema = graphene.Schema(query=Query)
