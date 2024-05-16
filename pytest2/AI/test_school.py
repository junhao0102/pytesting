import pytest
from school import classroom, Teacher, Student, TooManyStudentsError

@pytest.fixture
def hogwarts_classroom():
    # 哈利波特主题的人物
    teacher = Teacher("Professor McGonagall")
    students = [Student("Harry"), Student("Hermione"), Student("Ron")]
    course = "Transfiguration"
    return classroom(teacher, students, course)

# 测试初始化
def test_classroom_initialization(hogwarts_classroom):
    assert hogwarts_classroom.teachers.name == "Professor McGonagall"
    assert len(hogwarts_classroom.students) == 3
    assert hogwarts_classroom.course == "Transfiguration"

# 测试添加学生
def test_add_student(hogwarts_classroom):
    hogwarts_classroom.add_student(Student("Draco"))
    assert len(hogwarts_classroom.students) == 4
    with pytest.raises(TooManyStudentsError):
        for _ in range(7):  
            hogwarts_classroom.add_student(Student("New Student"))


# 测试移除学生
def test_remove_student(hogwarts_classroom):
    hogwarts_classroom.remove_student("Harry")
    assert len(hogwarts_classroom.students) == 2
    assert not any(s.name == "Harry" for s in hogwarts_classroom.students)

# 测试更换老师
def test_change_teacher(hogwarts_classroom):
    hogwarts_classroom.change_teacher(Teacher("Dumbledore"))
    assert hogwarts_classroom.teacher.name == "Dumbledore"
