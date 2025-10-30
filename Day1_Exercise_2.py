
sales = {
    "January": 12000,
    "February": 15000,
    "March": 17000,
    "April": 8000,
    "May": 22000
}


total = sum(sales.values())
average = total / len(sales)
highest= max(sales.values())
lowests = min(sales.values())

print(f"Total Sales: {total}")
print(f"Average Sales: {average:.1f}")

for month, amount in sales.items():
    if(amount == highest):
        print(f"Best Month: {month}({amount})")
    if(amount == lowests):
        print(f"Weakness Month: {month}({amount})")



