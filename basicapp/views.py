from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SignUp
from .serializers import SignupSerializer, KeySerializer

import logging

logger = logging.getLogger(__name__)


@api_view(['GET'])
def index(request):
    # Send the Test!! log message to standard out
    logger.error("Test!!")
    return Response("Hello logging world.")


@api_view(['POST'])
def create_new_record(request, *args, **kwargs):
    if request.method == "POST":
        input_data = SignupSerializer(data=request.data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data, status=status.HTTP_201_CREATED)
        return Response(input_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_the_records(request):
    if request.method == "GET":
        records = SignUp.objects.all()
        if records:
            serializer_records = SignupSerializer(records, many=True)
            return Response(serializer_records.data)
        return Response({"response": f"No records are found"}, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_the_record(request, pk):
    try:
        snippet = SignUp.objects.get(pk=pk)
    except SignUp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SignupSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_the_record(request, pk):
    try:
        snippet = SignUp.objects.get(pk=pk)
    except SignUp.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        snippet.delete()
        message = {"response": f"record deleted successfully"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def update_the_key(request):
    try:
        records = SignUp.objects.all()[0]
    except Exception as e:
        return Response({"response": f"record not found {e}"})

    if records:
        if request.method == "GET":
            records = SignUp.objects.all()[0]
            input_data = KeySerializer(data=request.data)
            if input_data.is_valid():
                input_data.save(signup=records)
                return Response({"response": f"success"}, status=status.HTTP_201_CREATED)
            return Response(input_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_by_id(request):
    signup_id = request.GET.get("signup_id", "")

    try:
        records = SignUp.objects.get(id=signup_id)
    except Exception as e:
        return Response({"response": f"record not found {e}"})

    if records:
        if request.method == "GET":
            serializer_records = SignupSerializer(records)
            return Response(serializer_records.data)
        return Response({"response": f"No records are found"}, status=status.HTTP_200_OK)
