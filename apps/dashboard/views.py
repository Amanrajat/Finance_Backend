from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from django.db.models import Sum, Q
from django.db.models.functions import TruncMonth
from django.utils.timezone import now
from datetime import timedelta

from apps.records.models import Record
from apps.records.serializers import RecordSerializer
from .throttles import DashboardThrottle
from apps.dashboard.models import Summary


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [DashboardThrottle]  

    def get(self, request):
        try:
            user = request.user

            # BASE QUERY 
            records = Record.objects.filter(user=user)

            # DATE FILTER 
            date_filter = request.GET.get('date_filter')
            start_date = request.GET.get('start_date')
            end_date = request.GET.get('end_date')

            today = now().date()

            if date_filter == 'today':
                records = records.filter(date=today)

            elif date_filter == 'yesterday':
                records = records.filter(date=today - timedelta(days=1))

            elif date_filter == 'this_week':
                start_week = today - timedelta(days=today.weekday())
                records = records.filter(date__gte=start_week)

            elif date_filter == 'this_month':
                records = records.filter(date__year=today.year, date__month=today.month)

            elif date_filter == 'this_year':
                records = records.filter(date__year=today.year)

            # custom range
            if start_date and end_date:
                records = records.filter(date__range=[start_date, end_date])

            # SUMMARY 
            income = records.filter(type__iexact='income').aggregate(total=Sum('amount'))['total'] or 0
            expense = records.filter(type__iexact='expense').aggregate(total=Sum('amount'))['total'] or 0
            balance = income - expense

            # SAVE DATA INTO SUMMARY TABLE
            Summary.objects.update_or_create(
                user=user,
                defaults={
                    "total_income": income,
                    "total_expense": expense,
                    "balance": balance
                }
)

            # CATEGORY BREAKDOWN 
            category_data = list(
                records.values('category')
                .annotate(total=Sum('amount'))
                .order_by('-total')
            )

            # MONTHLY TREND 
            monthly_data = list(
                records.annotate(month=TruncMonth('date'))
                .values('month')
                .annotate(
                    income=Sum('amount', filter=Q(type='income')),
                    expense=Sum('amount', filter=Q(type='expense'))
                )
                .order_by('month')
            )

            # TOP CATEGORIES 
            top_categories = category_data[:5]

            # RECENT 
            recent_records = records.order_by('-created_at')[:5]
            recent = RecordSerializer(recent_records, many=True).data

            # RESPONSE 
            return Response({
                "success": True,

                "summary": {
                    "total_income": income,
                    "total_expense": expense,
                    "balance": balance
                },

                "category_breakdown": category_data,
                "monthly_trend": monthly_data,
                "top_categories": top_categories,
                "recent": recent

            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "success": False,
                "message": "Something went wrong",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)