from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from config import settings
from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject
from main.services import get_cached_subject_for_student


@login_required
# @permission_required('main.view_student')
def index(request):
    student_list = Student.objects.all()
    context = {
        'object_list': student_list,
        'title': 'Главная',
    }
    return render(request, 'main/student_list.html', context)


@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'Name: {name}\nEmail: {email}\nMessage: {message}')

    context = {
        'title': 'Контакты',
    }

    return render(request, 'main/contact.html', context)


class StudentListView(LoginRequiredMixin, ListView):
    model = Student


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    permission_required = 'main.view_student'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['subjects'] = get_cached_subject_for_student(self.object.pk)

        return context_data


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    permission_required = 'main.add_student'
    # fields = ('first_name', 'last_name', 'avatar')
    # success_url = reverse_lazy('main:index')
    form_class = StudentForm
    success_url = reverse_lazy('main:index')


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    permission_required = 'main.change_student'

    # fields = ('first_name', 'last_name', 'avatar')
    form_class = StudentForm
    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1, can_delete=True)

        if self.request.method == "POST":
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        if form.is_valid() and formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    permission_required = 'main.delete_student'

    def test_func(self):
        return self.request.user.is_superuser


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)

    student_item.is_active = not student_item.is_active
    student_item.save()

    return redirect(reverse('main:index'))
