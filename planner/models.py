from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Major(models.Model):
    maj_id = models.AutoField(primary_key=True)
    maj_name = models.CharField(max_length=40)

class MajorSubject(models.Model):
    majsub_id = models.AutoField(primary_key=True)
    majsub_grade = models.PositiveIntegerField()
    majsub_semester = models.CharField(max_length=2)
    majsub_name = models.CharField(max_length=40)
    majsub_credit = models.PositiveIntegerField()
    majsub_required = models.BooleanField(default=False)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, db_column="maj_id")

class ElectiveSubject(models.Model): #교양과목
    elecsub_id = models.AutoField(primary_key=True)
    elecsub_name = models.CharField(max_length=40)
    elecsub_credit = models.PositiveIntegerField()

class GraudationConditionDetail(models.Model):
    grddet_id= models.AutoField(primary_key=True)
    grddet_name = models.CharField(max_length=10)
    grddet_majormintotal = models.PositiveIntegerField()
    grddet_secondmajormintotal = models.PositiveIntegerField()
    grddet_minormintotal = models.PositiveIntegerField()
    grddet_electivemintotal = models.PositiveIntegerField()
    major = models.ForeignKey(Major, on_delete=models.CASCADE, db_column="maj_id") #major is different so we connect major_id as foreignkey.

class GraduationCondition(models.Model):
    grdcon_id = models.AutoField(primary_key=True)
    grdcon_stunum = models.IntegerField() #max=?
    grdcon_total = models.PositiveIntegerField()
    grdconditiondetail = models.ForeignKey(GraudationConditionDetail, on_delete=models.CASCADE, db_column="grddet_id")

class Student(models.Model):
    stu_id = models.AutoField(primary_key=True)
    stu_password = models.CharField(max_length=50)
    stu_name = models.CharField(max_length=10)
    stu_number = models.CharField(max_length=2)
    stu_email = models.EmailField()
    stu_secondmajor = models.CharField(max_length=5)
    stu_majorcredit = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    stu_secondmajorcredit = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    stu_electivecredit = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    stu_retakecredit = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    graduatecondition = models.ForeignKey(GraduationCondition, null=True, on_delete=models.CASCADE, db_column="grdcon_id")
    firstmajor = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="firstmajor", db_column="maj_id1")
    secondmajor = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="secondmajor", db_column="maj_id2")

    # def find_graduatecondition(self):
    #     if self.firstmajor
        


class Timetable(models.Model):
    time_id = models.AutoField(primary_key=True)
    time_semester = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, db_column="stu_id")

class TimetableDetail(models.Model):
    timedetail_id = models.AutoField(primary_key=True)
    timedetail_retake = models.BooleanField(default=False)
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, db_column="time_id")
    majorsubjet = models.ForeignKey(MajorSubject, on_delete=models.CASCADE, db_column="majsub_id")

