from application.db.people import *
from application.salary import *
from datetime import datetime

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print('Сегодня', datetime.now())
