from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Task, Category, Note
from .serializers import TaskSerializer, AddTaskSerializer, UpdateStageSerializer, CategorySerilizer, NoteSerializer


class TaskViewSet(ModelViewSet):
    pagination_class = PageNumberPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['stage', 'created_at']
    search_fields = ['title', 'description']

    def get_queryset(self):
        queryset = Task.objects.select_related('category').all()
        category_id = self.request.query_params.get('category_id')
        completion_date = self.request.query_params.get('completion_date')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        elif completion_date is not None:
            queryset = queryset.filter(completion_date=completion_date)
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddTaskSerializer
        elif self.request.method == 'PATCH':
            return UpdateStageSerializer
        return TaskSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer


class NoteViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'text']


# @api_view(['GET'])
# def task_list_by_due_date(request, due_date):
#     due_date_obj = datetime.strptime(due_date, '%Y-%m-%d')
#     query_set = Task.objects.filter(due_to__date=due_date_obj.date())
#     serializer = TaskSerializer(query_set, many=True)
#     return Response(serializer.data)
