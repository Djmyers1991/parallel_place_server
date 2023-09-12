from django.db import models

class Assignment_Submission(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True, related_name="assignments_graded_by_teacher")
    student = models.ForeignKey("Student", on_delete=models.DO_NOTHING, related_name="assignments_completed_by_student")
    assignment = models.ForeignKey("Assignment", on_delete=models.DO_NOTHING, related_name="submissions_per_assignment")
    submission = models.CharField(max_length=10000)
    teacher_feedback = models.CharField(max_length=10000)
    date_reviewed = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)



