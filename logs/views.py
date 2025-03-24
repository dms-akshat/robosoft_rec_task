from django.shortcuts import render
from logs.models import Log
from collections import Counter

def dashboard(request):
    logs = Log.objects.all()
    total_logs = logs.count()
    success_count = logs.filter(status="success").count()
    failed_count = logs.filter(status="failure").count()
    
    # Calculate success rate
    success_rate = (success_count / total_logs * 100) if total_logs > 0 else 0
    
    # Status distribution
    status_counts = dict(Counter(logs.values_list("status", flat=True)))
    
    context = {
        "total_logs": total_logs,
        "success_count": success_count,
        "failed_count": failed_count,
        "success_rate": round(success_rate, 2),
        "status_counts": status_counts,
        "logs": logs.order_by("-created_at")[:5],  # Get the latest 5 logs
    }
    
    return render(request, "logs/dashboard.html", context)
