from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
# Create your views here.

from cardndice.polls.models import Choices, Poll

# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

# def detail(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/detail.html', {'poll': p})

@login_required
def vote(request, object_id):
    p = get_object_or_404(Poll, pk=object_id)
    try:
        selected_choice = p.choices_set.get(pk=request.POST['choice'])
    except (KeyError, Choices.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/poll_detail.html', {
                'object': p,
                'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        p.choices_set.order_by('votes')
        return HttpResponseRedirect('/polls/%s/results' % p.id)

# def results(request, poll_id):
#     p = get_object_or_404(Poll, pk=poll_id)
#     return render_to_response('polls/results.html', {'poll': p})
