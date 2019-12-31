from django import forms

from .models import Post, Login

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ( 'title', 'description', 'text')


class LoginForm(forms.Form):
	email = forms.CharField(widget=forms.EmailInput)
	passwd = forms.CharField(widget=forms.PasswordInput)
	#passwd = forms.ChaField(widget=forms.TextInput)

	class Meta:
		model = Login
		fieds = ('email', 'passwd')

	def login_save(self):
		self.sabe()