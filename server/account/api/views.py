from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import DummyUser
from account.api.serializers import DummyUserSerializer


# Create your views here.
@api_view(['GET', ])
def accounts_list(request):
    if request.method == 'GET':
        user = DummyUser.objects.all()
        serializer = DummyUserSerializer(user, many=True)
        data = {'user': serializer.data}
        return Response(data)


@api_view(['GET', ])
def account_detail(request, pk):
    try:
        user = DummyUser.objects.get(id=pk)
    except DummyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DummyUserSerializer(user)
        data = {'user': serializer.data}
        return Response(data)


@api_view(['PUT', ])
def account_update(request, pk):
    try:
        user = DummyUser.objects.get(id=pk)
    except DummyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DummyUserSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = True
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def account_delete(request, pk):
    try:
        user = DummyUser.objects.get(id=pk)
    except DummyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = user.delete()
        data = {}
        if operation:
            data['success'] = True
        else:
            data['success'] = False
        return Response(data=data)


@api_view(['POST', ])
def account_create(request):
    user = DummyUser()
    if request.method == 'POST':
        serializer = DummyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
