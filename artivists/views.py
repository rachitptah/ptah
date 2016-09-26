from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.views import generic
from django.views.generic import TemplateView
from .forms import UserForm


class UserFormView (TemplateView):
	template_name = "signup.html"
	#display signup blank form
	def get(self, request,*args,**kwargs):
		context = super(UserFormView,self).get_context_data(**kwargs)
		return self.render_to_response(context)


	#process form data
	def post(self, request,*args,**kwargs):
		data = request.POST
		user = get_user_model().objects.create(username=data["username"],first_name=data["first_name"],email=data["email"],last_name=data["last_name"])
		user.set_password(data["password"])
		user.save()
		user.backend = "django.contrib.auth.backends.ModelBackend"
		# form = self.form_class(request.POST)

		# if form.is_valid():

		# 	user = form.save(commit=False)

		# 	#cleaned (normalized) data
		# 	username = form.cleaned_data['username']
		# 	password = form.cleaned_data['password']
		# 	user.set_password(password)
		# 	user.save()

		# 	# Returns User objects if credentials are correct

		# 	user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("home")

		return render(request, self.template_name, {'form': form})

class UserLoginView (TemplateView):
	template_name = "login.html"
	#display signup blank form
	def get(self, request,*args,**kwargs):
		context = super(UserLoginView,self).get_context_data(**kwargs)
		return self.render_to_response(context)

	#process form data
	def post(self, request,*args,**kwargs):
		data = request.POST
		# user = get_user_model()
		user = authenticate(username=data["username"], password=data["password"])
		user.backend = "django.contrib.auth.backends.ModelBackend"
		if user is not None:
			login(request, user)
			return redirect("home")

class UserLogoutView (TemplateView):
	def get(self, request, *args, **kwargs):
		logout(request)
		return redirect("home")
