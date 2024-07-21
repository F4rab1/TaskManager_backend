from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerilizer


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer


# @api_view(['GET'])
# def task_list_by_due_date(request, due_date):
#     due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
#     query_set = Task.objects.filter(due_to__date=due_date_obj.date())
#     serializer = TaskSerializer(query_set, many=True)
#     return Response(serializer.data)
