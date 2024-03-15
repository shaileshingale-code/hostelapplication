# urls.py
from django.urls import path
from .views import  EmployeeRegistrationView
from .views import  EmployeeLoginView
from .views import user_profile
from .views import LeaveApplyFormView
from .views import LeaveApplyListView
from .views import approve_leave
from .views import approve_leave_parents
from .views import ReistrationListView
from .views import approve_student
from .views import employee_delete
from .views import ComplaintListView
from .views import reject_student
from .views import reject_leave_parent
from .views import user_dashboard
from .views import ComplaintApplyFormView
from .views import reject_leave_admin
from .views import EmployeeProfileUpdateView
from django.contrib.auth.views import LogoutView
from .views import custom_logout
from .views import complaint_delete
from .views import resolve_complaint
from .views import complaint_edit
from .views import NoticeApplyFormView
from .views import NoticeListView
from .views import Notice_delete
from .views import Notice_edit
from .views import UploadDocumentFormView
from .views import DocumentListView
from .views import Document_delete
from .views import Document_edit
from .views import NewsUploadFormView
from .views import NewsletterListView
from .views import Newsletter_Delete
from .views import Newsletter_Edit
from .views import Create_PhoneDirectoryView
from .views import PhoneDirectoryView
from .views import Phone_Delete
from .views import Phone_Edit
from .views import CreateHostelFacilityView
from .views import HostelFacilityRequestView
from .views import Request_Delete
from .views import Request_Edit
from .views import approve_facilityrequest
from .views import reject_facilityrequest
from .views import UploadScorecardView
from .views import ScoreCardListView
from .views import Scorecard_Delete
from .views import Scorecard_Edit
from .views import RefundRequestRaiseView
from .views import RefundRequestListView
from .views import Refund_Delete
from .views import Refund_Edit
from .views import approve_refundrequest
from .views import reject_refundrequest














urlpatterns = [
    path('', EmployeeLoginView.as_view(), name='employee_login' ),

    path('login/', EmployeeLoginView.as_view(), name='employee_login'),

    path('register/', EmployeeRegistrationView.as_view(), name='employee_register'),

    path('leaveapply/', LeaveApplyFormView.as_view(), name='leave_apply'),

    path('leaveapplylist/', LeaveApplyListView, name='leave_apply_list'),

    path('registrationlist/', ReistrationListView, name='registrations_list'),

    path('noticelist/', NoticeListView, name='notice_apply_list'),

    path('complaintlist/', ComplaintListView, name='complaint_list'),

    path('raisecomplaint/', ComplaintApplyFormView.as_view(), name='raise_complaint'),

    path('raisenotice/', NoticeApplyFormView.as_view(), name='raise_notice'),

    path('profile/', user_profile, name='user_profile'),

    path('dashboard/', user_dashboard, name='user_dashboard'),

    path('profile/update/<int:pk>/', EmployeeProfileUpdateView.as_view(), name='user_profile_update'),

    path('approveleave/', approve_leave, name='approve_leave'),

    path('approveleaveforparents/', approve_leave_parents, name='approve_leave_parents'),

    path('approvestudent/', approve_student, name='approve_student'),

    path('rejectstudent/', reject_student, name='reject_student'),

    path('rejectleaveforadmin/', reject_leave_admin, name='reject_leave_admin'),

    path('rejectleaveforparent/', reject_leave_parent, name='reject_leave_parent'),

    path('resolvecomplaint/', resolve_complaint, name='resolve_complaint'),

    path('employeedelete/<int:pk>/delete/', employee_delete, name='employee_delete'),

    path('complaintdelete/<int:pk>/delete/', complaint_delete, name='complaint_delete'),

    path('complaintedit/<int:pk>/delete/', complaint_edit, name='complaint_edit'),

    path('noticedelete/<int:pk>/delete/', Notice_delete, name='notice_delete'),

    path('noticeedit/<int:pk>/edit/', Notice_edit, name='notice_edit'),

    path('uploaddocument/', UploadDocumentFormView.as_view(), name='upload_document'),

    path('documentlist/', DocumentListView, name='document_list'),

    path('documentdelete/<int:pk>/delete/', Document_delete, name='document_delete'),

    path('documentedit/<int:pk>/edit/', Document_edit, name='document_edit'),

    path('uploadnews/', NewsUploadFormView.as_view(), name='upload_newsletter'),

    path('newsletterlist/', NewsletterListView, name='newsletter_list'),

    path('newsletterdelete/<int:pk>/delete/', Newsletter_Delete, name='newsletter_delete'),

    path('newsletteredit/<int:pk>/edit/', Newsletter_Edit, name='newsletter_edit'),

    path('createphonedirectory/', Create_PhoneDirectoryView.as_view(), name='create_phonedirectory'),

    path('phonedirectory/', PhoneDirectoryView, name='phone_directory'),

    path('phonedelete/<int:pk>/delete/', Phone_Delete, name='phone_delete'),

    path('phoneedit/<int:pk>/edit/', Phone_Edit, name='phone_edit'),

    path('hostelfacility/', CreateHostelFacilityView.as_view(), name='hostel_facility'),

    path('facilityrequest/', HostelFacilityRequestView, name='facility_request'),

    path('requestdelete/<int:pk>/delete/', Request_Delete, name='request_delete'),

    path('requestedit/<int:pk>/edit/', Request_Edit, name='request_edit'),

    path('approvefacility/', approve_facilityrequest, name='approve_facilityrequest'),

    path('rejectfacility/', reject_facilityrequest, name='reject_facilityrequest'),

    path('uploadscorecard/', UploadScorecardView.as_view(), name='upload_scorecard'),

    path('scorecardlist/', ScoreCardListView, name='scorecard_list'),

    path('scorecarddelete/<int:pk>/delete/', Scorecard_Delete, name='scorecard_delete'),

    path('scorecardedit/<int:pk>/edit/', Scorecard_Edit, name='scorecard_edit'),

    path('refundrequest/', RefundRequestRaiseView.as_view(), name='refund_request'),

    path('refundrequestlist/', RefundRequestListView, name='refund_request_list'),

    path('refunddelete/<int:pk>/delete/', Refund_Delete, name='refund_delete'),

    path('refundedit/<int:pk>/edit/', Refund_Edit, name='refund_edit'),

    path('approverefund/', approve_refundrequest, name='approve_refundrequest'),

    path('rejectrefund/', reject_refundrequest, name='reject_refundrequest'),









    path('logout/', custom_logout, name='logout'),
      
    # Add other URLs as needed
]

