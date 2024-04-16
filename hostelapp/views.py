# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import Employee
from .models import LeaveApply
from .models import Complaints
from .models import Notice
from .models import Document
from .models import Phone_Directory
from .models import News_letter
from .models import Facility_Request
from .models import Scorecard
from .models import Refund_Request
from .models import Fine_List
from .models import About_Hostel
from .models import Contact_us
from .models import Instructions
from .models import Attendance
from .forms import EmployeeRegistrationForm
from .forms import EmployeeLoginForm
from .forms import EmployeeChangeForm
from .forms import LeaveApplyForm
from .forms import ComplaintApplyForm
from .forms import NoticeApplyForm
from .forms import DocumentApplyForm
from .forms import NewsletterApplyForm
from .forms import PhoneDirectoryForm
from .forms import FacilityApplyForm
from .forms import ScoreCardApplyForm
from .forms import RefundApplyForm
from .forms import FineApplyForm
from .forms import AbouthostelForm
from .forms import ContactusForm
from .forms import InstructionsForm
from .forms import AttendanceForm
from django.views.generic.edit import UpdateView
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.contrib import messages
from django.utils.decorators import method_decorator













# class EmployeeRegistrationView(CreateView):
#     model = Employee
#     form_class = EmployeeRegistrationForm
#     template_name = 'employeeapp/registration.html'  
#     success_url = reverse_lazy('employee_login') 





class EmployeeRegistrationView(CreateView):
    model = Employee
    form_class = EmployeeRegistrationForm
    template_name = 'employeeapp/registration.html'
    success_url = reverse_lazy('employee_login')

    def form_valid(self, form):
        
        response = super().form_valid(form)
       
        messages.success(self.request, 'Registration successful!')

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the form was successfully submitted
        if self.request.method == 'POST' and self.object:
            context['registration_successful'] = True
        return context




@method_decorator([login_required, never_cache], name='dispatch')
class LeaveApplyFormView(CreateView):
    model = LeaveApply
    form_class = LeaveApplyForm
    template_name = 'employeeapp/applyleave.html'
    success_url = reverse_lazy('leave_apply_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page'))


@method_decorator([login_required, never_cache], name='dispatch')
class ComplaintApplyFormView(CreateView):
    model = Complaints
    form_class = ComplaintApplyForm
    template_name = 'employeeapp/raisecomplaint.html'
    success_url = reverse_lazy('complaint_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page'))            





