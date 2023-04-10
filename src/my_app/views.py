from django.shortcuts import render
from django.views import View


# Create your views here.

class MyView(View):
    def get(self, req):
        print(req)
        return render(req, "index.html", context={"VARS": 124})

    def post(self, req):
        print(req)
        return render(req, "index.html", context={"VARS": 125})
