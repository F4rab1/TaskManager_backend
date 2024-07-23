from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerilizer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.select_related('category').all()
        category_id = self.request.query_params.get('category_id')
        completion_date = self.request.query_params.get('completion_date')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        elif completion_date is not None:
            queryset = queryset.filter(completion_date=completion_date)
        return queryset


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer


# @api_view(['GET'])
# def task_list_by_due_date(request, due_date):
#     due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
#     query_set = Task.objects.filter(due_to__date=due_date_obj.date())
#     serializer = TaskSerializer(query_set, many=True)
#     return Response(serializer.data)
