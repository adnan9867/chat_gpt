from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from gpt_models.models import TestModel


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'


class DeployDjangoView(TemplateView):
    template_name = 'django_deployment.html'


class TestViewSet(ModelViewSet):
    permission_classes = []
    queryset = None
    serializer_class = None

    def list(self, request, *args, **kwargs):
        print(request)
        print('request hit now')
        TestModel.objects.create(request=request.META)
        return Response({'message': 'Hello World Chutiya Gus'})