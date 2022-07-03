def time_float_to_string(hours):
    
    predznak = "" if hours >= 0 else "-"
    hours = abs(hours)
    
    hour = int(hours)
    minutes = (hours - hour) * 60
    minutes = int(minutes)
    return f"{predznak}{str(hour).zfill(2)}:{str(minutes).zfill(2)}"