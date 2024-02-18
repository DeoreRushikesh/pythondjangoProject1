from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class Register(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = "/login"

# def register(request):
#     return render(request, "registration/register.html")
