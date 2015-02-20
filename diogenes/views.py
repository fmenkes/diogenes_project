from django.shortcuts import render
from forms import BookForm
from models import Book
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def about(request):
    return render(request, 'diogenes/about.html')


def sorry(request):
    return render(request, 'diogenes/sorry.html')


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
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.user.id != request.user.id:
        return sorry(request)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save(commit=True)

            return HttpResponseRedirect('/diogenes/')
        else:
            print form.errors

    return render(request, 'diogenes/edit_book.html', {'form': form, 'book': book})


def index(request):
    if request.user.is_authenticated():
        book_list = Book.objects.filter(user=request.user).order_by('clean_title')
    else:
        book_list = Book.objects.order_by('clean_title')
    context_dict = {'books': book_list}

    return render(request, 'diogenes/index.html', context_dict)


def collection(request):
    # Not the best way to do it perhaps, maybe think of something else?
    book_list = Book.objects.filter(user=User.objects.get_by_natural_key('francis')).order_by('clean_title')
    context_dict = {'books': book_list}

    return render(request, 'diogenes/collection.html', context_dict)