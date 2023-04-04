from unicodedata import name
from django.shortcuts import render,redirect

# Create your views here.
from myapp.forms import BookForm,BookModelForm,RegistrationForm,LoginForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView
from myapp.models import books,Books
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator



def signin_required(fn):
    def wrapper(request,*args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"signin required")
            return redirect("signin")
        else:
            return fn(request,args,*kwargs)
    return wrapper


@method_decorator(signin_required,name="dispatch")
class BookCreateView(CreateView):
    model=Books
    form_class=BookModelForm
    template_name="add-book.html"
    success_url=reverse_lazy("book-list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"added successfully")
        return super().form_valid(form)

@method_decorator(signin_required,name="dispatch")
class BookListView(ListView):
        model=Books
        context_object_name="books"
        template_name="book-list.html"

        # def get_queryset(self):
        #      return Books.objects.filter(author=self.request.user)

@method_decorator(signin_required,name="dispatch")
class BookDetailView(DetailView):
        model=Books
        context_object_name="books"
        template_name="book-detail.html"
        pk_url_kwarg: str="id"
        

@method_decorator(signin_required,name="dispatch")
class BookDeleteView(View):
    def get(self,request,args,*kwargs):
        id=kwargs.get("id")
        Books.objects.filter(id=id).delete()
        messages.success(request,"deleted successfully")
        return redirect("book-list")

@method_decorator(signin_required,name="dispatch")
class BookEditView(UpdateView):
    model=Books
    form_class=BookModelForm
    template_name="book-update.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("book-list")

    def form_valid(self, form):
        messages.success(self.request,"updated successfully")
        return super().form_valid(form)


class RegistrationView(View):
    def get(self,request,args,*kwargs):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,args,*kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            User.objects.create_user(**form.cleaned_data)
            # messages.success(request,"Registration Successful")
            return redirect("signin")
        else:
            messages.error(request,"Failed to Register")
            return render(request,"registration.html",{"form":form})

class LoginView(View):
    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("login successfully")
                return redirect("book-list")
            else:
                print("login failed")
                messages.error(request,"invalid Credentials")
                return render(request,"login.html",{"form":form})

@signin_required
def signout(request,*args, **kwargs):
    logout(request)
    return redirect("signin")