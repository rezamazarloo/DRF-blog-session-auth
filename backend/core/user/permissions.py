# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# class AuthorUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    
#     def test_func(self):
#         return self.request.user.groups.filter(name='author').exists() and 

#     def handle_no_permission(self):
#         return JsonResponse(
#             {'message': 'Only company administrators have access to this view'}
#         )


# https://stackoverflow.com/questions/65241141/django-userpassestestmixin-confusion-questions