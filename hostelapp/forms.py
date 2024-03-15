# forms.py
from django import forms

from .models import Employee

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User  # Add this import
from django.core.exceptions import ValidationError  # Add this line
from django.utils.translation import gettext as _
from .models import Employee
from .models import LeaveApply
from .models import Complaints
from .models import Notice
from .models import Document
from .models import News_letter
from .models import Phone_Directory
from .models import Facility_Request
from .models import Scorecard
from .models import Refund_Request




class EmployeeRegistrationForm(UserCreationForm):
     # Remove 'password2' field
    password2 = None
    
    # Make 'lastname' not required
    lastname = forms.CharField(required=False)
    
  
    

    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'username', 'password1','phone','role','adhar_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize the labels and help text
        self.fields['firstname'].label = 'First Name'
        self.fields['lastname'].label = 'Last Name'
        self.fields['username'].label = 'Username'
        self.fields['password1'].label = 'Password'
        
        self.fields['phone'].label = 'phone'
        self.fields['role'].label = 'role'
        self.fields['adhar_image'].label = 'adhar_image'
        

        self.fields['firstname'].help_text = 'Enter your first name'
        self.fields['username'].help_text = 'Enter a unique username'
        self.fields['password1'].help_text = 'Enter a password with at least one uppercase letter'
       

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        # Check if at least one uppercase letter is present
        if not any(char.isupper() for char in password1):
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
                code='password_no_upper',
            )

        return password1


class EmployeeLoginForm(AuthenticationForm):
    
     class Meta:
        model = Employee
        fields = ['username', 'password']


class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = ('profile_image',)  





class LeaveApplyForm(forms.ModelForm):

    class Meta:
        model = LeaveApply
        fields = ['apply_by', 'fromdate', 'todate', 'reason']
        labels = {
            'apply_by': 'Apply By',
            'fromdate': 'From',
            'todate': 'To',
            'reason': 'Reason',
        }
        help_texts = {
            'apply_by' : 'please enter your mail id',
            'fromdate': 'Please enter From Date',
            'todate': 'Please enter To Date',
            'reason': 'Please enter Reason',
        }




class ComplaintApplyForm(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ['apply_by', 'complaint_type', 'sub_complaint_type', 'description','note','complaint_image','phone']
        labels = {
            'apply_by': 'Apply By',
            'complaint_type': 'complaint_type',
            'sub_complaint_type': 'sub_complaint_type',
            'description': 'description',
            'note': 'note',
            'complaint_image': 'complaint_image',
             'phone': 'phone',

        }
        help_texts = {
            'apply_by' : 'please enter your mail id',
            'complaint_type': 'Please enter From Date',
            'sub_complaint_type': 'Please enter To Date',
            'description': 'Please enter Reason',
            'note': 'Please enter Reason',
             'phone': 'Please enter phone',

        }



class NoticeApplyForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ['created_by', 'date', 'title', 'desc']
        labels = {
            'created_by': 'created_by ',
            'date': 'date',
            'title': 'title',
            'desc': 'description',
           

        }
        help_texts = {
            'apply_by' : 'please enter your mail id',
            'date': 'Please enter date',
            'title': 'Please enter title',
            'desc': 'Please enter desc',
        }
       


class DocumentApplyForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['created_by', 'document_name', 'Document_image']
        labels = {
            'created_by': 'created_by',
            'document_name': 'document_name',
            'Document_image': 'Document_image',
           

        }
        help_texts = {
            'created_by' : 'please enter your mail id',
            'document_name': 'Please enter document_name',
            'Document_image': 'Please enter Document_image',
           

        }
    


class NewsletterApplyForm(forms.ModelForm):

    class Meta:
        model = News_letter
        fields = ['created_by', 'date', 'title', 'desc']
        labels = {
            'created_by': 'created_by ',
            'date': 'date',
            'title': 'title',
            'desc': 'description',
           

        }
        help_texts = {
            'apply_by' : 'please enter your mail id',
            'date': 'Please enter date',
            'title': 'Please enter title',
            'desc': 'Please enter desc',
        }


class PhoneDirectoryForm(forms.ModelForm):

    class Meta:
        model = Phone_Directory
        fields = ['created_by', 'name', 'position', 'phone','email','photo']
        labels = {
            'created_by': 'created_by ',
            'name': 'name',
            'position': 'position',
            'phone': 'phone',
            'email': 'email',
            'photo': 'photo',

        }
        help_texts = {
            'created_by' : 'please enter your mail id',
            'name': 'Please enter date',
            'position': 'Please enter title',
            'phone': 'Please enter desc',
            'email': 'Please enter email',
        }


class FacilityApplyForm(forms.ModelForm):

    class Meta:
        model = Facility_Request
        fields = ['created_by', 'date', 'facility', 'desc']
        labels = {
            'created_by': 'created_by ',
            'date': 'date',
            'facility': 'facility',
            'desc': 'description',
           

        }
        help_texts = {
            'apply_by' : 'please enter your mail id',
            'date': 'Please enter date',
            'facility': 'Please enter facility',
            'desc': 'Please enter desc',
        }


class ScoreCardApplyForm(forms.ModelForm):

    class Meta:
        model = Scorecard
        fields = ['created_by', 'course_name', 'semister', 'remark','scorecard_image']
        labels = {
            'created_by': 'created_by ',
            'course_name': 'course_name',
            'semister': 'semister',
            'remark': 'remark',
            'scorecard_image': 'scorecard_image',
           

        }
        help_texts = {
            'created_by' : 'please enter your mail id',
            'course_name': 'Please enter course_name',
            'semister': 'Please enter semister',
            'remark': 'Please enter remark',
            'scorecard_image': 'Please enter scorecard_image',
        }


class RefundApplyForm(forms.ModelForm):

    class Meta:
        model = Refund_Request
        fields = ['created_by', 'date', 'desc' ]
        labels = {
            'created_by': 'created_by ',
            'date': 'date',
            'desc': 'desc',
            
           

        }
        help_texts = {
            'created_by' : 'please enter your mail id',
            'date': 'Please enter date',
            'desc': 'Please enter desc',
            
        }




