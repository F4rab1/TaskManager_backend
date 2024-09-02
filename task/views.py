from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Task, Category, Note, Customer
from .serializers import TaskSerializer, AddTaskSerializer, UpdateStageSerializer, CategorySerilizer, NoteSerializer, CustomerSerializer


class TaskViewSet(ModelViewSet):
    pagination_class = PageNumberPagination
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['stage', 'created_at']
    search_fields = ['title', 'description']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        category_id = self.request.query_params.get('category_id')
        completion_date = self.request.query_params.get('completion_date')
        (customer, created) = Customer.objects.get_or_create(user=user)

        queryset = Task.objects.select_related('category').filter(customer_id=customer.id)

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        if completion_date is not None:
            queryset = queryset.filter(completion_date=completion_date)

        return queryset
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddTaskSerializer
        elif self.request.method == 'PATCH':
            return UpdateStageSerializer
        return TaskSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        customer, created = Customer.objects.get_or_create(user=user)
        serializer.save(customer=customer)

    def perform_update(self, serializer):
        user = self.request.user
        customer = Customer.objects.get(user=user)
        serializer.save(customer=customer)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizer
    permission_classes = [IsAuthenticated]


class NoteViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'text']
    permission_classes = [IsAuthenticated]


class CustomerViewSet(CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    
    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
