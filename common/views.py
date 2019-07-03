from rest_framework.generics import ListCreateAPIView

from common.models import ToDoList
from common.serializers import ToDoSerializer


class ToDoListView(ListCreateAPIView):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
