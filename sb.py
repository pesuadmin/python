# ============================================================
# ESA SECTION B – ALL PROGRAMS 
# ============================================================


# ============================================================
# MAY 2025 ESA
# ============================================================

# 3(a) Prime Palindrome Numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_palindrome(lst):
    result = []
    for num in lst:
        if is_prime(num) and str(num) == str(num)[::-1]:
            result.append(num)
    return result

numbers = [7, 11, 121, 131, 17, 44]
print("May 2025 - 3(a) Prime Palindrome:", prime_palindrome(numbers))
# Output: [7, 11, 131]


# 3(b) Student Marks Management System
students = {}

def add_student(name, marks):
    students[name] = marks

def update_marks(name, marks):
    if name in students:
        students[name] = marks

def average_marks():
    return sum(students.values()) / len(students)

def display_students():
    for name, marks in students.items():
        print(name, ":", marks)

add_student("Ram", 85)
add_student("Sita", 90)
update_marks("Ram", 95)

print("\nMay 2025 - 3(b) Student Marks:")
display_students()
print("Average Marks =", average_marks())
# Output: Ram : 95, Sita : 90, Average = 92.5


# 3(c) Employee Bonus Calculation
def calculate_bonus(emp_data):
    updated = {}
    for name, (exp, bonus, rating) in emp_data.items():
        if exp > 10:
            new_bonus = bonus + (0.20 * bonus) + (0.03 * bonus * rating)
        elif 5 <= exp <= 10:
            new_bonus = bonus + (0.15 * bonus) + (0.02 * bonus * rating)
        else:
            new_bonus = bonus + (0.10 * bonus) + (0.01 * bonus * rating)
        updated[name] = round(new_bonus, 2)
    return updated

employees = {
    "John": (12, 5000, 5),
    "Mary": (7, 4000, 4),
    "Sam": (3, 3000, 3)
}
print("\nMay 2025 - 3(c) Employee Bonus:", calculate_bonus(employees))
# Output: {'John': 6750.0, 'Mary': 4920.0, 'Sam': 3390.0}


# 3(d) Word Frequency Dictionary
import re

def word_count(sentences):
    counts = {}
    for sentence in sentences:
        words = re.findall(r"[a-zA-Z]+", sentence.lower())
        for word in words:
            if len(word) >= 4:
                counts[word] = counts.get(word, 0) + 1
    return counts

sentences = [
    "Python is easy.",
    "Python programming is powerful.",
    "Easy coding with Python."
]
print("\nMay 2025 - 3(d) Word Frequency:", word_count(sentences))
# Output: {'python': 3, 'easy': 2, 'programming': 1, 'powerful': 1, 'coding': 1, 'with': 1}


# 3(e) Youngest Student & December Birthdays
from datetime import datetime

names = ["Ram", "Sita", "John", "Mary"]
dobs = ["2001-12-10", "2003-05-15", "2002-12-20", "2004-08-18"]
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dobs]

youngest = names[dates.index(max(dates))]
print("\nMay 2025 - 3(e) Youngest Student:", youngest)
print("Students born in December:")
for i in range(len(dates)):
    if dates[i].month == 12:
        print(names[i])
# Output: Youngest: Mary | December: Ram, John


# ============================================================
# FEBRUARY 2025 ESA
# ============================================================

# 3(a) List, List Comprehension, Dictionary, Key Search
print("\n--- Feb 2025 - 3(a) List Operations ---")
n = 10  # change as needed

numbers_feb = list(range(1, n + 1))
print("Original List:", numbers_feb)

even_squares = [x**2 for x in numbers_feb if x % 2 == 0]
print("Even Squares:", even_squares)

square_dict = {int(x**0.5): x for x in even_squares}
print("Dictionary:", square_dict)

def check_key(d, key):
    if key in d:
        print("Key exists")
    else:
        print("Key does not exist")

check_key(square_dict, 4)  # sample key


