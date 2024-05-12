from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path("",views.dashboard),
    path("/category",views.category),
    path("/categories",views.categories),
    path("/delete/<int:pk>",views.delete,name="delete"),
    path("/edit/<int:pk>",views.edit,name="edit"),
    path("/problem/<int:pk>",views.problem),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
