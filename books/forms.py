from django import forms
from django.forms import Textarea

from books.models import Review


class BookReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["review", ]

        widgets = {
            "review": Textarea(attrs={"cols": 80, "rows": 20}),
        }
