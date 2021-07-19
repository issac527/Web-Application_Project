from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # username 필드를 사용할 수 없도록 맹금
        self.fields['username'].disabled = True


        