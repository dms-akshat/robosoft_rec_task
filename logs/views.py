from django.shortcuts import render
from django.core.paginator import Paginator
from logs.models import Log

def dashboard(request):
    # Get the total count of all SMS logs
    total_sms = Log.objects.count()

    # Get the count of each status type
    successful_deliveries = Log.objects.filter(status="success").count()
    failed_deliveries = Log.objects.filter(status="failure").count()
    pending_deliveries = Log.objects.filter(status="pending").count()

    # Calculate success rate (avoid division by zero)
    success_rate = (successful_deliveries / total_sms * 100) if total_sms > 0 else 0

    # Fetch logs with pagination (10 logs per page)
    logs_list = Log.objects.order_by("-created_at")
    paginator = Paginator(logs_list, 10)
    page_number = request.GET.get("page")
    logs_page = paginator.get_page(page_number)

    context = {
        "total_sms": total_sms,
        "successful_deliveries": successful_deliveries,
        "failed_deliveries": failed_deliveries,
        "pending_deliveries": pending_deliveries,
        "success_rate": round(success_rate, 1),
        "logs_page": logs_page,  # Paginated logs
    }

    return render(request, "logs/dashboard.html", context)
