# from django.contrib.auth import get_user_model
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse
# from django.utils.translation import gettext_lazy as _
# from django.views.generic import DetailView, RedirectView, UpdateView
from api.users.models import *
from api.users.serializers import *
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets


# class NeuralDropTaskapi(viewsets.ModelViewSet):
#     pass


class NeuralDropViewsets(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):

    permission_classes = [AllowAny]

    queryset = NeuralDropTasks.objects.all()
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

# class DataFileViewSet(viewsets.ModelViewSet):
#
#     serializer_class = DatafileSerializer
#     queryset = Datafile.objects.all()

# class NoteViewSet(viewsets.ModelViewSet):
#
#     serializer_class = NoteSerializer
#     queryset = CompanyTesting.objects.all()
#
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)
#
#     def get_queryset(self):
#         return self.queryset.filter(created_by=self.request.user)
#
#
# class SnippetList(generics.ListCreateAPIView):
#     permission_classes = [AllowAny]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [AllowAny]
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     permission_classes = [AllowAny]
#
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     permission_classes = [AllowAny]
#
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class UserDetailView(LoginRequiredMixin, DetailView):
#
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#
#
# user_detail_view = UserDetailView.as_view()
#
#
# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#
#     model = User
#     fields = ["name"]
#     success_message = _("Information successfully updated")
#
#     def get_success_url(self):
#         assert (
#             self.request.user.is_authenticated
#         )  # for mypy to know that the user is authenticated
#         return self.request.user.get_absolute_url()
#
#     def get_object(self):
#         return self.request.user
#
#
# user_update_view = UserUpdateView.as_view()
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#
#     permanent = False
#
#     def get_redirect_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})
#
#
# user_redirect_view = UserRedirectView.as_view()
