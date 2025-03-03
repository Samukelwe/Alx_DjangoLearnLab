from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request):
    