@csrf_exempt
def approve_leave(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(LeaveApply, id=leave_id)
        leave_instance.approved_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'Leave approved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)





@csrf_exempt
def approve_leave_parents(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(LeaveApply, id=leave_id)
        leave_instance.approved_status_parents = 1
        leave_instance.save()
        return JsonResponse({'message': 'Leave approved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)





@csrf_exempt
def approve_student(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Employee, id=leave_id)
        leave_instance.approved_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'approved successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def reject_student(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Employee, id=leave_id)
        leave_instance.approved_status = 0
        leave_instance.save()
        return JsonResponse({'message': ' Request rejected'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)        

@csrf_exempt
def reject_leave_admin(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(LeaveApply, id=leave_id)
        leave_instance.approved_status = 2
        leave_instance.save()
        return JsonResponse({'message': 'Leave Rejected'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)





@csrf_exempt
def reject_leave_parent(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(LeaveApply, id=leave_id)
        leave_instance.approved_status_parents = 2
        leave_instance.save()
        return JsonResponse({'message': 'Leave Rejected'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
def resolve_complaint(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Complaints, id=leave_id)
        leave_instance.resolve_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'Complaint Resolved'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)





def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('registrations_list')



def complaint_delete(request, pk):
    complaint = get_object_or_404(Complaints, pk=pk)
    complaint.delete()
    return redirect('complaint_list')


def Notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    notice.delete()
    return redirect('notice_apply_list')    


# def complaint_edit(request, pk):
#     complaint = get_object_or_404(Complaints, pk=pk)
#     if request.method == "POST":
#         form = ComplaintApplyForm(request.POST, instance=complaint)
#         if form.is_valid():
#             complaint = form.save(commit=False)
#             complaint.save()
#             return redirect('complaint_list')
           
#     else:
#         form = ComplaintApplyForm(instance=complaint)
#     return render(request, 'employeeapp/raisecomplaint.html', {'form': form})
@never_cache
@login_required 
def complaint_edit(request, pk):
    complaint = get_object_or_404(Complaints, pk=pk)
    if request.method == "POST":
        form = ComplaintApplyForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            new_complaint = form.save(commit=False)
            # Check if the complaint image has changed
            if 'complaint_image' in request.FILES:
                new_complaint.complaint_image.save(request.FILES['complaint_image'].name, request.FILES['complaint_image'], save=False)
            new_complaint.save()
            return redirect('complaint_list')
    else:
        form = ComplaintApplyForm(instance=complaint)
    return render(request, 'employeeapp/raisecomplaint.html', {'form': form})

@never_cache
@login_required 
def Notice_edit(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        form = NoticeApplyForm(request.POST, instance=notice)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.save()
            return redirect('notice_apply_list')
           
    else:
        form = NoticeApplyForm(instance=notice)
    return render(request, 'employeeapp/raisenotice.html', {'form': form})


@method_decorator([login_required, never_cache], name='dispatch')
class NoticeApplyFormView(CreateView):
    model = Notice
    form_class = NoticeApplyForm
    template_name = 'employeeapp/raisenotice.html'
    success_url = reverse_lazy('notice_apply_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page')) 


@method_decorator([login_required, never_cache], name='dispatch')
class UploadDocumentFormView(CreateView):
    model = Document
    form_class = DocumentApplyForm
    template_name = 'employeeapp/uploaddocument.html'
    success_url = reverse_lazy('document_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page')) 



class EmployeeLoginView(LoginView):
   
    form_class = EmployeeLoginForm
    template_name = 'employeeapp/login.html'  
    authentication_form = EmployeeLoginForm

@never_cache
@login_required    
def user_profile(request):
    employee = request.user
    if employee.approved_status == 1:
        return render(request, 'employeeapp/user_profile.html')
    else:
        messages.warning(request, "Please wait for approval from the admin.")
        return redirect('employee_login')



def custom_logout(request):
   
    logout(request)

    
    return redirect('employee_login')



class EmployeeProfileUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeChangeForm
    template_name = 'employeeapp/employee_profile_update.html'
    success_url = reverse_lazy('user_profile')


@never_cache
@login_required 
def LeaveApplyListView(request):
    leaves = LeaveApply.objects.all()
    return render(request, 'employeeapp/leave_list.html', {'leaves': leaves})

@never_cache
@login_required 
def ComplaintListView(request):
    complaints = Complaints.objects.all()
    return render(request, 'employeeapp/complaint_list.html', {'complaints': complaints})

@never_cache
@login_required 
def ComplaintListView(request):
    complaints = Complaints.objects.all()
    return render(request, 'employeeapp/complaint_list.html', {'complaints': complaints})


@never_cache
@login_required 
def user_dashboard(request):
    leaves = LeaveApply.objects.all()
    return render(request, 'employeeapp/user_profile.html', {'leaves': leaves})



    


@never_cache
@login_required 
def ReistrationListView(request):
    employees = Employee.objects.all()
    return render(request, 'employeeapp/registration_list.html', {'employees': employees})


@never_cache
@login_required 
def NoticeListView(request):
    notices = Notice.objects.all()
    return render(request, 'employeeapp/notice_list.html', {'notices': notices})  

@never_cache
@login_required 
def DocumentListView(request):
    documents = Document.objects.all()
    return render(request, 'employeeapp/document_list.html', {'documents': documents})    




def Document_delete(request, pk):
    document = get_object_or_404(Document, pk=pk)
    document.delete()
    return redirect('document_list')    


# def Document_edit(request, pk):
#     document = get_object_or_404(Document, pk=pk)
#     if request.method == "POST":
#         form = DocumentApplyForm(request.POST, instance=document)
#         if form.is_valid():
#             document = form.save(commit=False)
#             document.save()
#             return redirect('document_list')
           
#     else:
#         form = DocumentApplyForm(instance=document)
#     return render(request, 'employeeapp/uploaddocument.html', {'form': form})


@never_cache
@login_required 
def Document_edit(request, pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        form = DocumentApplyForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            new_document = form.save(commit=False)
           
            if 'Document_image' in request.FILES:
                new_document.Document_image.save(request.FILES['Document_image'].name, request.FILES['Document_image'], save=False)
            new_document.save()
            return redirect('document_list')
           
    else:
        form = DocumentApplyForm(instance=document)
    return render(request, 'employeeapp/uploaddocument.html', {'form': form})



@method_decorator([login_required, never_cache], name='dispatch')
class NewsUploadFormView(CreateView):
    model = News_letter
    form_class = NewsletterApplyForm
    template_name = 'employeeapp/raisenewsletter.html'
    success_url = reverse_lazy('newsletter_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page'))

@never_cache
@login_required 
def NewsletterListView(request):
    newsletters = News_letter.objects.all()
    return render(request, 'employeeapp/Newsletter_list.html', {'newsletters': newsletters})





def Newsletter_Delete(request, pk):
    newsletter = get_object_or_404(News_letter, pk=pk)
    newsletter.delete()
    return redirect('newsletter_list')    


def Newsletter_Edit(request, pk):
    newsletter = get_object_or_404(News_letter, pk=pk)
    if request.method == "POST":
        form = NewsletterApplyForm(request.POST, instance=newsletter)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.save()
            return redirect('newsletter_list')
           
    else:
        form = NewsletterApplyForm(instance=newsletter)
    return render(request, 'employeeapp/raisenewsletter.html', {'form': form})

@method_decorator([login_required, never_cache], name='dispatch')
class Create_PhoneDirectoryView(CreateView):
    model = Phone_Directory
    form_class = PhoneDirectoryForm
    template_name = 'employeeapp/createphonedirectory.html'
    success_url = reverse_lazy('phone_directory')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception as e:
           
            print("An error occurred while saving form data:", e)
          
            return HttpResponseRedirect(reverse_lazy('error_page'))    


@never_cache
@login_required 
def PhoneDirectoryView(request):
    phones = Phone_Directory.objects.all()
    return render(request, 'employeeapp/Phonedirectory_list.html', {'phones': phones})




def Phone_Delete(request, pk):
    phone = get_object_or_404(Phone_Directory, pk=pk)
    phone.delete()
    return redirect('phone_directory')    


@never_cache
@login_required 
def Phone_Edit(request, pk):
    phone = get_object_or_404(Phone_Directory, pk=pk)
    if request.method == "POST":
        form = PhoneDirectoryForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            new_phone = form.save(commit=False)
            
            if 'photo' in request.FILES:
                new_phone.photo.save(request.FILES['photo'].name, request.FILES['photo'], save=False)
            new_phone.save()
            return redirect('phone_directory')
    else:
        form = PhoneDirectoryForm(instance=phone)
    return render(request, 'employeeapp/createphonedirectory.html', {'form': form})


@method_decorator([login_required, never_cache], name='dispatch')
class CreateHostelFacilityView(CreateView):
    model = Facility_Request
    form_class = FacilityApplyForm
    template_name = 'employeeapp/createhostelfacility.html'
    success_url = reverse_lazy('facility_request')


  
@never_cache
@login_required 
def HostelFacilityRequestView(request):
    requests = Facility_Request.objects.all()
    return render(request, 'employeeapp/hostelfacilityrequest_list.html', {'requests': requests})

@never_cache
@login_required 
def Request_Edit(request, pk):
    facility = get_object_or_404(Facility_Request, pk=pk)
    if request.method == "POST":
        form = FacilityApplyForm(request.POST, instance=facility)
        if form.is_valid():
            facility = form.save(commit=False)
            facility.save()
            return redirect('facility_request')
           
    else:
        form = FacilityApplyForm(instance=facility)
    return render(request, 'employeeapp/createhostelfacility.html', {'form': form})


def Request_Delete(request, pk):
    facility = get_object_or_404(Facility_Request, pk=pk)
    facility.delete()
    return redirect('facility_request')       



@csrf_exempt
def approve_facilityrequest(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Facility_Request, id=leave_id)
        leave_instance.approved_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'facility Request Accepted'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def reject_facilityrequest(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Facility_Request, id=leave_id)
        leave_instance.approved_status = 2
        leave_instance.save()
        return JsonResponse({'message': 'facility Request Rejected'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)     


@method_decorator([login_required, never_cache], name='dispatch')
class UploadScorecardView(CreateView):
    model = Scorecard
    form_class = ScoreCardApplyForm
    template_name = 'employeeapp/uploadscorecardform.html'
    success_url = reverse_lazy('scorecard_list')           

@never_cache
@login_required 
def ScoreCardListView(request):
    scorecards = Scorecard.objects.all()
    return render(request, 'employeeapp/scorecard_list.html', {'scorecards': scorecards})


def Scorecard_Delete(request, pk):
    scorecard = get_object_or_404(Scorecard, pk=pk)
    scorecard.delete()
    return redirect('scorecard_list')    


@never_cache
@login_required 
def Scorecard_Edit(request, pk):
    scorecard = get_object_or_404(Scorecard, pk=pk)
    if request.method == "POST":
        form = ScoreCardApplyForm(request.POST, request.FILES, instance=scorecard)
        if form.is_valid():
            new_scorecard = form.save(commit=False)
            
            if 'scorecard_image' in request.FILES:
                new_scorecard.scorecard_image.save(request.FILES['scorecard_image'].name, request.FILES['scorecard_image'], save=False)
            new_scorecard.save()
            return redirect('scorecard_list')
    else:
        form = ScoreCardApplyForm(instance=scorecard)
    return render(request, 'employeeapp/uploadscorecardform.html', {'form': form})


@method_decorator([login_required, never_cache], name='dispatch')
class RefundRequestRaiseView(CreateView):
    model = Refund_Request
    form_class = RefundApplyForm
    template_name = 'employeeapp/refundrequestform.html'
    success_url = reverse_lazy('refund_request_list')         

@never_cache
@login_required 
def RefundRequestListView(request):
    refunds = Refund_Request.objects.all()
    return render(request, 'employeeapp/refundrequest_list.html', {'refunds': refunds})




def Refund_Delete(request, pk):
    refund = get_object_or_404(Refund_Request, pk=pk)
    refund.delete()
    return redirect('refund_request_list')

@never_cache
@login_required 
def Refund_Edit(request, pk):
    refund = get_object_or_404(Refund_Request, pk=pk)
    if request.method == "POST":
        form = RefundApplyForm(request.POST, instance=refund)
        if form.is_valid():
            refund = form.save(commit=False)
            refund.save()
            return redirect('refund_request_list')
           
    else:
        form = RefundApplyForm(instance=refund)
    return render(request, 'employeeapp/refundrequestform.html', {'form': form})



@csrf_exempt
def approve_refundrequest(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Refund_Request, id=leave_id)
        leave_instance.approved_status = 1
        leave_instance.save()
        return JsonResponse({'message': 'Refund Request Accepted'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def reject_refundrequest(request):
    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        leave_instance = get_object_or_404(Refund_Request, id=leave_id)
        leave_instance.approved_status = 2
        leave_instance.save()
        return JsonResponse({'message': 'refund Request Rejected'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)      

@method_decorator([login_required, never_cache], name='dispatch')
class FineUploadView(CreateView):
    model = Fine_List
    form_class = FineApplyForm
    template_name = 'employeeapp/fineappform.html'
    success_url = reverse_lazy('FineListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Employee.objects.all()
        return context


@never_cache
@login_required 
def FineListView(request):
    fines = Fine_List.objects.all()
    return render(request, 'employeeapp/fine_list.html', {'fines': fines})    




def fine_delete(request, pk):
    fine = get_object_or_404(Fine_List, pk=pk)
    fine.delete()
    return redirect('FineListView')

@never_cache
@login_required 
def fine_Edit(request, pk):
    fine = get_object_or_404(Fine_List, pk=pk)
    if request.method == "POST":
        form = FineApplyForm(request.POST, instance=fine)
        if form.is_valid():
            fine = form.save(commit=False)
            fine.save()
            return redirect('FineListView')
           
    else:
        form = FineApplyForm(instance=fine)
    
    
    students = Employee.objects.all()
    
    return render(request, 'employeeapp/fineappform.html', {'form': form, 'students': students})


@never_cache
@login_required 
def AboutHostelView(request):
    about = get_object_or_404(About_Hostel, pk='1')
    if request.method == "POST":
        form = AbouthostelForm(request.POST, instance=about)
        if form.is_valid():
            about = form.save(commit=False)
            about.save()
            return redirect('about_hostel')
           
    else:
        form = AbouthostelForm(instance=about)
    
    students = Employee.objects.all()
    
    return render(request, 'employeeapp/aboutus.html', {'form': form, 'students': students})






@never_cache
@login_required 
def ContactusView(request):
    about = get_object_or_404(Contact_us, pk='1')
    if request.method == "POST":
        form = ContactusForm(request.POST, instance=about)
        if form.is_valid():
            about = form.save(commit=False)
            about.save()
            return redirect('contact_us')
           
    else:
        form = ContactusForm(instance=about)
    
    students = Employee.objects.all()
    
    return render(request, 'employeeapp/contactus.html', {'form': form, 'students': students})










@never_cache
@login_required 
def InstructionsView(request):
    about = get_object_or_404(Instructions, pk='1')
    if request.method == "POST":
        form = InstructionsForm(request.POST, instance=about)
        if form.is_valid():
            about = form.save(commit=False)
            about.save()
            return redirect('instructions')
           
    else:
        form = InstructionsForm(instance=about)
    
    students = Employee.objects.all()
    
    return render(request, 'employeeapp/instructions.html', {'form': form, 'students': students})        


@method_decorator([login_required, never_cache], name='dispatch')
class AttendanceView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = 'employeeapp/attendanceform.html'
    success_url = reverse_lazy('attendance')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Employee.objects.all()
        return context
@never_cache
@login_required 
def AttendanceListView(request):
    fines = Attendance.objects.all()
    return render(request, 'employeeapp/attendance_list.html', {'fines': fines})    





def Attendance_delete(request, pk):
    fine = get_object_or_404(Attendance, pk=pk)
    fine.delete()
    return redirect('AttendanceListView')

@never_cache
@login_required 
def Attendance_Edit(request, pk):
    fine = get_object_or_404(Attendance, pk=pk)
    if request.method == "POST":
        form = AttendanceForm(request.POST, instance=fine)
        if form.is_valid():
            fine = form.save(commit=False)
            fine.save()
            return redirect('AttendanceListView')
           
    else:
        form = AttendanceForm(instance=fine)
    
    
    students = Employee.objects.all()
    
    return render(request, 'employeeapp/attendanceform.html', {'form': form, 'students': students})    