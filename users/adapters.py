from allauth.account.adapter import DefaultAccountAdapter
import logging

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user =  super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.role = data.get('role', 3)
        user.save()
        return user