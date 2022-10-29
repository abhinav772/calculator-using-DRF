from rest_framework.response import Response
from rest_framework.views import APIView

from operation.api.serializers import AddSerializer, SubtractSerializer, MultiplySerializer, DivideSerializer

class AddResult(APIView):

    def post(self, request):
        serializer = AddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SubtractResult(APIView):

    def post(self, request):
        serializer = SubtractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MultiplyResult(APIView):

    def post(self, request):
        serializer = MultiplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class DivideResult(APIView):

    def post(self, request):
        serializer = DivideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



