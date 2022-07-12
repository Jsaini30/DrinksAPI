from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

putautoschema = swagger_auto_schema(
    methods=['put'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'desc'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'desc': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
)


postautoschema = swagger_auto_schema(
    methods=['post'],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name', 'desc'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'desc': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
)


booksputautoschema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['title', 'author', 'totalpages', 'category'],
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'author': openapi.Schema(type=openapi.TYPE_INTEGER),
            'totalpages': openapi.Schema(type=openapi.TYPE_INTEGER),
            'category': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
)

bookspostautoschema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['title', 'author', 'totalpages', 'category'],
        properties={
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'author': openapi.Schema(type=openapi.TYPE_INTEGER),
            'totalpages': openapi.Schema(type=openapi.TYPE_INTEGER),
            'category': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
)



writersputautoschema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name','gender'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'gender': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
)

writerspostautoschema = swagger_auto_schema(
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['name','gender'],
        properties={
            'name': openapi.Schema(type=openapi.TYPE_STRING),
            'gender': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
)