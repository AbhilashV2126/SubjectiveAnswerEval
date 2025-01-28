from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class notification_table(models.Model):
    notification=models.CharField(max_length=100)
    date=models.DateField(max_length=100)

class courses_table(models.Model):
    course=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

class students_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    COURSE= models.ForeignKey(courses_table, on_delete=models.CASCADE)
    Sem=models.IntegerField()
    place = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    image = models.FileField()

class complaint_table(models.Model):
    STUDENT = models.ForeignKey(students_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.CharField(max_length=100)

class staff_table(models.Model):
    LOGIN = models.ForeignKey(login_table, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    image = models.FileField()

class subject_table(models.Model):
    COURSE = models.ForeignKey(courses_table, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    Sem = models.IntegerField()


class assign_sub_table(models.Model):
    SUBJECT = models.ForeignKey(subject_table, on_delete=models.CASCADE)
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)


class exam_table(models.Model):
    subject = models.ForeignKey(assign_sub_table,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
class question_table(models.Model):
    EXAMID = models.ForeignKey(exam_table, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)

class question_keys(models.Model):
    QUESTION=models.ForeignKey(question_table,on_delete=models.CASCADE)
    questionkey=models.CharField(max_length=50)


class feedback_table(models.Model):
    STAFF = models.ForeignKey(staff_table, on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(students_table, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    date = models.DateField()

class chat_table(models.Model):
    FROM = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name="fid")
    TO = models.ForeignKey(login_table, on_delete=models.CASCADE,related_name='tid')
    message = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()


class previous_question(models.Model):
    assign_sub = models.ForeignKey(assign_sub_table, on_delete=models.CASCADE)
    question = models.FileField()
    year = models.CharField(max_length=100)


class attend_exam(models.Model):
    STUDENT = models.ForeignKey(students_table, on_delete=models.CASCADE)
    QUESTION = models.ForeignKey(question_table, on_delete=models.CASCADE)
    answer=models.TextField()
    mark=models.FloatField()



class result_table(models.Model):
    STUDENT = models.ForeignKey(students_table, on_delete=models.CASCADE)
    EXAM = models.ForeignKey(exam_table, on_delete=models.CASCADE)
    result=models.BigIntegerField()
    status=models.CharField(max_length=100)

class notes_table(models.Model):
    SUBJECT=models.ForeignKey(subject_table, on_delete=models.CASCADE)
    NOTES = models.FileField()
    DATE = models.DateField()

