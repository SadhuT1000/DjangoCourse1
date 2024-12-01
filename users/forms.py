from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.forms import ModelForm
from django.urls import reverse_lazy

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1', 'password2')

class UserUpdateForm(StyleFormMixin, ModelForm):

    class Meta:
        model = User
        fields = '__all__'
        exclude =  ('token',)

        success_url = reverse_lazy("users:users")

class UserForgotPasswordForm(PasswordResetForm):
    """Форма запроса на восстановление пароля"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "autocomplete": "off"}
            )




class UserSetNewPasswordForm(SetPasswordForm):
    """Форма изменения пароля пользователя после подтверждения"""

    def __init__(self, *args, **kwargs):
        """Обновление стилей формы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "autocomplete": "off"}
            )

