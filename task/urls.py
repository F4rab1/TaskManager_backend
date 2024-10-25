from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')
router.register('categories', views.CategoryViewSet)
router.register('notes', views.NoteViewSet, basename='notes')
router.register('customers', views.CustomerViewSet)

notes_router = routers.NestedDefaultRouter(router, 'notes', lookup='note')
notes_router.register('images', views.NoteImageViewSet, basename='note-images')


urlpatterns = router.urls + notes_router.urls