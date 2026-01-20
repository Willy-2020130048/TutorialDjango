from django.forms import ModelForm
from app.models.sales import Sales

class SalesForm(ModelForm):
    class Meta:
        model = Sales
        exclude = ['id']
