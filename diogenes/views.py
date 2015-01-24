from django.shortcuts import render
from forms import BookForm
from models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request, 'diogenes/about.html')

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            # this line
            form.instance.user = request.user
            form.save(commit=True)
            #book.user = request.user
            #book.save()

            return HttpResponseRedirect('/diogenes/')
        else:
            print form.errors

    else:
        form = BookForm()

    return render(request, 'diogenes/add_book.html', {'form': form})

@login_required
def delete_book(request):
    book_id = None
    if request.method == 'GET':
        book_id = request.GET['book_id']

        Book.objects.filter(id=int(book_id)).delete()
        print "Book %d deleted successfully." % int(book_id)

    return HttpResponse(book_id)

@login_required
def edit_book(request, book_slug):
    if request.method == 'GET':
        book = Book.objects.get(slug=book_slug)
        form = BookForm(instance=book)

    else:
        book = Book.objects.get(slug=book_slug)
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect('/diogenes/')
        else:
            print form.errors

    return render(request, 'diogenes/edit_book.html', {'form': form, "book_slug": book_slug})


def index(request):
    if request.user.is_authenticated():
        book_list = Book.objects.filter(user=request.user)
    else:
        book_list = Book.objects.order_by('title')
    context_dict = {'books': book_list}

    return render(request, 'diogenes/index.html', context_dict)

def collection(request):
    book_list = Book.objects.order_by('title')
    context_dict = {'books': book_list}

    return render(request, 'diogenes/collection.html', context_dict)