import random
from datetime import datetime
from .models import FlowData

def generate_flow_data():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Get the current date, time and day
    now = datetime.now()
    current_date = now.date()
    current_time = now.time()
    current_day = weekdays[now.weekday()]
    
    # Generate random daily flow between 10 and 100
    daily_flow = random.randint(10, 100)
    
    # Get the latest record to calculate total flow
    latest_record = FlowData.objects.order_by('-created_at').first()
    
    if latest_record:
        total_flow = latest_record.total_flow + daily_flow
    else:
        total_flow = daily_flow
    
    # Create new record
    FlowData.objects.create(
        date=current_date,
        time=current_time,
        day=current_day,
        daily_flow=daily_flow,
        total_flow=total_flow
    )
    
    return daily_flow, total_flow