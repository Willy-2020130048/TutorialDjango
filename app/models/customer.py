from django.db.models import Model
from django.db.models.fields import AutoField, CharField


class Customer(Model):
    customer_id = AutoField(primary_key=True, null=False, blank=False)
    customer_no = CharField(null=False, blank=False, max_length=20)
    customer_name = CharField(null=False, blank=False, max_length=100)
    customer_address = CharField(null=False, blank=False, max_length=100)

    class Meta:
        # managed = False
        db_table = "customer"
        ordering = ['customer_name']

    def __str__(self):
        return self.customer_name