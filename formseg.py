from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.formsets import BaseFormSet
from django.forms.fields import FileField
from django.forms.util import ValidationError

from django.shortcuts import render_to_response
from django.contrib.formtools.wizard import FormWizard

from ddtcms.office.equipment.models import Equipment,Characteristic,CharacteristicValue

class EquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment

class CharacteristicValueForm(forms.Form):
    def clean(self):
        a=self.fields
        s=self.data
        self.cleaned_data = {}
        # 下面的这一段for 是从 django的forms.py中的 full_clean 中复制来的
        for name, field in self.fields.items():
            # value_from_datadict() gets the data from the data dictionaries.
            # Each widget type knows how to retrieve its own data, because some
            # widgets split data over several HTML fields.
            value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
            try:
                if isinstance(field, FileField):
                    initial = self.initial.get(name, field.initial)
                    value = field.clean(value, initial)
                else:
                    value = field.clean(value)
                self.cleaned_data[name] = value
                if hasattr(self, 'clean_%s' % name):
                    value = getattr(self, 'clean_%s' % name)()
                    self.cleaned_data[name] = value
            except ValidationError, e:
                self._errors[name] = self.error_class(e.messages)
                if name in self.cleaned_data:
                    del self.cleaned_data[name]
        #cl=self.cleaned_data
        #debug()<<<调试用的,查看cl的值,主要是看self.cleaned_data的值,如果return了,就看不到了
        return self.cleaned_data

class EquipmentCreateWizard(FormWizard):
    def done(self, request, form_list):
        return render_to_response('equipment/done.html',
        {
        'form_data': [form.cleaned_data for form in form_list],
        })


    def get_form(self, step, data=None):
        "Helper method that returns the Form instance for the given step."
        form     = self.form_list[step](data, prefix=self.prefix_for_step(step), initial=self.initial.get(step, None))
        
        if step == 1:
            if data:
                cg       = data.get('0-category', 1)
                cs       = Characteristic.objects.all().filter(category__id=cg)
                for c in cs:
                    form.fields['Characteristic-'+str(c.id)] = forms.CharField(label = c.name)
                g=form.fields
                #debug()
        return form
        
    # 从wizard.py中复制过来进行更改的.    
    def render(self, form, request, step, context=None):
        "Renders the given Form object, returning an HttpResponse."
        old_data = request.POST
        prev_fields = []
        if old_data:
            hidden = forms.HiddenInput()
            # Collect all data from previous steps and render it as HTML hidden fields.
            for i in range(step):
                old_form = self.get_form(i, old_data)
                hash_name = 'hash_%s' % i
                prev_fields.extend([bf.as_hidden() for bf in old_form])
                prev_fields.append(hidden.render(hash_name, old_data.get(hash_name, self.security_hash(request, old_form))))
            if step == 1:
                cg       = old_data.get('0-category', 1)
                cs       = Characteristic.objects.all().filter(category__id=cg)
                for c in cs:
                    form.fields['Characteristic-'+str(c.id)] = forms.CharField(label = c.name)
                g=form.fields
                #debug()
            if step == 2:
                debug()
        return super(EquipmentCreateWizard, self).render(form, request, step, context=None)
        

    def get_template(self, step):
        return 'equipment/wizard_%s.html' % step



