

from datetime import date
from django.db.models.query import QuerySet

from tasks.models import Task




class TaskRepository:
    # El patrón Repository se utiliza para separar la lógica de acceso a los datos de la lógica de negocio.
    # En este caso, el repositorio se encarga de manejar todas las operaciones de acceso a datos relacionadas con las tareas.

    def get_all_tasks(self) -> QuerySet[Task]:
        # Este método devuelve todas las tareas almacenadas en la base de datos.
        return Task.objects.all()

    def get_task_by_id(self, task_id: int) -> Task:
        # Este método devuelve una tarea específica basada en su ID.
        return Task.objects.get(id=task_id)

    def create_task(self, title: str, description: str, due_date: date, completed: bool) -> Task:
        # Este método crea una nueva tarea en la base de datos con los datos proporcionados.
        return Task.objects.create(title=title, description=description, due_date=due_date, completed=completed)

    def update_task(self, task_id: int, title: str, description: str, due_date: date, completed: bool) -> Task:
        # Este método actualiza una tarea existente en la base de datos con los datos proporcionados.
        task = self.get_task_by_id(task_id)
        task.title = title
        task.description = description
        task.due_date = due_date
        task.completed = completed
        task.save()
        return task

    def delete_task(self, task_id: int) -> None:
        # Este método elimina una tarea de la base de datos basada en su ID.
        task = self.get_task_by_id(task_id)
        task.delete()
