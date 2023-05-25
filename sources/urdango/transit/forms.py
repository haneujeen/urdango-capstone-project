from django import forms


class RouteForm(forms.Form):
    START_POINT_CHOICES = [
        ('subway', 'Subway'),
        ('bus', 'Bus'),
        ('both', 'Both'),
    ]
    start_point = forms.CharField(label='Starting point (Station or Stop name)', max_length=200, required=True)
    end_point = forms.CharField(label='Ending point (Station or Stop name)', max_length=200, required=True)
    transportation = forms.ChoiceField(choices=START_POINT_CHOICES, required=True)
