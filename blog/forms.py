from django import forms
from django.core.exceptions import ValidationError

from blog.models import Post


class BlogBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class BlogCreateForm(BlogBaseForm):
    class Meta:
        model = Post
        fields = '__all__'

        error_messages = {
            'title': {
                'required': 'Please enter the title of your post',
                'max_length': f'The title is too long. Please keep it under {Post.TITLE_MAX_LENGTH} characters',
            },
        }


    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title')
        content = cleaned_data.get('description')

        if title and content and title in content:
            raise ValidationError("The post title cannot be included in the post content")

        return cleaned_data

    def save(self, commit=True):
        post = super().save(commit=False)

        post.title = post.title.capitalize()

        if commit:
            post.save()

        return post


class BlogEditForm(BlogBaseForm):
    pass


class BlogDeleteForm(BlogBaseForm):
    pass


class BlogDetailsForm(BlogBaseForm):
    pass