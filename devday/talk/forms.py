from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Layout, Field, Submit, Hidden
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django_file_form.forms import FileFormMixin, UploadedFileField
from registration.forms import RegistrationFormUniqueEmail

from devday.utils.forms import CombinedFormBase
from talk.models import Talk, Speaker

User = get_user_model()


class TalkForm(forms.models.ModelForm):
    class Meta:
        model = Talk
        fields = ["title", "abstract", "remarks"]
        widgets = {
            'abstract': forms.Textarea(attrs={'rows': 3}),
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }


class SpeakerForm(FileFormMixin, forms.models.ModelForm):
    firstname = forms.fields.CharField(label=_("Firstname"), max_length=64)
    lastname = forms.fields.CharField(label=_("Lastname"), max_length=64)
    uploaded_image = UploadedFileField(label=_("Speaker portrait"))

    class Meta:
        model = Speaker
        fields = ["shortbio", "videopermission", "shirt_size"]
        widgets = {
            'shortbio': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(SpeakerForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        speaker = self.instance
        speaker.portrait = self.cleaned_data['uploaded_image']
        result = super(SpeakerForm, self).save(commit)
        if commit:
            self.delete_temporary_files()
        return result


class ExistingFileForm(SpeakerForm):
    def get_upload_url(self):
        return reverse('talk_handle_upload')


class DevDayRegistrationForm(RegistrationFormUniqueEmail):
    class Meta(RegistrationFormUniqueEmail.Meta):
        fields = [
            'email',
            'password1',
            'password2'
        ]

    def clean(self):
        if self.cleaned_data.get('email'):
            self.cleaned_data[User.USERNAME_FIELD] = self.cleaned_data.get('email')
        return super(RegistrationFormUniqueEmail, self).clean()


class CreateTalkForm(TalkForm):
    def __init__(self, *args, **kwargs):
        self.speaker = kwargs.pop('speaker')
        super(CreateTalkForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'create_session'
        self.helper.form_id = 'create-talk-form'
        self.helper.field_template = 'talk/form/field.html'
        self.helper.html5_required = True

        self.helper.layout = Layout(
            Div(
                Field("title", template='talk/form/field.html', autofocus='autofocus'),
                "abstract",
                "remarks",
                css_class="col-md-12 col-lg-offset-3 col-lg-6"
            ),
            Div(
                Submit('submit', _('Submit'), css_class="btn-default"),
                css_class="col-md-12 col-lg-offset-3 col-lg-6"
            )
        )

    def save(self, commit=True):
        self.instance.speaker = self.speaker
        return super(CreateTalkForm, self).save(commit=commit)


class TalkAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(TalkAuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'submit_session'
        self.helper.form_method = 'post'
        self.helper.field_template = 'talk/form/field.html'
        self.helper.html5_required = True
        self.helper.layout = Layout(
            Div(
                Hidden('next', value=reverse('submit_session')),
                Field('username', template='talk/form/field.html', autofocus='autofocus'),
                Field('password', template='talk/form/field.html'),
            ),
            Div(
                Submit('submit', _('Login'), css_class='btn-default'),
                css_class='text-center'
            )
        )


class BecomeSpeakerForm(SpeakerForm):
    def __init__(self, *args, **kwargs):
        super(BecomeSpeakerForm, self).__init__(*args, **kwargs)
        self.helper.form_action = 'create_speaker'
        self.helper.form_method = 'post'
        self.helper.form_id = 'create-speaker-form'
        self.helper.field_template = 'talk/form/field.html'
        self.helper.html5_required = True

        self.helper.layout = Layout(
            "upload_url",
            "delete_url",
            "form_id",
            Div(
                "firstname",
                "lastname",
            ),
            Div(
                "shirt_size",
                Field("videopermission", template="talk/form/videopermission-field.html"),
                Field("uploaded_image", template="talk/form/speakerportrait-field.html"),
                Field("shortbio", rows=2),
            ),
            Div(
                Submit('submit', _('Register as speaker'))
            )
        )


class CreateSpeakerForm(CombinedFormBase):
    form_classes = [DevDayRegistrationForm, SpeakerForm]

    def __init__(self, *args, **kwargs):
        super(CreateSpeakerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'create_speaker'
        self.helper.form_method = 'post'
        self.helper.form_id = 'create-speaker-form'
        self.helper.field_template = 'talk/form/field.html'
        self.helper.html5_required = True
        self.fields['email'].help_text = None
        self.fields['email'].label = _('E-Mail')
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.helper.layout = Layout(
            'upload_url',
            'delete_url',
            'form_id',
            Div(
                Field('email', template='talk/form/field.html', autofocus='autofocus'),
                'firstname',
                'lastname',
                'password1',
                'password2',
                css_class='col-md-12 col-lg-offset-2 col-lg-4'
            ),
            Div(
                Field('uploaded_image', template='talk/form/speakerportrait-field.html'),
                'shirt_size',
                Field('shortbio', rows=2, template='talk/form/field.html'),
                Field('videopermission', template='talk/form/videopermission-field.html'),
                css_class='col-md-12 col-lg-4'
            ),
            Div(
                Submit('submit', _('Register as speaker')),
                css_class='col-md-12 col-lg-offset-2 col-lg-8 text-center'
            )
        )