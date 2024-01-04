from dependency_injector import containers, providers
from repositories.task import TaskRepository
from services.task import TaskService

class TaskContainer(containers.DeclarativeContainer):
    # Definir un contenedor para gestionar las dependencias de la aplicación de gestión de tareas

    # Proveedor de configuración
    config = providers.Configuration()

    # Proveedor Factory para crear instancias de TaskRepository
    task_repository = providers.Factory(TaskRepository)

    # Proveedor Singleton para proporcionar una única instancia de TaskService
    task_service = providers.Singleton(TaskService, task_repository)
