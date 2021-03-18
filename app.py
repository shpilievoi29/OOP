from models import Programmer

from models import Recruiter

from models import Employee


class Candidate:

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


if __name__ == "__main__":

    igor = Programmer('Igor', 1000, 'igor@gmail.com', 'programmer', ['JS', 'Python', 'Delphi'])

    sasha = Programmer('Sasha', 130, 'sasha@gmai.com', 'programmer', ['Python'])

    curt = Recruiter('Cobain', 180, 'ineedagun@bang.us', 'recruiter')

    john = Candidate('John Fitzgerald Kennedy', 'oneshot@president.us', ["Python", 'JS'], ['Pylon', 'JS'],
                     ['Python -middle', 'JS-junior'])

    java = Vacancy('Java', ['Java game developer'], ['Java - middle', 'Python - senior'])

    full_stack = Vacancy('Full-Stack', ['PHP', 'MySQL', 'JS'], ['PHP - senior', 'MySql - senior', 'JS -middle'])

print(Programmer.comparison_stack(igor, sasha))
print(Employee.check_salary(sasha, Employee.day_count))
