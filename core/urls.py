from django.conf.urls.static import static
from django.contrib.auth import views as ve
from django.conf import settings
from core import form
from django.urls import path
from core.form import Login
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("login", ve.LoginView.as_view(template_name="login.html", authentication_form=Login), name="login"),
    path("signup",views.signup),
    path("faq",views.faq),
    path("logout",views.logout_view),
    path("profile",views.profile),
    path("book",views.book),
    path("404",views.errorr),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
