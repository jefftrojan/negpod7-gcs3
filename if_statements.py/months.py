month = input("Please enter month name: ").title()

months_dict = {
    'January': '31 days',
    'February': '28 or 29 days',
    'March': '31 days',
    'April': '30 days',
    'May': '31 days',
    'June': '30 days',
    'July': '31 days',
    'August': '31 days',
    'September': '30 days',
    'October': '31 days',
    'November': '30 days',
    'December': '31 days'
}
month_days = months_dict.get(month)
print(month_days)
print(f"The month of {month} has {month_days} days.")
