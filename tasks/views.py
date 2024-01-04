from DI import TaskContainer


# Create your views here.
from rest_framework import viewsets

from mixins_customs import CreateModelMixinCustom,ListModelMixinCustom,UpdateModelMixinCustom
from services.task import TaskService
from .models import Task
from .serializers import TaskSerializer
from dependency_injector.wiring import inject, Provide
from rest_framework.response import Response
from rest_framework import status, mixins
class TaskViewSet(CreateModelMixinCustom,
                   mixins.RetrieveModelMixin,
                    UpdateModelMixinCustom,
                   mixins.DestroyModelMixin,
                   ListModelMixinCustom,
                   viewsets.GenericViewSet):
    serializer_class = TaskSerializer

    @inject
    def __init__(self,task_service:TaskService=Provide[TaskContainer.task_service],*args, **kwargs, ):
        super(TaskViewSet, self).__init__(*args, **kwargs)
        self.queryset = task_service.get_all_tasks()

    @inject
    def perform_create(self, serializer, task_service:TaskService=Provide[TaskContainer.task_service]):
        print("sobreescribie")
        task_service.create_task(**serializer.validated_data)

    @inject
    def perform_update(self, serializer, task_service:TaskService=Provide[TaskContainer.task_service]):
        task_id = self.kwargs['pk']  # Obtener el task_id de los parámetros de la URL o de donde sea que esté disponible
        updated_task = task_service.update_task(task_id, **serializer.validated_data)


        serialized_task = TaskSerializer(updated_task)  # Serializar la tarea actualizada
        print("serialized_task", serialized_task)
        print("response")
        return serialized_task

    @inject
    def perform_destroy(self, instance, task_service:TaskService=Provide[TaskContainer.task_service]):
        task_service.delete_task(instance.id)