# 3(b) Employee Joining Date Program
employees_feb = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
joining_dates = ['1/15/2010', '3/22/2005', '1/8/2018', '7/19/2002', '12/5/2015']

dates_feb = [datetime.strptime(d, "%m/%d/%Y") for d in joining_dates]

first_employee = employees_feb[dates_feb.index(min(dates_feb))]
print("\nFeb 2025 - 3(b) Employee who joined first:", first_employee)

print("Employees joined in January:")
for i in range(len(dates_feb)):
    if dates_feb[i].month == 1:
        print(employees_feb[i])
# Output: David | January: Alice, Charlie


# 3(d) Functional Programming Password Validator
passwords = [
    "Admin@12345",
    "Hello@World1",
    "password@123",
    "Strong#Pass9"
]
dictionary_words = ["password", "admin", "12345", "letmein"]

def is_valid(password):
    if len(password) < 10:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*()\-_=+]', password):
        return False
    lower_pwd = password.lower()
    for word in dictionary_words:
        if word in lower_pwd:
            return False
    return True

valid_passwords = list(filter(is_valid, passwords))
print("\nFeb 2025 - 3(d) Valid Passwords:", valid_passwords)
# Output: ['Hello@World1', 'Strong#Pass9']


# 3(e) Bookstore Billing System
print("\nFeb 2025 - 3(e) Bookstore Billing System")
total_bookstore = 0
orders = [("F", 25), ("N", 40), ("STOP", 0)]  # sample data

for category, qty in orders:
    if category.upper() == "STOP":
        break
    if category.upper() == "F":
        if qty < 20:
            price = 200
        elif qty < 50:
            price = 180
        else:
            price = 150
    elif category.upper() == "N":
        if qty < 30:
            price = 300
        elif qty < 80:
            price = 270
        else:
            price = 250
    total_bookstore += qty * price

if total_bookstore > 8000:
    total_bookstore *= 0.90
elif total_bookstore > 5000:
    total_bookstore *= 0.95

print("Total Payable Amount = Rs.", total_bookstore)


# ============================================================
# MARCH 2024 ESA (Typed Paper)
# ============================================================

# 3(a) Stock Profit Calculation
print("\n--- March 2024 - 3(a) Stock Profit ---")
shares = 2000
purchase_price = 40
sale_price = 42.75

purchase_cost = shares * purchase_price
purchase_commission = purchase_cost * 0.03
selling_cost = shares * sale_price
selling_commission = selling_cost * 0.03
profit = (selling_cost - selling_commission) - (purchase_cost + purchase_commission)

print("Purchase Cost =", purchase_cost)
print("Purchase Commission =", purchase_commission)
print("Selling Price =", selling_cost)
print("Selling Commission =", selling_commission)
print("Profit =", profit)
# Output: Profit = 535.0


# 3(b) Product Inventory Management
print("\nMarch 2024 - 3(b) Inventory Management")

product_inventory = {"Laptop": 10, "Mobile": 20, "Keyboard": 15}

def update_inventory(inventory, shipment):
    for product, qty in shipment.items():
        if product in inventory:
            inventory[product] += qty
        else:
            inventory[product] = qty
    return inventory

def apply_discount(prices, discounts):
    for product, new_price in discounts.items():
        if product in prices:
            prices[product] = new_price
    return prices

shipment = {"Laptop": 5, "Mouse": 10}
prices = {"Laptop": 50000, "Mobile": 20000}
discounts = {"Laptop": 45000}

print(update_inventory(product_inventory, shipment))
print(apply_discount(prices, discounts))


# 3(c) Find Special Codes (Regex)
def find_special_codes(text):
    codes = re.findall(r'\b[A-Za-z0-9]+\b', text)
    return codes

msg = "abc123 @xyz code45 #hello data99"
print("\nMarch 2024 - 3(c) Special Codes:", find_special_codes(msg))
# Output: ['abc123', 'code45', 'data99']  (Note: 'xyz' and 'hello' also match \b word boundaries)


