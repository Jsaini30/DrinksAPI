
from .models import Drink, book ,Writer
from .serializer import DrinkSerializer, bookserializer , writerserializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .swagger_schema import putautoschema, postautoschema, bookspostautoschema,booksputautoschema,writerspostautoschema,writersputautoschema


@postautoschema
@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@putautoschema
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk):
    try:
        print(pk)
        drink = Drink.objects.get(id=pk)
        print(drink)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# BOOKS VIEW
class BooksAPI(APIView):

    def get(self, request):
        books = book.objects.all()
        serializer = bookserializer(books, many=True)
        return Response(serializer.data)

    @bookspostautoschema
    def post(self, request):
        serializer = bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookAPI(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            books = book.objects.get(id=pk)
            serializer = bookserializer(books)
            return Response(serializer.data)

    @booksputautoschema
    def put(self, request, pk=None):
        books = book.objects.get(id=pk)
        serializer = bookserializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        books = book.objects.get(id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#WRITER'S SERIALIZER

class WritersAPI(APIView):

    def get(self, request):
        writers = Writer.objects.all()
        serializer = writerserializer(writers, many=True)
        return Response(serializer.data)


    @writerspostautoschema
    def post(self, request):
        serializer = writerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class WriterAPI(APIView):
    def get(self, request, pk=None):
        id = pk
        if id is not None:
            writers = Writer.objects.get(id=pk)
            serializer = writerserializer(writers)
            return Response(serializer.data)

    @writersputautoschema
    def put(self, request, pk=None):
        writers = Writer.objects.get(id=pk)
        serializer = writerserializer(writers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status-status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        writers = Writer.objects.get(id=pk)
        Writer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)