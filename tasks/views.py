from DI import TaskContainer


# Create your views here.
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from dependency_injector.wiring import inject, Provide

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @inject
    def __init__(self,task_service=Provide[TaskContainer.task_service],*args, **kwargs, ):
        super(TaskViewSet, self).__init__(*args, **kwargs)
        self.queryset = task_service.get_all_tasks()

    @inject
    def perform_create(self, serializer, task_service=Provide[TaskContainer.task_service]):
        task_service.create_task(**serializer.validated_data)

    @inject
    def perform_update(self, serializer, task_service=Provide[TaskContainer.task_service]):
        task_service.update_task(**serializer.validated_data)

    @inject
    def perform_destroy(self, instance, task_service=Provide[TaskContainer.task_service]):
        task_service.delete_task(instance.id)
