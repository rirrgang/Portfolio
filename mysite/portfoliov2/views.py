
from django.shortcuts import render, get_object_or_404
import datetime
from django.core import serializers
from django.http import JsonResponse
from django.utils.translation import activate
from django.urls import reverse
from django.http import HttpResponseRedirect
from sendgrid.helpers.mail import *
from sendgrid import SendGridAPIClient
from django.conf import settings
from portfoliov2.forms import ContactForm
from portfoliov2.models import ExperienceStations
from portfoliov2.models import Projects
from portfoliov2.models import ProjectModels
from portfoliov2.models import ProjectMusic
from portfoliov2.models import ProjectProgramming
from portfoliov2.models import Article
from portfoliov2.models import ArticlePicture
from portfoliov2.models import ArticleVideo
from portfoliov2.models import ArticleCodeExample
from portfoliov2.models import ArticleCodeLinks
from django.shortcuts import render
import os
from django.utils.translation import gettext as _

# Create your views here.

######################   CONTEXT FUNCTIONS   #####################

context = {
    'isOnePage': True,
    'extendHTML': 'portfolio_base.html',
}


def resetContext():
    global context
    context = {
        'isOnePage': True,
        'extendHTML': 'portfolio_base.html',
    }
    return context


def getContext(iOP=True):
    context['isOnePage'] = iOP
    if context['isOnePage'] == True:
        context['extendHTML'] = 'portfoliov2_null.html'
    else:
        context['extendHTML'] = 'portfoliov2_base.html'
    return context


def addToContext(data):
    context.update(data)


######################   BASE ONEPAGE   #####################

