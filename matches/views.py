from django.shortcuts import get_object_or_404, render_to_response
# Create your views here.

from cardndice.matches.models import Match, Result

def match_detail(request, match_id):
    try:
        match = get_object_or_404(Match, pk=match_id)
        results = Result.objects.filter(match=match_id)
    except Result.DoesNotExist:
        results = {}
    return render_to_response('matches/match_detail.html',
                              {'match': match,
                               'results': results})

