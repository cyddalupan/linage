from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

class CustomPasswordChangeView(PasswordChangeView):
	def form_valid(self, form):
		# Perform necessary actions after password change
		# For example, redirect to a custom success page
		return HttpResponseRedirect(reverse('home'))

	def form_invalid(self, form):
		# Perform necessary actions when the form is invalid
		return super().form_invalid(form)

	def get_success_url(self):
		# Log out the user after changing the password
		logout(self.request)
		# Redirect to a custom success page or login page
		return HttpResponseRedirect(reverse('home'))