def basev2(request):
    resetContext()
    if request.method == "POST":
        result = handle_contact_form(request)
        if result:
            return result
    else:
        form = {'form': ContactForm()}
        addToContext(form)

    # Model loading into context for all the other templates
    #ABOUT#
    expStations = ExperienceStations.objects.all()
    expStations = expStations.order_by("date_from")
    # Load language-specific columns
    for expStation in expStations:
        try:
            expStation.title = getattr(
                expStation, 'title_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            expStation.title = expStation.title_en

        try:
            expStation.station = getattr(
                expStation, 'station_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            expStation.station = expStation.station_en

        try:
            expStation.description = getattr(
                expStation, 'description_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            expStation.description = expStation.description_en

    modelEntries = {"expStations": expStations}
    addToContext(modelEntries)
    #ABOUT#
    # Load additional project cards
    #PROJECTS#
    # load the model
    model = Projects
    language_code = request.LANGUAGE_CODE

    if is_ajax(request):
        category = request.GET.get('category')
        per_page = 3  # Number of model entries per page

        # Get the primary keys of the entries that have already been loaded
        already_loaded_entries = request.session["alreadyLoadedModelEntries"]

        # retrieve the model name
        model_name = model.objects.model.__name__.lower()
        # filter model by category
        if category == 'All':
            additional_model_entries = model.objects.exclude(isVisible=False).exclude(
                pk__in=already_loaded_entries).order_by('pk').order_by('-category')[:per_page]
        else:
            additional_model_entries = model.objects.filter(category=category).exclude(
                pk__in=already_loaded_entries).exclude(isVisible=False).order_by('pk').order_by('-category')[:per_page]

        # Add the primary keys of the new entries to the session variable
        request.session["alreadyLoadedModelEntries"] += [
            entry.pk for entry in additional_model_entries]

        # Serialize the entries and return as JSON
        serializedEntries = getAdditionalModelEntriesAsJSON(
            model=additional_model_entries)
        for entry in serializedEntries:
            entry['title'] = entry.get(
                f'title_{language_code}', entry['title_en'])
            entry['details'] = entry.get(
                f'details_{language_code}', entry['details_en'])
            entry['description'] = entry.get(
                f'description_{language_code}', entry['description_en'])
        data = {model_name: serializedEntries}
        return JsonResponse(data)

    # Create session variables for each category
    request.session["alreadyLoadedModelEntries"] = []

    # Handle the regular request for rendering the template
    models = model.objects.exclude(
        isVisible=False).order_by('pk').order_by('-category')[0:3]
    for model in models:
        model.title = getattr(model, f'title_{language_code}', model.title_en)
        model.details = getattr(
            model, f'details_{language_code}', model.details_en)
        model.description = getattr(
            model, f'description_{language_code}', model.description_en)
    request.session["alreadyLoadedModelEntries"] += [
        entry.pk for entry in models]
    modelEntries = {"projects": models}
    print(modelEntries)
    addToContext(modelEntries)
    #PROJECTS#
    return render(request, "portfoliov2_base.html", getContext())

######################   HOME   #####################


def home(request):
    return render(request, "portfoliov2_home.html", getContext(iOP=False))

######################   ABOUT   #####################


def about(request):
    context = getContext(iOP=False)
    expStations = ExperienceStations.objects.all()
    expStations = expStations.order_by("date_from")
    # Load language-specific columns
    for expStation in expStations:
        try:
            expStation.title = getattr(
                expStation, 'title_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            expStation.title = expStation.title_en

        try:
            expStation.station = getattr(
                expStation, 'station_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            expStation.station = expStation.station_en

        try:
            expStation.description = getattr(
                expStation, 'description_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            expStation.description = expStation.description_en

    modelEntries = {"expStations": expStations}
    addToContext(modelEntries)
    return render(request, "portfoliov2_about.html", context)

######################   HELP FUNCTIONS   #####################


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def getAdditionalModelEntriesAsJSON(model=None):
    if not model:
        print("The Model does not have more entries")
        return []

    # Retrieve all instances of the model class
    all_entries = model

    # Create a list of dictionaries for the serialized entries
    serialized_entries = []
    for entry in all_entries:
        entry_dict = vars(entry)
        serialized_entry = {}
        for key, value in entry_dict.items():
            if isinstance(value, (str, int, bool, float)) or value is None:
                serialized_entry[key] = value
            elif isinstance(value, datetime.datetime):
                serialized_entry[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            else:
                serialized_entry[key] = str(value)
        serialized_entries.append(serialized_entry)

    return serialized_entries

######################   PROJECTS   #####################


def projects(request):
    # load the model
    model = Projects

    language_code = request.LANGUAGE_CODE

    if is_ajax(request):
        category = request.GET.get('category')
        per_page = 3  # Number of model entries per page

        # Get the primary keys of the entries that have already been loaded
        already_loaded_entries = request.session["alreadyLoadedModelEntries"]

        # retrieve the model name
        model_name = model.objects.model.__name__.lower()
        # filter model by category
        if category == 'All':
            additional_model_entries = model.objects.exclude(isVisible=False).exclude(
                pk__in=already_loaded_entries).order_by('pk').order_by('-category')[:per_page]
        else:
            additional_model_entries = model.objects.filter(category=category).exclude(
                pk__in=already_loaded_entries).exclude(isVisible=False).order_by('pk').order_by('-category')[:per_page]

        # Add the primary keys of the new entries to the session variable
        request.session["alreadyLoadedModelEntries"] += [
            entry.pk for entry in additional_model_entries]

        # Serialize the entries and return as JSON
        serializedEntries = getAdditionalModelEntriesAsJSON(
            model=additional_model_entries)
        for entry in serializedEntries:
            entry['title'] = entry.get(
                f'title_{language_code}', entry['title_en'])
            entry['details'] = entry.get(
                f'details_{language_code}', entry['details_en'])
            entry['description'] = entry.get(
                f'description_{language_code}', entry['description_en'])
        data = {model_name: serializedEntries}
        return JsonResponse(data)

    # Create session variables for each category
    request.session["alreadyLoadedModelEntries"] = []

    # Handle the regular request for rendering the template
    models = model.objects.exclude(isVisible=False).order_by(
        'pk').order_by('-category')[0:3]
    for model in models:
        model.title = getattr(model, f'title_{language_code}', model.title_en)
        model.details = getattr(
            model, f'details_{language_code}', model.details_en)
        model.description = getattr(
            model, f'description_{language_code}', model.description_en)
    request.session["alreadyLoadedModelEntries"] += [
        entry.pk for entry in models]
    modelEntries = {"projects": models}
    addToContext(modelEntries)
    return render(request, "portfoliov2_projects.html", getContext(iOP=False))


def get_object_or_empty(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return {}


def modelDetail(request, pk):
    # load the project
    project = get_object_or_404(Projects, pk=pk)
    if project is not None:
        try:
            project.title = getattr(
                project, 'title_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            project.title = project.title_en
        try:
            project.description = getattr(
                project, 'description_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            project.description = project.description_en
        try:
            project.details = getattr(
                project, 'details_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            project.details = project.details_en
    model = get_object_or_empty(ProjectModels, project=pk)
    addToContext({"project": project})
    addToContext({"model": model})
    print(project)
    return render(request, "portfoliov2_modelDetail.html", getContext(iOP=False))


def musicDetail(request, pk):
    # load the project
    project = get_object_or_404(Projects, pk=pk)
    if project is not None:
        try:
            project.title = getattr(
                project, 'title_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            project.title = project.title_en
        try:
            project.description = getattr(
                project, 'description_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            project.description = project.description_en
        try:
            project.details = getattr(
                project, 'details_%s' % request.LANGUAGE_CODE)
        except AttributeError:
            project.details = project.details_en
    music = get_object_or_empty(ProjectMusic, project=pk)
    addToContext({"project": project})
    addToContext({"music": music})
    return render(request, "portfoliov2_musicDetail.html", getContext(iOP=False))


def programmingDetail(request, pk):
    # load the project
    project = get_object_or_404(Projects, pk=pk)
    project.title = getattr(project, 'title_%s' % request.LANGUAGE_CODE)
    # load the programming project object
    programming = get_object_or_empty(
        ProjectProgramming, project=project)

    data = {
        'project': project,
        'programming': programming,
        'articles': [],
    }

    # Retrieve the articles related to the project programming
    articles = Article.objects.filter(projectProgramming=programming)

    # Iterate over each article and retrieve the associated pictures and code examples
    for article in articles:
        pictures = ArticlePicture.objects.filter(article=article)
        videos = ArticleVideo.objects.filter(article=article)
        code_examples = ArticleCodeExample.objects.filter(article=article)
        code_links = ArticleCodeLinks.objects.filter(article=article)

        article.title = getattr(article, 'title_%s' % request.LANGUAGE_CODE)
        article.content = getattr(article, 'content_%s' %
                                  request.LANGUAGE_CODE)

        # Create a dictionary representation of the article with its related pictures and code examples
        article_data = {
            'article': article,
            'pictures': pictures,
            'videos': videos,
            'code_examples': code_examples,
            'code_links': code_links,
        }

        # Add the article data to the 'articles' list in the main data dictionary
        data['articles'].append(article_data)

    print("DATA: " + str(data))

    addToContext({"data": data})
    return render(request, "portfoliov2_programmingDetail.html", getContext(iOP=False))


######################   CONTACT   #####################


def send_email(name, email, subj, message):
    content = "Name: {}\nE-Mail: {}\nSubject: {}\nMessage: {}".format(
        name, email, subj, message)
    mail = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=settings.DEFAULT_TO_EMAIL,
        subject="New Contact E-Mail from {}".format(name),
        plain_text_content=content
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


def handle_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()
            send_email(name, email, subject, message)
            return render(request, "portfoliov2_contactSuccess.html", getContext(False))
        else:
            form = ContactForm()
    return None


def contact(request):
    if request.method == "POST":
        result = handle_contact_form(request)
        if result:
            return result
    else:
        form = {'form': ContactForm()}
        addToContext(form)
    return render(request, "portfoliov2_contact.html", getContext(False))


def contactSuccess(request):
    return render(request, "portfoliov2_contactSuccess.html", getContext(False))


def legalnotice(request):
    return render(request, "portfoliov2_legalnotice.html", getContext(False))


def switchLanguage(request):
    return render(request, "portfoliov2_switchLanguage.html", getContext(False))
