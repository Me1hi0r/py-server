class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("custom middleware before")
        request.cf = True

        response = self.get_response(request)

        print("custom middleware after")

        return response