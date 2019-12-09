from app01 import models
from django import forms
from django.forms import widgets as wid
from multiselectfield.forms.fields import MultiSelectFormField


class BSModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            if isinstance(filed, (MultiSelectFormField, forms.BooleanField)):
                continue
            filed.widget.attrs['class'] = 'form-control'


class QingJiaForm(BSModelForm):
    class Meta:
        model = models.Application
        fields = "__all__"

        exclude = ["case"]  # 排除的字段

        widgets = {
            "start_time": wid.TimeInput(attrs={"type": "date"}),  # 自定义属性
            "end_time": wid.TimeInput(attrs={"type": "date"})
        }
