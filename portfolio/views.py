# from django.shortcuts import render
# from .models import Images
# from django.core.mail import EmailMessage
#
# def home(request):
#     context = {}
#     images = Images.objects.all()
#     context["images"] = images
#
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         subject = request.POST.get("subject")
#         message = request.POST.get("message")
#
#         email_message = EmailMessage(
#             subject = name + " : " +subject,
#             body = message,
#             to = ['your gmail'],
#             headers = {"Reply-To": email}
#         )
#         email_message.send()
#     return render(request, "index.html", context)


from django.views.generic import ListView
from .models import Images, Category


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"


class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Images.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context