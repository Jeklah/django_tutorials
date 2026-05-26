from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    # Return a specfic column from the database
    mydata = Member.objects.all().values_list('firstname')
    # Return a specific row from the database
    mydata = Member.objects.filter(firstname='Emil').values()
    # Filtering with an AND condition
    mydata = Member.objects.filter(id=2, lastname='Refsnes').values()
    # Filtering with an OR condition
    mydata = Member.objects.filter(firstname='Emil').values(
    ) | Member.objects.filter(firstname='Tobias').values()
    # Using Q expressions for an OR condition
    mydata = Member.objects.filter(
        Q(firstname='Emil') | Q(firstname='Tobias')).values()
    template = loader.get_template('template.html')
    context = {
        # 'mymembers': mydata,
        'fruits': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))
