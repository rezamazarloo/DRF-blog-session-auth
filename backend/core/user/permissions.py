from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.http import JsonResponse


class AuthorUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        is_author = self.request.user.groups.filter(name="author").exists()
        has_profile_update_permission = Group.objects.get(name='author').permissions.filter(codename="change_profile").exists()
        return is_author and has_profile_update_permission

    def handle_no_permission(self):
        return JsonResponse({'message': 'Only authors can update profiles.'}, status=403)
