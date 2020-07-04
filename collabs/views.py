from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from .models import Researcher, Author, Collaboration, PubSubmission
from .forms import PubSubmissionForm

import itertools

def home(request):
    return render(request, 'home.html')

def researcher(request, rid):
    r = get_object_or_404(Researcher, rid__exact=rid)

    cids = Author.objects.filter(rid__exact=r.rid) \
        .values_list('cid', flat=True)
    collabs = Collaboration.objects.filter(cid__in=cids).values()

    authorships = Author.objects \
        .filter(cid__in=cids) \
        .values('cid', 'rid', 'author_index')
    cid_to_authorship = _aggregate_authorships(authorships)   

    collaborators = Researcher.objects \
            .filter(rid__in=authorships.values_list('rid', flat=True)) \
            .values('rid', 'name')
    rid_to_collaborator = {c['rid']:c for c in collaborators}
    for c in collaborators:
        c['url']= reverse('researcher', kwargs=dict(rid=c['rid']))

    edges = []
    vertices = [dict(id=r.rid, key=0)] \
            + [dict(id=c['rid'], key=1) for c in collaborators
               if c['rid'] != r.rid]

    for collab in collabs:
        rids = [a['rid'] for a in cid_to_authorship[collab['cid']]]
        authors = [rid_to_collaborator[rid] for rid in rids]

        for author in authors:
            author['count'] = author.get('count', 0) + 1
            edges.append(dict(source=r.rid, target=author['rid'], value=1))

        for a1, a2 in itertools.combinations(authors, 2):
            edges.append(dict(source=a1['rid'], target=a2['rid'], value=0))

        collab['authors'] = ', '.join(a['name'] for a in authors)

    return render(request, 'researcher.html',
                  {'researcher':r, 'collabs':collabs,
                   'collaborators':list(rid_to_collaborator.values()),
                   'rid_to_collaborator':rid_to_collaborator,
                   'graph':dict(vertices=vertices, edges=edges)})

def _aggregate_authorships(authorships):
    cid_to_authorship = dict()
    for authorship in authorships:
        cid_to_authorship.setdefault(authorship['cid'], list()) \
                .append(authorship)
    return cid_to_authorship

def search(request):
    name_pattern = request.GET.get('name')
    researchers = Researcher.objects.filter(name__icontains=name_pattern)
    return render(request, 'search_results.html',
                  {'researchers':researchers})

def pub_submit(request):
    if request.method == 'POST':
        form = PubSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PubSubmissionForm()
    return render(request, 'pub_submit.html', {'form':form})

def pub_submissions(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    submissions = PubSubmission.objects.all()
    return render(request, 'pub_submissions.html',
                  {'pub_submissions':submissions})

def pub_review(request, pk):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.method == 'POST':
        form = PubSubmissionForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            rids = [int(x) for x in form.cleaned_data['authors'].split(',')]
            year = form.cleaned_data['year']
            venue = form.cleaned_data['venue']
            type = form.cleaned_data['type']

            collab = Collaboration.objects.create(title=title, year=year,
                                                  venue=venue, type=type)
            for i, rid in enumerate(rids):
                Author.objects.create(cid_id=collab.cid, rid_id=rid,
                                      author_index=i)
            
            PubSubmission.objects.get(pk=pk).delete()

            return redirect('home')
    else:
        p = PubSubmission.objects.get(pk=pk)
        form = PubSubmissionForm(instance=p)
    return render(request, 'pub_review.html', {'form':form, 'pk':pk})
