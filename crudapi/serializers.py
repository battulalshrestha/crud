from django.db.models import fields
from rest_framework import serializers
from .models import ItemList
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ('category','sub_category','item_name','item_location','item_id','item_description','item_amount')


