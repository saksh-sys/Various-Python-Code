# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'


from datetime import datetime, timedelta

def get_previous_date(date, n):
    # Convert date string to datetime object
    date_obj = datetime.strptime(date, '%y-%m-%d')

    # Calculate the previous date by subtracting timedelta
    previous_date = date_obj - timedelta(days=n)

    # Convert the previous date back to string representation
    previous_date_str = previous_date.strftime('%y-%m-%d')

    return previous_date_str


# Example usage
date = '16-12-10'
n = 11

previous_date = get_previous_date(date, n)
print(previous_date)
