from connect import engine, db
from models import Program, Course



# program2 = Program(
#     name = "Bachelors of Computer Science",
#     years_of_study = 4
# )

# program1 = Program(
#     name = "Bachelors of Business",
#     years_of_study = 4
# )
# saving programs 
# db.add_all([program1, program2])
# db.commit()

# query for the created programs 
program1 = db.query(Program).filter_by(name = "Bachelors of Computer Science").first()
program2 = db.query(Program).filter_by(name = "Bachelors of Business").first()


# create course objects 
course1 = Course(
    title = "Data Structures",
    code = "CS101",
)

course2 = Course(
    title = "Database Management Systems",
    code = "CS104",
)
course3 = Course(
    title = "Human Resource Management",
    code = "BE 907",
)
course4 = Course(
    title = "Calculaus",
    code = "BE 908",
)
# program1.courses.append(course1)
# program1.courses.append(course2)
# program2.courses.append(course3)
# program2.courses.append(course4)
# db.commit()
