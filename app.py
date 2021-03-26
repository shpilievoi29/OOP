import datetime

import traceback

from models import Programmer

from models import Recruiter

from models import Employee

from models import Candidate

from models import Vacancy

if __name__ == '__main__':
    igor = Programmer('Igor', 1000, 'igor@gmail.com', 'programmer', ['JS', 'Python', 'Delphi'])

    sasha = Programmer('Sasha', 130, 'sasha@gmai.com', 'programmer', ['Python'])

    curt = Recruiter('Cobain', 180, 'ineedagun@bang.us', 'recruiter')

    john = Candidate('John Fitzgerald Kennedy', 'oneshot@president.us', ["Python", 'JS'], ['Pylon', 'JS'],
                     ['Python -middle', 'JS-junior'])

    java = Vacancy('Java', ['Java game developer'], ['Java - middle', 'Python - senior'])

    full_stack = Vacancy('Full-Stack', ['PHP', 'MySQL', 'JS'], ['PHP - senior', 'MySql - senior', 'JS -middle'])
    oleg = Employee('Oleg', 120, 'privet@oleg.com', 'programmer')

    # print(Programmer.comparison_stack(igor, sasha))
    #print(Employee.check_salary(sasha, Employee.day_count))
    # print(sasha.__dict__)
    # print(igor.__dict__)
    # print(Programmer.comparison_stack(sasha, igor))
    # print(Employee.check_salary(igor, Employee.day_count))
try:
    Candidate.work(john)

except Exception as err:
    with open('logs.txt', 'a') as f:
        message = '{}    {}:\n {}\n \n'.format(datetime.datetime.now(), err.__class__.__name__, traceback.format_exc())
        f.write(message)

try:
    Employee.validate_email(oleg, "privet@oleg.com")

except Exception as err:
    with open('logs.txt', 'a') as f:
        message = '{}    {}:\n {}\n \n'.format(datetime.datetime.now(), err.__class__.__name__, traceback.format_exc())
        f.write(message)

    vasia = Programmer('Igor', 1000, 'igor@gmail.com', 'programmer', ['JS', 'Python', 'Delphi'])
    print(vasia.full_name)

zet = Candidate.create_candidate('employees.csv')