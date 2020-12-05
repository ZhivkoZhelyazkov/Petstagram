from django import forms


# this will take all the pets
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'

class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',
            }
        )
    )
