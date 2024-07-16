from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def task_list(request):
    query_set = Task.objects.all()
    serializer = TaskSerializer(query_set, many=True)
    return Response(serializer.data)
