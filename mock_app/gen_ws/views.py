from django.shortcuts import render
from django.views.generic import View


class SendHttpRequest(View):

    template_name = 'request_table.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    

