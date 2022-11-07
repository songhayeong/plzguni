import djoser
from djoser import urls
from djoser.urls import jwt
from djoser.urls import authtoken
from django.urls import path
from django.conf.urls import include
from api.users import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns


app_name = "users"
urlpatterns = [
    path("testing/", include(djoser.urls)),
    path("testing/", include(djoser.urls.jwt)),
    path("NeuralDrops/", views.NeuralDropViewsets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("NeuralDrops/<int:pk>", views.NeuralDropViewsets.as_view({
        'get': 'retrieve',
        'post':'create',
        'put': 'update',
        'delete': 'destroy'
    })),
    path("Testingkch/",views.TestingViewsets.as_view({
        'get': 'list',
        'post': 'create',
        'delete': 'destroy'
    })),
        path("Testingkch/<int:pk>",views.TestingViewsets.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path("raw-query/",views.MyModelViewSets.as_view({
        'get':'list'
        })),
    path("Testing/<int:id>",views.NeuralDropAPI.as_view()),
    path("Testing/<int:id>/<int:pk>", views.NeuralDropViewsets.as_view({
        'get': 'retrieve',
        'post':'create',
        'put': 'update',
        'delete': 'destroy'
    })),
    #path("File",views.TaskApi.as_view()), #여기서 task를 만듬
    path("Task/<int:id>",views.TaskApi.as_view()), #여기에서 task를 만들어야죵?? int:id는 user의 id
    #path("Task/<int:id>/<int:pk>",views.TaskApi.as_view()), 
    path("File/<int:id>",views.FileApi.as_view()), #여기서 file을 만듬
    path("File/<int:id>/<int:pk>",views.FileApi.as_view()), #여기서 파일을 보거나 수정하거나 삭제할 수 있다
    path("Task/<int:id>/<int:pk>", views.TasksApi.as_view()),
    path("TaskAdmin/<int:pk>",views.TasksViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path("FileAdmin/<int:pk>",views.FileView.as_view({
        'get':'retrieve',
        'put':'update',
        'patch':'update',
        'delete':'destroy'       
    })),
    path("A",views.Reco1view.as_view({
        'get':'list',
        'post':'create'
    })),
    path("A/<int:pk>",views.Reco1view.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
        path("B",views.Reco2view.as_view({
        'get':'list',
        'post':'create'
    })),
    path("B/<int:pk>",views.Reco2view.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
        path("C",views.Reco3view.as_view({
        'get':'list',
        'post':'create'
    })),
    path("C/<int:pk>",views.Reco3view.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
        path("D",views.Reco4view.as_view({
        'get':'list',
        'post':'create'
    })),
    path("D/<int:pk>",views.Reco4view.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
        path("E",views.Reco5view.as_view({
        'get':'list',
        'post':'create'
    })),
    path("E/<int:pk>",views.Reco5view.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
        path("F",views.Reco6view.as_view({
        'get':'list',
        'post':'create'
    })),
    path("F/<int:pk>",views.Reco6view.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
        path("Result",views.Resultview.as_view({
        'get':'list',
        'post':'create'
    })),
    path("Result/<int:pk>",views.Resultview.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),              
        path("Ai",views.Aiview.as_view({
        'get':'list',
        'post':'create'
    })),
    path("Ai/<int:pk>",views.Aiview.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),       
    path("a/<int:id>",views.Re1view.as_view()),
    path("b/<int:id>",views.Re2view.as_view()),
    path("c/<int:id>",views.Re3view.as_view()),
    path("d/<int:id>",views.Re4view.as_view()),
    path("e/<int:id>",views.Re5view.as_view()),
    path("f/<int:id>",views.Re6view.as_view()),     
    path("result/<int:id>",views.Resview.as_view()),  
    path("Contactus",views.ContactusView.as_view()), 
]


#  def post(self, request, id):
#         instance = NeuralDropTasks.objects.filter(company_id=id)
#         serializer_class = NeuralDropTaskSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


#     def put(self, request, id):
#         instance = NeuralDropTasks.objects.filter(company_id=id)
#         serializer_class = NeuralDropTaskSerializer(instance, many=True,data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
