from api.users.models import *
from api.users.serializers import *
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import views
from rest_framework import viewsets
from multipledispatch import dispatch
from django.core.mail import EmailMessage


class NeuralDropAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = NeuralDropTasks.objects.filter(company_id=id)
        serializer_class = NeuralDropTaskSerializer(instance, many=True)
        return Response(serializer_class.data)

    def post(self, request, id):
        instance = NeuralDropTasks.objects.filter(company_id=id)
        serializer_class = NeuralDropTaskSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        instance = NeuralDropTasks.objects.filter(company_id=id)
        serializer_class = NeuralDropTaskSerializer(instance, many=True,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = NeuralDropTasks.objects.filter(company_id=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TasksApi(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        instance = Task.objects.filter(pk=id)
        serializer = TaskSerializer(instance, many=True)
        return Response(serializer.data)


class TaskApi(APIView):
    permission_classes = [AllowAny]
    #neuraldrop task 만들고 볼 수 있게하는 기능을 구현한 view
    def get(self, request, id):
        instance = Task.objects.filter(userId = id)
        serializer = TaskSerializer(instance, many=True)
        return Response(serializer.data)

    # @dispatch
    # def get(self , request, pk):
    #     instance = Task.objects.filter(pk=id)
    #     serializer = TaskSerializer(instance, many=True)
    #     return Response(serializer.data)    

    def post(self, request ,id):
        instance = Task.objects.filter(userId=id)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        instance = Task.objects.filter(userId=id)
        serializer = TaskSerializer(instance, many=True,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, id):
        instance = Task.objects.filter(userId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      

class FileApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = File.objects.filter(taskId=id)
        serializer = FileSerializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = File.objects.filter(taskId=id)
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def delete(self, request, id):
        instance = File.objects.filter(taskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    


class Re1view(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = RecommendedTech1.objects.filter(TaskId=id)
        serializer = RecommendedTech1Serializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = RecommendedTech1.objects.filter(TaskId=id)
        serializer = RecommendedTech1Serializer(instance, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = RecommendedTech1.objects.filter(TaskId=id)
        serializer = RecommendedTech1Serializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = RecommendedTech1.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Re2view(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = RecommendedTech2.objects.filter(TaskId=id)
        serializer = RecommendedTech2Serializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = RecommendedTech2.objects.filter(TaskId=id)
        serializer = RecommendedTech2Serializer(instance, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = RecommendedTech2.objects.filter(TaskId=id)
        serializer = RecommendedTech2Serializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = RecommendedTech2.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)     


class Re3view(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = RecommendedTech3.objects.filter(TaskId=id)
        serializer = RecommendedTech3Serializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = RecommendedTech3.objects.filter(TaskId=id)
        serializer = RecommendedTech3Serializer(instance, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = RecommendedTech3.objects.filter(TaskId=id)
        serializer = RecommendedTech3Serializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = RecommendedTech3.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      


class Re4view(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = RecommendedTech4.objects.filter(TaskId=id)
        serializer = RecommendedTech4Serializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = RecommendedTech4.objects.filter(TaskId=id)
        serializer = RecommendedTech4Serializer(instance, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = RecommendedTech4.objects.filter(TaskId=id)
        serializer = RecommendedTech4Serializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = RecommendedTech4.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Re5view(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = RecommendedTech5.objects.filter(TaskId=id)
        serializer = RecommendedTech5Serializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = RecommendedTech5.objects.filter(TaskId=id)
        serializer = RecommendedTech5Serializer(instance, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = RecommendedTech5.objects.filter(TaskId=id)
        serializer = RecommendedTech5Serializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = RecommendedTech5.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


class Re6view(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = RecommendedTech6.objects.filter(TaskId=id)
        serializer = RecommendedTech6Serializer(instance, many=True)
        return Response(serializer.data)

    def post(self, request, id):
        instance = RecommendedTech6.objects.filter(TaskId=id)
        serializer = RecommendedTech6Serializer(instance, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = RecommendedTech6.objects.filter(TaskId=id)
        serializer = RecommendedTech6Serializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = RecommendedTech6.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #queryset = ResultTech.objects.all()
    #serializer_class = ResultTechSerializer
class Resview(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        instance = ResultTech.objects.filter(TaskId=id)
        serializer = ResultTechSerializer(instance, many=True)
        return Response(serializer.data)

    # def post(self, request, id):
    #     instance = RecommendedTech6.objects.filter(TaskId=id)
    #     serializer = RecommendedTech6Serializer(instance, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

    def put(self, request, id):
        instance = ResultTech.objects.filter(TaskId=id)
        serializer = ResultTechSerializer(instance, many=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
        i
    def delete(self, requset, id):
        instance = ResultTech.objects.filter(TaskId=id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                                       

# class FileView(mixins.CreateModelMixin,
#                mixins.RetrieveModelMixin,
#                mixins.DestroyModelMixin,
#                viewsets.GenericViewSet):
#     permission_classes = [AllowAny]
#     queryset = File.objects.filter(taskId=id)
#     serializer = FileSerializer             
#     # 여기에 파일을 실질적으로 담는다 ㅇㅋ?



class MyModelViewSets(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = TestingTasks
    query = 'select * from users_user;'
    queryset = User.objects.raw(query)
    serializer_class = UserSerializer


class TestingViewsets(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    permission_classes = [AllowAny]

    queryset = TestingTasks.objects.all()
    serializer_class = TestingSerializer

class TasksViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    permission_classes = [AllowAny]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer    


class NeuralDropViewsets(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    permission_classes = [AllowAny]

    queryset = NeuralDropTasks.objects.filter()
    serializer_class = NeuralDropTaskSerializer


class testingapi(APIView):
    """
    testing for fboe
    """
    permission_classes = [AllowAny]

    def get(self, request):
        viewtesting = NeuralDropTask.objects.all()
        serializer = NeuralDropTaskSerializer(viewtesting, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DatafileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TaskView(mixins.CreateModelMixin,
#                mixins.ListModelMixin,
#                mixins.UpdateModelMixin,
#                mixins.RetrieveModelMixin,
#                mixins.DestroyModelMixin,
#                viewsets.GenericViewSet):
#     permission_classes = [AllowAny]
#     queryset = Task.objects.all()  
#     serializer = TaskSerializer        
#     #여기서는 task만 만들거야 쉽게 생각하자 쉬운코드가 좋은코드라고 했어 


class FileView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = File.objects.all()
    serializer_class = FileSerializer             
    # 여기에 파일을 실질적으로 담는다 ㅇㅋ?


class Reco1view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech1.objects.all()
    serializer_class = RecommendedTech1Serializer


class Reco2view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech2.objects.all()
    serializer_class = RecommendedTech2Serializer


class Reco2view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech2.objects.all()
    serializer_class = RecommendedTech2Serializer


class Reco3view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech3.objects.all()
    serializer_class = RecommendedTech3Serializer


class Reco4view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech4.objects.all()
    serializer_class = RecommendedTech4Serializer


class Reco5view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech5.objects.all()
    serializer_class = RecommendedTech5Serializer


class Reco6view(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = RecommendedTech6.objects.all()
    serializer_class = RecommendedTech6Serializer


class Resultview(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = ResultTech.objects.all()
    serializer_class = ResultTechSerializer





class Aiview(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = TestingAiModel.objects.all()
    serializer_class = AiSerializer
    #   def post(self, request):
    #     serializer = DatafileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def send_email(data):
    email = EmailMessage(to=[data['to_email']],
    subject=data['email_subject'], body=data['email_body'])
    email.send()

# class ContactusView(APIView):
#     """
#      NeuralDrop page Contact us 
#      if user post the message API sends the message 
#      to CEO and send message to user about thanks-word
#     """
#     permission_classes = [AllowAny]    
#     def post(self, request):
#         serializer = ContactUsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             customer = ContactUs.objects.get(email=serializer.data.get('email'))
#             #customer = ContactUs.objects.values('pk')
#             email_body = 'here is the customer information\n'+customer.company+'\nand here is name'+customer.firstName+','+customer.lastName+'\ncustomer email='+customer.email+'\nand here is the text that written by customer'+customer.message
#             data = {
#                 'to_email':'thdgk1245@naver.com',
#                 'email_body':email_body,
#                 'email_subject':'Customer send to message: '+customer.company
#             }
#             #email이 계속 중복되면 multipleobject error 발생!
#             send_email(data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class ContactusView(APIView):
    """
     NeuralDrop page Contact us 
     if user post the message API sends the message 
     to CEO and send message to user about thanks-word
    """
    permission_classes = [AllowAny]    
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email=serializer.data.get('email')
            company=serializer.data.get('company')
            firstName=serializer.data.get('firstName')
            lastName=serializer.data.get('lastName')
            message=serializer.data.get('message')
            #customer = ContactUs.objects.values('pk')
            email_body = 'here is the customer information\n'+company+'\nand here is name'+firstName+','+lastName+'\ncustomer email='+email+'\nand here is the text that written by customer'+message
            data = {
                'to_email':'thdgk1245@naver.com',
                'email_body':email_body,
                'email_subject':'Customer send to message:'+company +' name :'+firstName+lastName
            }
            #email이 계속 중복되면 multipleobject error 발생!
            send_email(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
