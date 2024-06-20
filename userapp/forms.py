


from django.forms import ModelForm

# Register your models here.
from .models import UserDetails



class UserForm(ModelForm):
    class Meta:
        model=UserDetails