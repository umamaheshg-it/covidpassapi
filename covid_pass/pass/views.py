from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Pass
from .serializers import PassSerializer


@api_view(['GET','PUT'])
def get_update_pass(request, pk):
    try:
        pa = Pass.objects.get(pk=pk)
    except Pass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single pass details
    if request.method == 'GET':
        serializer = PassSerializer(pa)
        return Response(serializer.data)
    # update details of a single pass details
    elif request.method == 'PUT':
        serializer = PassSerializer(pa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_pending_pass(request):
    # get pending passes data
    if request.method == 'GET':
        passes = Pass.objects.filter(status='pending')
        serializer = PassSerializer(passes,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_issued_pass(request):
    # get all issued passes data
    if request.method == 'GET':
        passes = Pass.objects.filter(status='issued')
        serializer = PassSerializer(passes,many=True)
        return Response(serializer.data)


@api_view(['POST'])
def insert_pass_data(request):
    # insert a new record for a pass
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'id_number': request.data.get('id_number'),
            'address': request.data.get('address'),
            'status': request.data.get('status')
        }
        serializer = PassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



