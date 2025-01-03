from datetime import datetime, timedelta, time  # Import time explicitly

def create_time_slots(start_time, end_time, start_break_time, end_break_time, slot_duration=30):
    # Parse the input times
    if isinstance(start_time, time):  # Use time type here
        start_time = start_time.strftime('%H:%M:%S')
    if isinstance(end_time, time):  # Use time type here
        end_time = end_time.strftime('%H:%M:%S')
    
    # Assuming strptime() is being used for formatting the time
    start_time_obj = datetime.strptime(start_time, '%H:%M:%S')
    end_time_obj = datetime.strptime(end_time, '%H:%M:%S')
    
    # Create a timedelta object for the slot duration
    slot_delta = timedelta(minutes=slot_duration)

    # Generate the time slots
    slots = []
    current_time = start_time_obj

    while current_time < end_time_obj:
        slot_start = current_time
        slot_end = current_time + slot_delta

        # Check if the slot overlaps with the break time
        if slot_end.time() <= start_break_time or slot_start.time() >= end_break_time:  
            # Convert back to time format for slots
            slots.append({"start_time": slot_start.strftime('%H:%M'), "end_time": slot_end.strftime('%H:%M')})

        # Move to the next slot
        current_time = slot_end

    return slots
