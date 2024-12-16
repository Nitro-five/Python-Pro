from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreateSchema(BaseModel):
    """
    Схема для создания задачи.

    Атрибуты:
        title (str): Название задачи.
        description (str): Описание задачи.
        due_date (Optional[datetime]): Дата и время, когда задача должна быть выполнена (по умолчанию None).
        status (str): Статус задачи (по умолчанию "not_started").
    """
    title: str
    description: str
    due_date: Optional[datetime] = None
    status: str = "not_started"

class TaskSchema(TaskCreateSchema):
    """
    Схема для отображения задачи.

    Атрибуты:
        id (int): ID задачи.
        created_at (datetime): Время создания задачи.
        user (int): ID пользователя, который создал задачу.
    """

    id: int
    created_at: datetime
    user: int

    class Config:
        """
        Конфигурация для схемы, которая позволяет работать с объектами ORM.
        """
        orm_mode = True
