import graphene
from graphene_django.types import DjangoObjectType
from .models import DataDocument

class DataDocumentType(DjangoObjectType):
    """
    Тип GraphQL для модели DataDocument.

    Этот класс автоматически генерирует типы для всех полей модели
    DataDocument, используя graphene-django.
    """
    class Meta:
        model = DataDocument
        fields = '__all__'

class CreateDataDocument(graphene.Mutation):
    """
    Мутация для создания нового объекта DataDocument.

    Аргументы:
    - title (String): Заголовок документа.
    - description (String): Описание документа.

    Возвращает:
    - data_document (DataDocumentType): Созданный объект.
    """
    class Arguments:
        title = graphene.String(required=True, description="Заголовок документа.")
        description = graphene.String(required=True, description="Описание документа.")

    data_document = graphene.Field(DataDocumentType)

    def mutate(self, info, title, description):
        """
        Создает новый объект DataDocument и сохраняет его в базе данных.

        Аргументы:
        - info: Контекст выполнения.
        - title: Заголовок документа.
        - description: Описание документа.

        Возвращает:
        - Экземпляр CreateDataDocument с созданным объектом.
        """
        new_document = DataDocument(title=title, description=description)
        new_document.save()
        return CreateDataDocument(data_document=new_document)

class Query(graphene.ObjectType):
    """
    Определение запросов GraphQL.

    Включает:
    - all_data_documents: Список всех объектов DataDocument.
    """
    all_data_documents = graphene.List(DataDocumentType, description="Список всех документов.")

    def resolve_all_data_documents(self, info):
        """
        Возвращает все объекты DataDocument из базы данных.

        Аргументы:
        - info: Контекст выполнения.

        Возвращает:
        - QuerySet объектов DataDocument.
        """
        return DataDocument.objects.all()

class Mutation(graphene.ObjectType):
    """
    Определение мутаций GraphQL.

    Включает:
    - create_data_document: Создание нового объекта DataDocument.
    """
    create_data_document = CreateDataDocument.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
