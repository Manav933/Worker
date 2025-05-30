from django import forms
from .models import WorkerProduction

class WorkerProductionForm(forms.ModelForm):
    class Meta:
        model = WorkerProduction
        fields = [
            'name', 'machine_no', 'date', 'rate_per_meter',
            'day_1_meter', 'day_2_meter', 'day_3_meter', 'day_4_meter',
            'day_5_meter', 'day_6_meter', 'day_7_meter', 'day_8_meter',
            'day_9_meter', 'day_10_meter', 'day_11_meter', 'day_12_meter',
            'day_13_meter', 'day_14_meter', 'day_15_meter'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'machine_no': forms.Select(attrs={'class': 'form-control'}),
            'rate_per_meter': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add form-control class to all meter input fields
        for i in range(1, 16):
            field_name = f'day_{i}_meter'
            self.fields[field_name].widget.attrs['class'] = 'form-control'
            self.fields[field_name].widget.attrs['step'] = '0.01' 