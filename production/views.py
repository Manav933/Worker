from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
from django.core.paginator import Paginator
from .models import WorkerProduction
from .forms import WorkerProductionForm
from datetime import datetime, timedelta

def index(request):
    # Get latest records
    latest_records = WorkerProduction.objects.all().order_by('-date')[:10]
    
    # Get summary statistics
    today = datetime.now().date()
    month_start = today.replace(day=1)
    
    monthly_stats = WorkerProduction.objects.filter(
        date__gte=month_start
    ).aggregate(
        total_production=Sum('total_meter'),
        total_earnings=Sum('total_rate'),
        avg_daily_production=Avg('avg_meter_per_day')
    )
    
    context = {
        'latest_records': latest_records,
        'monthly_stats': monthly_stats,
    }
    return render(request, 'production/index.html', context)

@login_required
def record_list(request):
    records = WorkerProduction.objects.all().order_by('-date', 'name')
    paginator = Paginator(records, 25)  # Show 25 records per page
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'production/record_list.html', {'page_obj': page_obj})

@login_required
def record_create(request):
    if request.method == 'POST':
        form = WorkerProductionForm(request.POST)
        if form.is_valid():
            record = form.save()
            messages.success(request, 'Production record created successfully.')
            return redirect('production:record_detail', pk=record.pk)
    else:
        form = WorkerProductionForm()
    
    return render(request, 'production/record_form.html', {'form': form, 'title': 'Create Record'})

@login_required
def record_edit(request, pk):
    record = get_object_or_404(WorkerProduction, pk=pk)
    
    if request.method == 'POST':
        form = WorkerProductionForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save()
            messages.success(request, 'Production record updated successfully.')
            return redirect('production:record_detail', pk=record.pk)
    else:
        form = WorkerProductionForm(instance=record)
    
    return render(request, 'production/record_form.html', {
        'form': form,
        'title': 'Edit Record',
        'record': record
    })

@login_required
def record_detail(request, pk):
    record = get_object_or_404(WorkerProduction, pk=pk)
    daily_meters = [
        (f'Day {i}', getattr(record, f'day_{i}_meter'))
        for i in range(1, 16)
    ]
    
    context = {
        'record': record,
        'daily_meters': daily_meters,
    }
    return render(request, 'production/record_detail.html', context)

@login_required
def worker_summary(request):
    # Get unique worker names
    workers = WorkerProduction.objects.values_list('name', flat=True).distinct()
    selected_worker = request.GET.get('worker')
    
    if selected_worker:
        today = datetime.now().date()
        month_start = today.replace(day=1)
        
        # Get monthly statistics for selected worker
        monthly_stats = WorkerProduction.objects.filter(
            name=selected_worker,
            date__gte=month_start
        ).aggregate(
            total_production=Sum('total_meter'),
            total_earnings=Sum('total_rate'),
            avg_daily_production=Avg('avg_meter_per_day')
        )
        
        # Get recent records for selected worker
        recent_records = WorkerProduction.objects.filter(
            name=selected_worker
        ).order_by('-date')[:15]
    else:
        monthly_stats = None
        recent_records = None
    
    context = {
        'workers': workers,
        'selected_worker': selected_worker,
        'monthly_stats': monthly_stats,
        'recent_records': recent_records,
    }
    return render(request, 'production/worker_summary.html', context)

@login_required
def machine_summary(request):
    # Get unique machine numbers
    machines = WorkerProduction.objects.values_list('machine_no', flat=True).distinct()
    selected_machine = request.GET.get('machine')
    
    if selected_machine:
        today = datetime.now().date()
        month_start = today.replace(day=1)
        
        # Get monthly statistics for selected machine
        monthly_stats = WorkerProduction.objects.filter(
            machine_no=selected_machine,
            date__gte=month_start
        ).aggregate(
            total_production=Sum('total_meter'),
            avg_daily_production=Avg('avg_meter_per_day')
        )
        
        # Get recent records for selected machine
        recent_records = WorkerProduction.objects.filter(
            machine_no=selected_machine
        ).order_by('-date')[:15]
    else:
        monthly_stats = None
        recent_records = None
    
    context = {
        'machines': machines,
        'selected_machine': selected_machine,
        'monthly_stats': monthly_stats,
        'recent_records': recent_records,
    }
    return render(request, 'production/machine_summary.html', context)
