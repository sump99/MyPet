from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class Main(APIView):
    def get(self, request):
        return render(request, "index.html")