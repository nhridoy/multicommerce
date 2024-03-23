from django.db.models import Sum
from django.utils.timezone import now

from .models import DailyData
from cart.models import Order
from datetime import timedelta
from celery import shared_task


@shared_task(bind=True)
def daily_job(self, *args, **kwargs):
    # Get the current date
    current_date = now().date()

    # Calculate yesterday's date
    yesterday_date = current_date - timedelta(days=1)

    total_revenue = Order.objects.filter(created_at__date=yesterday_date).aggregate(total_revenue=Sum('revenue'))[
        'total_revenue']

    daily_data, created = DailyData.objects.get_or_create(date=yesterday_date, revenue=total_revenue)

    print(daily_data, created)
    return "Done"