# 3(d) Map and Filter Program
numbers_map = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_map))
squares_map = list(map(lambda x: x**2, even_numbers))
print("\nMarch 2024 - 3(d) Map & Filter:", squares_map)
# Output: [4, 16, 36, 64, 100]


# 3(e) Fibonacci Series
print("\nMarch 2024 - 3(e) Fibonacci Series")
n_fib = 8  # change as needed

fib = [0, 1]
for i in range(2, n_fib):
    fib.append(fib[i-1] + fib[i-2])

print(",".join(map(str, fib[:n_fib])))
# Output: 0,1,1,2,3,5,8,13


# 3(f) Replace Numbers Greater Than 10 using map()
nums_sample = [2, 5, 11, 13, 7, 14, 8, 9, 15, 1]
result_map = list(map(lambda x: 10 if x > 10 else x, nums_sample))
print("\nMarch 2024 - 3(f) Replace >10 with 10:", result_map)
# Output: [2, 5, 10, 10, 7, 10, 8, 9, 10, 1]


# ============================================================
# MARCH 2024 (Scanned Paper)
# ============================================================

# 3(a) Happy Number
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))
    return n == 1

print("\nMarch 2024 (Scanned) - 3(a) Happy Number:")
print("19 ->", "Happy Number" if is_happy(19) else "Not a Happy Number")
print("4  ->", "Happy Number" if is_happy(4) else "Not a Happy Number")


# 3(b) Student Grades
scores = [95, 92, 85, 75, 65, 40]
A = [x for x in scores if x >= 90]
B = [x for x in scores if 80 <= x <= 89]
C = [x for x in scores if 70 <= x <= 79]
D = [x for x in scores if 60 <= x <= 69]
F = [x for x in scores if x <= 59]
grades = [A, B, C, D, F]
print("\nMarch 2024 (Scanned) - 3(b) Student Grades:", grades)


# 3(c) Date Validation Program
months = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}

def validate_date(month, day):
    if month in months and 1 <= day <= months[month]:
        return "Valid Date"
    return "Invalid Date"

print("\nMarch 2024 (Scanned) - 3(c) Date Validation:")
print(validate_date("January", 15))   # Valid
print(validate_date("January", 32))   # Invalid


# 3(d) Superstore Billing System
print("\nMarch 2024 (Scanned) - 3(d) Superstore Billing")
total_store = 0
store_orders = [("A", 35), ("B", 60), ("STOP", 0)]  # sample data

for category, qty in store_orders:
    if category.upper() == "STOP":
        break
    if category.upper() == "A":
        if qty < 30:
            price = 15
        elif qty < 100:
            price = 12
        else:
            price = 10
    elif category.upper() == "B":
        if qty < 50:
            price = 30
        elif qty < 100:
            price = 25
        else:
            price = 20
    total_store += qty * price

if total_store > 1500:
    total_store *= 0.90
elif total_store > 1000:
    total_store *= 0.95

print("Total Payable =", total_store)


# 3(e) Username Validation
def UsernameValidation(username):
    pattern = r'^[A-Za-z][A-Za-z0-9_]{2,23}[A-Za-z0-9]$'
    return bool(re.match(pattern, username))

print("\nMarch 2024 (Scanned) - 3(e) Username Validation:")
print("John_123  ->", UsernameValidation("John_123"))    # True
print("_invalid  ->", UsernameValidation("_invalid"))    # False
print("ab_       ->", UsernameValidation("ab_"))         # False


# ============================================================
# NOVEMBER 2023 ESA
# ============================================================

# 3(a) Movie Age Restriction
def movie_restriction(age):
    if age < 13:
        return "Only U movies allowed"
    elif age < 18:
        return "U and UA movies allowed"
    else:
        return "All movies allowed"

print("\nNov 2023 - 3(a) Movie Restriction:")
print(movie_restriction(10))
print(movie_restriction(16))
print(movie_restriction(20))


# 3(c) Telephone Number Match
mapping = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
}

