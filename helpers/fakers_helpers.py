from faker import Faker
import random


def create_contract_title():
    f = Faker()
    name = f.name()
    with open('./reporting/titles/title.txt', 'w') as file:
        file.write(str(name))


def read_contract_title():
    with open('./reporting/titles/title.txt', 'r') as file:
        name = file.read()
    return name


def get_released_amount():
    amount = random.randint(100, 500)
    return amount


def get_amount():
    amount = random.randint(1000000, 10000000)
    with open('./reporting/wallets/amount.txt', 'w') as file:
        file.write(str(amount))
    return amount


def get_deposited_amount():
    amount = random.randint(1000, 10000)
    with open('./reporting/wallets/amount.txt', 'w') as file:
        file.write(str(amount))
    return amount


def get_big_amount():
    amount = ['1000000', '10000000', '50000000']
    big = (random.choice(amount))
    return big


def get_cliff_percentage():
    cliff_amount = random.randint(1, 100)
    return cliff_amount


def get_seconds():
    seconds = random.randint(1, 60)
    return seconds


def get_minutes():
    minutes = random.randint(1, 59)
    return minutes


def get_hours():
    hours = random.randint(1, 23)
    return hours


def get_days():
    days = random.randint(1, 7)
    return days


def get_weeks():
    weeks = random.randint(1, 4)
    return weeks


def get_months():
    months = random.randint(1, 12)
    return months


def get_years():
    years = random.randint(1, 3)
    return years


def random_start_date():
    days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    months = ['01', '02', '03', '04', '05', '06']
    years = ['2025', '2026']
    day = (random.choice(days))
    month = (random.choice(months))
    year = (random.choice(years))
    return day + month + year


def random_end_date():
    days = ['11', '12', '13', '14', '15']
    months = ['11', '12']
    years = ['2027', '2028']
    day = (random.choice(days))
    month = (random.choice(months))
    year = (random.choice(years))
    return day + month + year


def random_start_time():
    minutes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']
    hours = ['01', '02', '03', '04', '05', '06']
    minute = (random.choice(minutes))
    hour = (random.choice(hours))
    return hour + minute + 'AM'


def random_end_time():
    minutes = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    hours = ['07', '08', '09', '10', '11', '12']
    minute = (random.choice(minutes))
    hour = (random.choice(hours))
    return hour + minute + 'PM'


def random_start_past_date():
    days = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    months = ['07', '08', '09', '10', '11', '12']
    years = ['2000', '2010']
    day = (random.choice(days))
    month = (random.choice(months))
    year = (random.choice(years))
    return day + month + year


def random_end_past_date():
    days = ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    months = ['07', '08', '09', '10', '11', '12']
    years = ['2010', '2020']
    day = (random.choice(days))
    month = (random.choice(months))
    year = (random.choice(years))
    return day + month + year
