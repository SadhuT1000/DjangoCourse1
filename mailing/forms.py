from django.forms import ModelForm, BooleanField
from .models import Mailing, Message, AttemptMailing, ReceiveMail
from django.core.exceptions import ValidationError



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'



class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"
        exclude = ("set_is_active", "owner")



class MessageForm(StyleFormMixin, ModelForm):

    class Meta:

        model = Message
        fields = "__all__"



class ReceiveMailForm(StyleFormMixin, ModelForm):

    class Meta:

        model = ReceiveMail
        fields = "__all__"
        exclude = ("can_blocking_client", "owner")

class ReceiveMailModeratorForm(StyleFormMixin, ModelForm):
    class Meta:

        model = ReceiveMail
        fields = "__all__"


class MailingModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"