from django.db.models import Model
from django.db.models.fields import AutoField, CharField, IntegerField


class Item(Model):
    item_id = AutoField(primary_key=True, null=False, blank=False)
    item_no = CharField(null=False, blank=False, max_length=20)
    item_name = CharField(null=False, blank=False, max_length=100)
    stock = IntegerField(null=False, blank=False, default=0)

    class Meta:
        # managed = False
        db_table = "item"
        ordering = ['item_name']

    def __str__(self):
        return self.item_name