from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django.utils.timezone import now
from datetime import timedelta

from .models import Record
from .serializers import RecordSerializer
from .permissions import IsAdminOrAnalyst
from .throttles import RecordThrottle, RecordWriteThrottle
from apps.common.pagination import CustomPagination


# ================= LIST + CREATE =================

class RecordListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrAnalyst]

    def get_throttles(self):
        if self.request.method == 'GET':
            return [RecordThrottle()]        
        return [RecordWriteThrottle()]        

    def get(self, request):
        records = Record.objects.filter(user=request.user).order_by('-created_at')

        # category
        category = request.GET.get('category')
        if category:
            records = records.filter(category__icontains=category)

        # type
        record_type = request.GET.get('type')
        if record_type:
            records = records.filter(type=record_type)

        # search
        search = request.GET.get('search')
        if search:
            records = records.filter(
                Q(category__icontains=search) |
                Q(note__icontains=search)
            )

        # date filters
        date_filter = request.GET.get('date_filter')
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
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if start_date and end_date:
            records = records.filter(date__range=[start_date, end_date])

        # PAGINATION
        paginator = CustomPagination()
        paginated_records = paginator.paginate_queryset(records, request)

        serializer = RecordSerializer(paginated_records, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = RecordSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "success": True,
                "message": "Record created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


# ================= UPDATE + DELETE =================

class RecordDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrAnalyst]

    throttle_classes = [RecordWriteThrottle]

    def put(self, request, pk):
        record = get_object_or_404(Record, id=pk, user=request.user)

        serializer = RecordSerializer(record, data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "success": True,
                "message": "Record updated successfully",
                "data": serializer.data
            })

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        record = get_object_or_404(Record, id=pk, user=request.user)
        record.delete()

        return Response({
            "success": True,
            "message": "Record deleted successfully"
        }, status=status.HTTP_200_OK)