from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt

# Список URL-ов приложения
urlpatterns = [
    # Путь для GraphQL запроса
    path('graphql/',
         csrf_exempt(
             # Представление GraphQL с отключенной поддержкой интерфейса GraphiQL
             GraphQLView.as_view(graphiql=False, schema=schema)
         ))
]
