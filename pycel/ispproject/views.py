from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Project
from django.urls import reverse
from django.views import  generic



class IndexView(generic.ListView):
    template_name = 'ispproject/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Project.objects.order_by('-pub_date')[:5]

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

class SelectView(generic.TemplateView):
    template_name = 'ispproject/select.html'
