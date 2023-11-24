from django import forms
from organization.models import BusinessInfo, InvestorType, InvestmentStage


class BusinessInfoForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo
        fields = '__all__'
        exclude = ['created_at', 'updated_at']


class BusinessCustomForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter name'}))
    employee_size = forms.IntegerField(label='Employee Size')
    owner_info = forms.CharField(label='Owner Information',
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter owner information'}))
    street = forms.CharField(label='Street', max_length=255)
    city = forms.CharField(label='City', max_length=255)
    country = forms.CharField(label='Country', max_length=255)

    investor_type = forms.ModelChoiceField(
        queryset=InvestorType.objects.all(),
        label='Investor Type',
        empty_label='Select Investor Type'
    )

    investor_stage = forms.ModelMultipleChoiceField(
        queryset=InvestmentStage.objects.all(),
        label='Investor Stage',
        widget=forms.CheckboxSelectMultiple
    )
