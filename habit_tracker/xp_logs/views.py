from django.shortcuts import render
from .models import XpLog

# Create your views here.


def xp_log_list(request):
    xp_logs = XpLog.objects.all()
    return render(request, 'xp_logs/xplog_list.html', {'xp_logs': xp_logs})
