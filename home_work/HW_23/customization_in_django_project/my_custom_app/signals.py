
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

@receiver(post_save, sender=MyModel)
def mymodel_post_save(sender, instance, created, **kwargs):
    """
    Этот сигнал будет срабатывать после сохранения объекта MyModel.
    Здесь можно выполнять дополнительные действия, например, логирование.
    """
    if created:
        print(f"Новый объект MyModel был создан с ID: {instance.id} и именем: {instance.name}")
    else:
        print(f"Объект MyModel с ID: {instance.id} был обновлен.")
