from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.db.models import Q
from django.forms.util import ErrorList
from django.contrib import messages
from utils.group_decorator import group_admin_required, is_admin
from intranet.models import Member, PreMember
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from intranet.member_database.forms import NewMemberForm, EditMemberForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json


def main(request):
   pre_members = PreMember.objects.all()
   return render_to_response('intranet/acoustics/main.html',{
      "section":"intranet",
      "page":'acoustics',
      "pre_members": pre_members
   },context_instance=RequestContext(request))


def skip(request):
    return HttpResponse(json.dumps({'success': True}), content_type="application/json")


def state(request):
    return HttpResponse(json.dumps({
        'state': 1,
        'volume': 50,
        'time_left': 100,
        'currently_playing': {
            'id': 304,
            'name': 'We are the music makers',
            'artist': 'Aphex Twin',
            'length': 500,
            'album_name': 'Selected Ambient Works 85-92',
            'album_art_url': 'http://upload.wikimedia.org/wikipedia/en/thumb/d/d9/Selected_ambient_works_85-92.jpg/220px-Selected_ambient_works_85-92.jpg',
        },
    }), content_type="application/json")


def search(request):
    pass


def queue(request):
    return HttpResponse(json.dumps([
        {
            'votes': 10,
            'song': {
                'id': 301,
                'name': 'Purple Haze',
                'artist': 'Jimmy Hendrix',
                'length': 200,
                'album_name': 'Jimmy Henrix\'s Album',
                'album_art_url': 'http://www.writeawriting.com/wp-content/uploads/2011/03/Why-did-Jimi-Hendrix-Write-Wrote-Purple-Haze-.jpg',
            },
            'votes': 9,
            'song': {
                'id': 999,
                'name': 'Radioactive',
                'artist': 'Imagine Dragons',
                'length': 900,
                'album_name': 'Night Visions',
                'album_art_url': 'http://a4.mzstatic.com/us/r1000/109/Music/v4/04/15/78/04157815-169d-9f91-d596-342dee2f4c46/UMG_cvrart_00602537150120_01_RGB72_1200x1200_12UMGIM46901.170x170-75.jpg',
            },
        },
    ]), content_type="application/json")


def vote(request):
    pass
