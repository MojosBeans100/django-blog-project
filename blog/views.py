from django.shortcuts import render
from django.views import generic 
from .models import Post

# Django Views are one of the vital participants of MVT Structure of Django. 
# As per Django Documentation, 
# A view function is a Python function that takes a Web request and returns a Web response. 

# 1 create the view code
# 2 create the view templates
# 3 connect up our URLS to the urls file

class PostList(generic.ListView):

    # use Post as its model
    model = Post

    # the contencts of our post table, filtered by status (1 = published, 0 = draft)
    # ordered in descending order (minus sign)
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    # HTML file which our view will render
    template_name = 'index.html'

    # list views provides build in view to paginate displayd list
    # limiting number of posts on front page
    paginate_by = 6



