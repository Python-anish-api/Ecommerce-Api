from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
    print("this is heated")
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("anish")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
