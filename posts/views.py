from django.shortcuts import render
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Post, Status
from django.urls import reverse_lazy


class PostListView(ListView):
    # model = Post
    template_name = "posts/list.html"
    # queryset attribute allow us to slect some data from the db by using the model class
    published_status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    context_object_name = "posts"

    #this method helps us to use the context however we want
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        print(context)
        return context

class PostCreateView(CreateView):
    template_name = 'posts/new.html'
    model = Post
    fields = ["title", 'subtitle', 'body', 'status']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView): 
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class PostUpdateView(UpdateView): 
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("post_list")


