import calendar 

def display_calendar():
  
  print()
  year = int(input("Enter the year: "))
  month = int(input("Enter the month(1-12): "))
  print()

  cal = calendar.TextCalendar(calendar.SUNDAY)

  month_calendar = cal.formatmonth(year, month)
  print(month_calendar)

display_calendar()