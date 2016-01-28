from django.shortcuts import render
from .forms import SignUpForm, LoginForm
from django.shortcuts import render_to_response
from .models import Document
from .forms import DocumentForm
from django.template import RequestContext
# Create your views here.

def sign_up(request):
    title = "Welcome"
    form = LoginForm(request.POST or None)
    context = {
        "title" : title,
        "form" : form,

    }

    return render(request, "home.html", context)
menu = [
        [1, 0],
        [2, 1],
        [3, 1],
        [4, 3],
        [5, 3],
        [6, 5],
        [7,1]
        ]

# menu1 = {0: [1], 1: [2, 3, 7], 3: [4, 5], 5: [6]}

menu = [map(str,i) for i in menu]
def welcome(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        if request.POST["username"] == "admin" and request.POST["password"] == "admin":
            context = {}
            for element in menu:
                if element[1] not in context:
                    context[element[1]] = []
                context[element[1]].append(element[0])
        else:
            context = {
                "title" : "Please Try Again hehehe!"
            }

    return render(request, "thankyou.html", dict(context=context))

def document_show(request, doc_name):
     context = {
                "title" : "thats my boy",
                "id"    : doc_name
            }
     return render(request, "document_view.html", context)


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            context = {
                "title" : "thats my boy",
            }
            # Redirect to the document list after POST
            # return render(request, "document_view.html", context)
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'thankyou.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


# def home(request):
#     title = "Welcome"
#     form = SignUpForm(request.POST or None)
#     # if request.user.is_authenticated():
#     #     title = "Authenticated Title: %s" % request.user
#     # if request.method == "POST":
#     #     print request.POST
#     context = {
#         "title" : title,
#         "form" : form,
#
#     }
#
#     if form.is_valid():
#         instance = form.save(commit=False)
#         if instance.name == "admin" and instance.email == "admin@ipv.com":
#             context = {
#                 "title" : "Thank you"
#             }
#         else:
#             context = {
#                 "title" : "Please Try Again!"
#             }
#
#     return render(request, "home.html", context)
#
