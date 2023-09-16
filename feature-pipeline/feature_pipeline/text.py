from datetime import timedelta

# Create a timedelta representing 3 days, 4 hours, and 30 minutes
duration = timedelta(days=3, hours=4, minutes=30)
print(f"Duration10001: {duration}")

# Extract and format components
days = duration.days
hours, remainder = divmod(duration.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Duration: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
