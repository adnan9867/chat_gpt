from django.views.generic import TemplateView


class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'


class DeployDjangoView(TemplateView):
    template_name = 'django_deployment.html'
