from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

'''
NOTE: Conside this as a reference and follow this same coding structure or format to work on you tasks
'''

# Create your views here.
class ItemView(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def menu_list(request):
    # Hardcoded menu items (later replace with DB query)
    menu_items = [
        {"name": "Margherita Pizza", "price": 8.99, "description": "Classic cheese and tomato pizza"},
        {"name": "Pepperoni Pizza", "price": 10.99, "description": "Pepperoni, mozzarella, and tomato sauce"},
        {"name": "Veggie Burger", "price": 7.49, "description": "Served with lettuce, tomato, and fries"},
        {"name": "Pasta Alfredo", "price": 9.99, "description": "Creamy Alfredo sauce with fettuccine"},
        ]

        return render(request, "menu_list.html", {"menu_items": menu_items})
    ]