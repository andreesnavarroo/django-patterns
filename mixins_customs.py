
from rest_framework import status
from rest_framework.response import Response
from rest_framework.settings import api_settings




class CreateModelMixinCustom:
    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
        print("paso por aqui")
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data = {'message': serializer.errors,  'data': None}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)     
                    
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'message': 'Registro guardado con éxito','data': serializer.data}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        print("aqui no")
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
        

class ListModelMixinCustom:
    """
    List a queryset.
    """
    def list(self, request, *args, **kwargs):

        queryset = self.queryset.filter()
        queryset = self.filter_queryset(queryset)
        model_name = self.get_serializer().Meta.model.__name__
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(queryset, many=True)
        data = {'message': 'Listado de {}'.format(model_name),'data': serializer.data}        
        return Response(data)        
    



class UpdateModelMixinCustom:
    """
    Update a model instance.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer = self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)



    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)