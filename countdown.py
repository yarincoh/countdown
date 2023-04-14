from datetime import datetime

def parse_countdown_string(countdown_string):
    try:
        parts = countdown_string.split()
        if len(parts) == 2:
            date_str, time_str = parts
        else:
            date_str = countdown_string
            time_str = '00:00:00'
            
        if '/' in date_str:
            day, month, year = map(int, date_str.split('/'))
        else:
            year, month, day = map(int, date_str.split('-'))
        
        hour, minute, second = map(int, time_str.split(':'))
        
        return datetime(year, month, day, hour, minute, second)
    except ValueError:
        print("Error: invalid input format")
        return None

countdown_string = input("Enter a countdown time (D:H:M:S or DD/MM/YYYY HH:MM:SS): ")
target_time = parse_countdown_string(countdown_string)

if target_time:
    while True:
        time_left = target_time - datetime.now()
        if time_left.total_seconds() < 0:
            print("Countdown is over!")
            break
        print("Time remaining: ", str(time_left).split(".")[0], end='\r')
