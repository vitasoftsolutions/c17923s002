from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from globalapp2.ed import encode_jwt
# Create your views here.
class BaseViews(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model_name.objects.filter(is_deleted=False)
    # def list(self, request, *args, **kwargs):
    #     # Custom logic for the list (GET) method
    #     data = self.get_queryset()
    #     serializer = self.get_serializer(data, many=True)
    #     # print(serializer.data)
    #     # token = encode_jwt({"data":serializer.data})
    #     # return Response({"token": token})
    #     return self.get_paginated_response(serializer.data)
    def list(self, request, *args, **kwargs):
        # Get the paginated queryset
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            # Serialize the paginated data
            serializer = self.get_serializer(page, many=True)

            # Return the paginated response
            token = encode_jwt({"data":serializer.data})
            return self.get_paginated_response({"token":token})

        # If there is no pagination, serialize the entire queryset
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data without pagination
        token = encode_jwt({"data":serializer.data})
        return Response({"token":token})
    @action(detail=True, methods=['post'])
    def soft_delete(self, request, pk=None):
        item = self.get_object()
        item.is_deleted = True
        item.save()
        return Response({"message": "Data deleted. But you can recover your data"})
    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        item = self.get_object()
        item.status = not item.status
        item.save()
        return Response({"message": "Status changed"})
    



