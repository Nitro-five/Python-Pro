from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']

    # Валидация поля due_date, чтобы дата не была в прошлом
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date < timezone.localdate():  # Используем localdate() для корректности
            raise ValidationError('Время не может быть в прошлом.')
        return due_date

    # Пример дополнительной кастомной валидации
    def save(self, commit=True):
        task = super().save(commit=False)
        # Например, можно автоматически установить пользователя (если не передан)
        # task.user = self.user  # если вы передаёте пользователя через представление
        if commit:
            task.save()
        return task
