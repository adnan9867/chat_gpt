from django.http import HttpResponseForbidden


class AdminHostMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the HTTP_HOST matches the allowed host
        if request.META.get('HTTP_HOST') == '34.217.76.153' and 'admin' in request.path:
            return self.get_response(request)
        elif request.META.get('HTTP_HOST') == '34.217.76.153' and 'admin' not in request.path:
            return HttpResponseForbidden('<h1>Forbidden</h1>')
        else:
            return self.get_response(request)