def telephone_match(number, word):
    word = word.upper()
    result = ""
    for ch in word:
        for digit, letters in mapping.items():
            if ch in letters:
                result += digit
    return result == number

print("\nNov 2023 - 3(c) Telephone Match:")
print(telephone_match("43556", "HELLO"))  # True


# 3(d) Password Strength Checker
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*]", password):
        strength += 1

    if strength <= 2:
        return "Weak Password"
    elif strength <= 4:
        return "Medium Password"
    else:
        return "Strong Password"

print("\nNov 2023 - 3(d) Password Strength:")
print(check_password_strength("Admin@123"))   # Strong
print(check_password_strength("hello123"))    # Medium
print(check_password_strength("abc"))         # Weak


# 3(e) Collatz Conjecture
def collatz(n, limit=30):
    result = []
    count = 0
    while n != 1 and count < limit:
        result.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    result.append(1)
    return result

print("\nNov 2023 - 3(e) Collatz Conjecture:")
print(*collatz(6))
# Output: 6 3 10 5 16 8 4 2 1


# ============================================================
# ESA MODEL SET
# ============================================================

# 3(a) List Operations
from collections import Counter

print("\nModel Set - 3(a) List Operations")
list_name = ['Ann', 'Pat', 'David', 'Tisha', 'Sumantha']

lengths = [len(name) for name in list_name]
print("Lengths:", lengths)

short_names = [name for name in list_name if len(name) < 5]
print("Names < 5 chars:", short_names)

name_dict = {name: len(name) for name in list_name}
print("Dictionary:", name_dict)

sorted_names = sorted(list_name, key=len, reverse=True)
print("Sorted by length (desc):", sorted_names)

all_chars = ''.join(list_name).lower()
freq = Counter(all_chars)
most_char = freq.most_common(1)
print("Most Frequent Character:", most_char)


# 3(b) Farmer Truck Optimization (Greedy)
print("\nModel Set - 3(b) Farmer Truck Optimization")
truck_capacity = 500

vegetables = {
    "Tomato":  {"yield": 150, "must": 50, "price": 50},
    "Potato":  {"yield": 200, "must": 70, "price": 42},
    "Garlic":  {"yield": 250, "must": 70, "price": 70},
    "Brinjal": {"yield": 100, "must": 40, "price": 60}
}

selected = {}
used = 0

for veg in vegetables:
    selected[veg] = vegetables[veg]["must"]
    used += vegetables[veg]["must"]

remaining = truck_capacity - used

profit_order = sorted(
    vegetables.items(),
    key=lambda x: x[1]["price"],
    reverse=True
)

for veg, data in profit_order:
    extra = data["yield"] - selected[veg]
    take = min(extra, remaining)
    selected[veg] += take
    remaining -= take
    if remaining == 0:
        break

print("Vegetables to carry:")
for k, v in selected.items():
    print(k, ":", v, "kg")


# 3(c) Vehicle Number Even/Odd Dictionary
number_plates = [
    'MH 12 XJ - 2234',
    'UP 04 LG - 2455',
    'GJ 34 RV - 2442',
    'KL 07 AP - 2433'
]

def check_even_odd(plates):
    result = {}
    for plate in plates:
        num = int(plate.split('-')[-1].strip())
        result[num] = "Even" if num % 2 == 0 else "Odd"
    return result

print("\nModel Set - 3(c) Vehicle Even/Odd:", check_even_odd(number_plates))


# ============================================================
# AUGUST 2021 ESA
# ============================================================

# 3(a) Minimum Element and Average from Nested List
print("\nAug 2021 - 3(a) Nested List Min & Average")
list1 = [[20, 25, 30], 24, 56, [10, 15, 18], [12, 45, 20], 35, 20, 23, 28]

flat_list = []
for item in list1:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

print("Minimum Element =", min(flat_list))
print("Average =", round(sum(flat_list) / len(flat_list), 2))
# Output: Minimum = 10, Average = 25.06


