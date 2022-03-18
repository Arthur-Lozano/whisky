from rest_framework import generics
from .serializer import VodkaSerializer
from .models import Vodka


class VodkaList(generics.ListCreateAPIView):
    queryset = Vodka.objects.all()
    serializer_class = VodkaSerializer


class ThingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vodka.objects.all()
    serializer_class = VodkaSerializer
