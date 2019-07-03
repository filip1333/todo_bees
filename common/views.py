from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView

from common.models import ToDoList
from common.serializers import ToDoListSerializer, ToDoEditSerializer


class ToDoListCreate(ListCreateAPIView):
    queryset = ToDoList.objects.create()
    serializer_class = ToDoListSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ToDoListRead(ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoEditSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_id(self):
        return self.get_id()


class ToDoListDestroy(DestroyAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoEditSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ToDoListUpdate(UpdateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoEditSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
