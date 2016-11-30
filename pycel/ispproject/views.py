from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project
from django.urls import reverse
from django.views.generic import  TemplateView, ListView, DetailView



class IndexView(ListView):
    model = Project
    template_name = 'ispproject/index.html'


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'exam/detail.html'
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'exam/results.html'
#
# def vote(request, question_id):
#     question = get_object_or_404(Question)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'exam/detail.html', {
#         'question': question,
#         'error_message': "You didn`t select a choice."
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('exam:results', args=(question.id,)))

class SelectView(ListView):
    model = Project
    template_name = 'ispproject/select.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'ispproject/detail.html'
    context_object_name = "project"
    pk_url_kwarg = 'project_id'

    def get_object(self, queryset=None):
        obj = super(ProjectDetailView, self).get_object()
        return obj



def selector(request):
    class_level = request.GET.get('class_level')
    leader_name = request.GET.get('leader_name')
    rd_name = request.GET.get('rd_name')
    pm_name = request.GET.get('pm_name')

