from django.contrib.auth.forms import UsernameField, AuthenticationForm,BaseUserCreationForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django import forms
from .models import MyUser

class MyUserCreationForm(BaseUserCreationForm):
    error_messages = {
        "password_mismatch": _("Hai mật khẩu nhập không khớp nhau."),
    }

    password1 = forms.CharField(
        label=_("Mật khẩu"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Xác nhận mật khẩu"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = MyUser
        fields = ('email', 'is_superuser','username', 'first_name', 'last_name','birthdate', 'gender' )

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Địa chỉ Email"),
        max_length=100,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

class MyPasswordResetConfirmForm(SetPasswordForm):
    error_messages = {
        "password_mismatch": _("Hai mật khẩu nhập không khớp nhau."),
    }
    new_password1 = forms.CharField(
        label=_("Mật khẩu mới"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Xác nhận mật khẩu mới"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

class MyLoginForm(AuthenticationForm):

    username = UsernameField(label= _("Tài khoản"), widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Mật khẩu"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    error_messages = {
        "invalid_login": _(
            "Làm ơn nhập đúng %(username)s và mật khẩu. Lưu ý "
            "hoa thường."
        ),
        "inactive": _("Tài khoản này không được active."),
    }