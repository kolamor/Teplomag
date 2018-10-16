from django import forms
from ticket.models import Tag



class TagForm(forms.ModelForm):

	# name = forms.CharField(max_length=50)
	# telephon = forms.IntegerField()
	# email_t = forms.EmailField()
	# comment = forms.CharField(max_length=50)

	# name.widget.attrs.update({'class': 'form-control'})
	# telephon.widget.attrs.update({'class': 'form-control'})
	# email_t.widget.attrs.update({'class': 'form-control'})
	# comment.widget.attrs.update({'class': 'form-control'})

	class Meta:

		model = Tag
		fields = ['name', 'telephon', 'email_t', 'comment']
		widget = {
		    'name' : forms.TextInput(attrs={'class': 'form-control'}),
		    'telephon' : forms.TextInput(attrs={'class': 'form-control'}),
		    'nemail_t' : forms.TextInput(attrs={'class': 'form-control'}),
		    'comment' : forms.TextInput(attrs={'class': 'form-control'}),
		    }


	# def save(self):
	# 	new_tag = Tag.object.create(
	# 		name=self.cleaned_data['name'],
	# 		telephon=self.cleaned_data['telephon'],
	# 		email_t=self.cleaned_data['email_t'],
	# 		comment=self.cleaned_data['comment']
	# 		)
	# 	return new_tag

