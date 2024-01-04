from django.apps import AppConfig


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    def ready(self):
        # Realiza tareas de inicialización aquí, como configurar la inyección de dependencias
        from DI import TaskContainer
        container = TaskContainer()
        container.wire(modules=[".views"])
