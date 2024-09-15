from datetime import datetime, timedelta


def create_time_slots(start_time, end_time, start_break_time, end_break_time, slot_duration=30):
    # Parse the input times
    start_time = datetime.strptime(start_time, '%H:%M')
    end_time = datetime.strptime(end_time, '%H:%M')
    start_break_time = datetime.strptime(start_break_time, '%H:%M')
    end_break_time = datetime.strptime(end_break_time, '%H:%M')

    # Create a timedelta object for the slot duration
    slot_delta = timedelta(minutes=slot_duration)

    # Generate the time slots
    slots = []
    current_time = start_time

    while current_time < end_time:
        slot_start = current_time
        slot_end = current_time + slot_delta

        # Check if the slot overlaps with the break time
        if slot_end <= start_break_time or slot_start >= end_break_time:
            # Append the tuple (start, end) time of the slot if it's not in the break time
            slots.append({"start_time": slot_start.strftime('%H:%M'), "end_time": slot_end.strftime('%H:%M')})

        # Move to the next slot
        current_time = slot_end

    return slots

