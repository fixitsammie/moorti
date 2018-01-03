from django import forms


class CampaignForm(forms.Form):
    opinion=forms.CharField(label='Write your opinion', max_length=500,widget=forms.Textarea)
    