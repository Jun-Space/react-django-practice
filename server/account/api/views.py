from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import DummyUser
from account.api.serializers import DummyUserSerializer


# Create your views here.
@api_view(['GET', 'POST', ])
def accounts_rc(request):
    if request.method == 'GET':
        users = DummyUser.objects.all()
        serializer = DummyUserSerializer(users, many=True)
        data = {'user': serializer.data}
        return Response(data)

    if request.method == 'POST':
        user = DummyUser()
        serializer = DummyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', ])
def accounts_rud(request, pk):
    try:
        user = DummyUser.objects.get(id=pk)
    except DummyUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DummyUserSerializer(user)
        data = {'user': serializer.data}
        return Response(data)

    if request.method == 'PUT':
        serializer = DummyUserSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = True
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        operation = user.delete()
        data = {}
        if operation:
            data['success'] = True
        else:
            data['success'] = False
        return Response(data=data)