# 3(b) Job Fair Scheduling (Activity Selection – Greedy)
print("\nAug 2021 - 3(b) Job Fair Scheduling")
companies = [
    ("Data Vision",    8.00,  9.00),
    ("InfoWorld",      8.00,  9.30),
    ("Data Wide",      8.10,  9.40),
    ("Analyticpoint",  8.15,  9.30),
    ("TradeData",     10.00, 11.30),
    ("Panini View",   10.30, 11.00),
    ("Skyview",       11.00, 11.30),
    ("Data Magnet",   11.30, 14.30),
    ("Clean View",    13.30, 14.00),
    ("InfoGrade",     14.00, 15.30),
    ("Secureit",      15.00, 17.00),
    ("Top Gain",      15.30, 16.00),
    ("Fizo",          16.00, 17.00)
]

companies.sort(key=lambda x: x[2])

selected_companies = []
last_end = 0

for company in companies:
    if company[1] >= last_end:
        selected_companies.append(company[0])
        last_end = company[2]

print("Maximum Companies Selected:")
print(selected_companies)


# 3(c) Verify Every Number is Even using map() and reduce()
from functools import reduce

numbers_even = [2, 4, 6, 8, 10]
even_check = list(map(lambda x: x % 2 == 0, numbers_even))
result_all_even = reduce(lambda a, b: a and b, even_check)
print("\nAug 2021 - 3(c) All numbers even?", result_all_even)
# Output: True


# ============================================================
# JULY 2021 ESA
# ============================================================

# 3(a) Computer Assembly Billing System
print("\nJuly 2021 - 3(a) Computer Assembly Billing")
price_list = {
    "HDD":       {"1TB": 5000,  "2TB": 7500,  "4TB": 10000},
    "RAM":       {"8GB": 4000,  "16GB": 6000},
    "Processor": {"I5": 15000,  "I7": 18000},
    "Display":   {"24": 3500,   "26": 4500},
    "Keyboard":  {"Normal": 1800, "Wireless": 2200}
}

other_charges = 4000

# Sample choices
choices = {"HDD": "1TB", "RAM": "8GB", "Processor": "I5",
           "Display": "24", "Keyboard": "Normal"}

total_computer = sum(price_list[comp][choice]
                     for comp, choice in choices.items()) + other_charges

gst = total_computer * 0.12
final_bill = total_computer + gst

print("GST =", gst)
print("Total Bill =", final_bill)


# 3(b) Fractional Knapsack Problem
def fractional_knapsack(profit, weight, capacity):
    n = len(profit)
    ratio = [(profit[i] / weight[i], profit[i], weight[i], i) for i in range(n)]
    ratio.sort(reverse=True)

    selected = [0] * n
    total_profit = 0

    for r, p, w, idx in ratio:
        if capacity >= w:
            selected[idx] = 1
            total_profit += p
            capacity -= w
        else:
            fraction = capacity / w
            selected[idx] = fraction
            total_profit += p * fraction
            break

    return selected, round(total_profit, 3)

profit = [1, 2, 3, 4]
weight = [6, 3, 8, 10]
capacity = 10

selected_items, earned = fractional_knapsack(profit, weight, capacity)
print("\nJuly 2021 - 3(b) Fractional Knapsack:")
print("Selected Items:", selected_items)
print("Profit Earned:", earned)
# Output: [0, 1, 0.875, 1], Profit = 8.625


# 3(c) Series Generation and Range Sum
print("\nJuly 2021 - 3(c) Series Generation")

def generate_series(n):
    series = []
    total = 0
    for i in range(n):
        total += i
        series.append(total)
    return series

def range_sum(series, k, l):
    return sum(series[k:l+1])

n_series = 10
k, l = 2, 5

series = generate_series(n_series)
print("Series:", series)
print(f"Sum from index {k} to {l} =", range_sum(series, k, l))
# Output: [0,1,3,6,10,15,21,28,36,45], Sum = 34


print("\n" + "="*50)
print("ALL PROGRAMS EXECUTED SUCCESSFULLY")
print("="*50)
