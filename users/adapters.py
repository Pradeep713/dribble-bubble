from allauth.account.adapter import DefaultAccountAdapter
import logging

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user =  super().save_user(request, user, form, commit)
        data = form.cleaned_data
        logging.INFO(f"{user} and \n\n\n\n\n {data} \n\n\n\n\n\n\n\n\n")
        user.role = data.get('role', 3)
        user.save()
        return user