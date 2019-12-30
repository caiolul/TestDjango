from django import forms

from .models import Post, Login

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ( 'title', 'description', 'text')


"""class LoginForm(forms.ModelForm):
	#passwd = forms.TextField(widget=forms.PasswordInput)
	passwd = forms.CharField(widget=forms.TextInput)

	class Meta:
		model = Login
		fieds = ('email', 'passwd')"""