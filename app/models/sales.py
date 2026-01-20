from django.db.models import Model, ForeignKey, DO_NOTHING
from django.db.models.fields import AutoField, CharField, IntegerField

from app.models.item import Item


class Sales(Model):
    sales_id = AutoField(primary_key=True, null=False, blank=False)
    sales_no = CharField(null=False, blank=False, max_length=20)
    item = ForeignKey(Item, null=False, blank=False, on_delete=DO_NOTHING, related_name='sales')
    quantity = IntegerField(null=False, blank=False, max_length=100)

    class Meta:
        # managed = False
        db_table = "sales"
        ordering = ['sales_no']

    def __str__(self):
        return self.sales_no