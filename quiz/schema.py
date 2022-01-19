import graphene
from graphene import Schema
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer
from django.db.models import QuerySet


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category", "quiz")


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")


class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")


class Query(graphene.ObjectType):
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())
    all_questions = graphene.List(QuestionType, id=graphene.Int())

    def resolve_all_quizzes(self, info, id: int) -> QuerySet:
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(self, info, id: int) -> QuerySet:
        return Question.objects.get(pk=id)

    def resolve_all_answers(self, info, id: int) -> QuerySet:
        return Answer.objects.filter(question=id)


class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id: int):
        category = Category.objects.get(id=id)
        # category.name = name
        category.delete()
        return


class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()


schema: Schema = graphene.Schema(query=Query, mutation=Mutation)
