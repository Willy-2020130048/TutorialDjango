from django.forms import ModelForm

from app.models.customer import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['id']
