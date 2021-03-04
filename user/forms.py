from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.widgets import PasswordInput

User = get_user_model()

class FormRegisterUser(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='يجب ان لا يحتوي على علامات فارغة او رموز خاصة ', label='اسم المستخدم')
    password1 = forms.CharField(min_length=8 , help_text='يجب ان يحتوي على حروف كبيرة وصغيرة وارقام',label='كملة المرور', widget=PasswordInput )
    password2 = forms.CharField(min_length=8, label=' تأكيد كلمة المرور ',  help_text='يجب ان يتطابق مع كلمة المرور الأولى', widget=PasswordInput)
    first_name = forms.CharField(max_length=150, required=False, label='الاسم الأول ')
    last_name = forms.CharField(max_length=150, required=False, label='الاسم الأخير')
    email = forms.EmailField(max_length=254, label='البريد الالكتروني ')

    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2', 'email', 'first_name', 'last_name'
        )