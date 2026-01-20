from django.forms import ModelForm
from app.models.item import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
