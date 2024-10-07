from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from .models import ItemList
from .serializers import ItemSerializer
@api_view(['GET','POST'])
def item_list(request):
    '''
    list all the product here or create the all new product
    '''
    if request.method == 'GET':
        data = ItemList.objects.all()
        # many = true is one importan
        serializer = ItemSerializer(data,many = True)
        return Response(serializer.data)
    elif request.method == "POST":
       serializer = ItemSerializer(data = request.data)
       
       if ItemList.objects.filter(**request.data).exists():
           raise serializers.ValidationError("this is already exits")
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
@api_view(['GET','PUT',"DELETE"])
def item_update(request,pk):
   '''
   retrive ,update  the item list
   '''
      
      
   try: 
      item = ItemList.objects.get(pk = pk)
   except ItemList.DoesNotExist:
      return Response({"error":"Item coundnot found"},status= status.HTTP_404_NOT_FOUND)
   if request.method == "GET":
       serializer = ItemSerializer(item)
       return Response(serializer.data)
   elif request.method == "PUT":
      serializer = ItemSerializer(item,data = request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   elif request.method == "DELETE":
      

# delete the item list

     item.delete()
     return Response(status=status.HTTP_204_NO_CONTENT)
   
   