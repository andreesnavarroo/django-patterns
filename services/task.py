

from datetime import date
from repositories.task import TaskRepository
from django.db.models.query import QuerySet

from tasks.models import Task


class TaskService:
    # El patrón Service encapsula la lógica de negocio relacionada con las tareas.
    # Utiliza un objeto TaskRepository para interactuar con los datos de las tareas.

    def __init__(self, task_repository: TaskRepository) -> None:
        self._task_repository = task_repository

    def get_all_tasks(self) -> QuerySet[Task]:
        # Este método devuelve todas las tareas.
        return self._task_repository.get_all_tasks()

    def get_task_by_id(self, task_id: int) -> Task:
        # Este método devuelve una tarea por su ID.
        return self._task_repository.get_task_by_id(task_id)

    def create_task(self, title: str, description: str, due_date: date, completed: bool) -> Task:
        # Este método crea una nueva tarea.
        return self._task_repository.create_task(title, description, due_date, completed)

    def update_task(self, task_id: int, title: str, description: str, due_date: date, completed: bool) -> Task:
        # Este método actualiza una tarea existente.
        return self._task_repository.update_task(task_id, title, description, due_date, completed)

    def delete_task(self, task_id: int) -> None:
        # Este método elimina una tarea por su ID.
        self._task_repository.delete_task(task_id)
