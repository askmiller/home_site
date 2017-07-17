from django.shortcuts import render

from django.views.generic import TemplateView

class HomeView(TemplateView):
    def get(selfself, request, **kwarts):
        return render(request, 'neuralNet/index.html', context=None)