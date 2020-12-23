from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.models import Account
from account.api.serializers import AccountSerializer


# Create your views here.
@api_view(['GET', ])
def accounts_list(request):
    if request.method == 'GET':
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def account_detail(request, pk):
    try:
        account = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)


@api_view(['PUT', ])
def account_update(request, pk):
    try:
        account = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "true"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
def account_delete(request, pk):
    try:
        account = Account.objects.get(id=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = account.delete()
        data = {}
        if operation:
            data['success'] = 'true'
        else:
            data['success'] = 'false'
        return Response(data=data)


@api_view(['POST', ])
def account_create(request):
    account = Account()
    if request.method == 'POST':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
