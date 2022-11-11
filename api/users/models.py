from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db import connection


class User(AbstractUser):
    """
    Default custom user model for API.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    
    #: First and last name do not cover name patterns around the globe
    email = models.EmailField(unique=True, blank=False, null=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    company = models.CharField(max_length=10, null=False, default='')
    created_by = models.DateTimeField(auto_now_add=True, null=True)
    phonenumber = models.CharField(blank=False, null=False, max_length=30, default='')
    position = models.CharField(max_length=10, blank=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    REQUIRED_FIELDS = ["id", "email", "name", "company", "phonenumber", "position"]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})



        

class NeuralDropTasks(models.Model):
   Taskname = models.CharField(max_length=100, null=True)
   dateofuse = models.DateTimeField(auto_now_add=True)
   #File = models.FileField(null=True, upload_to=user_directory_path)
   FileType = models.CharField(max_length=50,null=False,default='file')
   Checkbox1 = models.CharField(max_length=100,null=True)
   Checkbox2 = models.CharField(max_length=100,null=True)
   company_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
   state = models.CharField(max_length=10, default='null')



def user_directory_path(instance, filename):
    #file will be uploaded to MEDIA_ROOT/user_id/filename
    return 'user_{0}/{1}'.format(instance.company_id.id, filename)



class TestingTasks(models.Model):
   File = models.FileField(null=True, upload_to=user_directory_path)
   FileType = models.CharField(max_length=50,null=False,default='file')
   Checkbox1 = models.CharField(max_length=10,null=True)
   Checkbox2 = models.CharField(max_length=10,null=True)
   

class CompanyInfo(models.Model):
    company_uid = models.UUIDField(primary_key=True)
    company_name = models.CharField(max_length=100)
    commit_date = models.DateField()
    insdustry = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'company_info'   


class NeuraldropUseHistory(models.Model):
    neuraldrop_use_history_uid = models.UUIDField(primary_key=True)
    task_name = models.CharField(max_length=100)
    date_of_use = models.DateField()
    ai_file_name_to_compress = models.CharField(max_length=100)
    ai_file_path_to_compress = models.CharField(max_length=100)
    company_uid = models.ForeignKey(CompanyInfo, models.DO_NOTHING, db_column='company_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neuraldrop_use_history'

class CompressionTech(models.Model):
    tech_id = models.BigAutoField(primary_key=True)
    tech_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'compression_tech'


class NeuraldropUseResult(models.Model):
    neuraldrop_use_result_uid = models.UUIDField(primary_key=True)
    compressed_ai_name = models.CharField(max_length=100)
    compressed_ai_file_path = models.CharField(max_length=100)
    used_tech = models.ForeignKey(CompressionTech, models.DO_NOTHING, blank=True, null=True)
    recommended_tech1 = models.ForeignKey(CompressionTech, models.DO_NOTHING, db_column='recommended_tech1', blank=True, null=True, related_name='+')
    recommended_tech2 = models.ForeignKey(CompressionTech, models.DO_NOTHING, db_column='recommended_tech2', blank=True, null=True, related_name='+')
    recommended_tech3 = models.ForeignKey(CompressionTech, models.DO_NOTHING, db_column='recommended_tech3', blank=True, null=True, related_name='+')
    recommended_tech4 = models.ForeignKey(CompressionTech, models.DO_NOTHING, db_column='recommended_tech4', blank=True, null=True, related_name='+')
    recommended_tech5 = models.ForeignKey(CompressionTech, models.DO_NOTHING, db_column='recommended_tech5', blank=True, null=True, related_name='+')
    neuraldrop_use_history_uid = models.OneToOneField(NeuraldropUseHistory, models.DO_NOTHING, db_column='neuraldrop_use_history_uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'neuraldrop_use_result'


class Task(models.Model):
    taskname = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=100, default='upload', null=True)
    userId = models.ForeignKey(User, models.CASCADE, null=True)


class File(models.Model):
    fileInput = models.FileField(null=True)
    FileType = models.CharField(max_length=50,null=True,default='file')
    Checkbox1 = models.CharField(max_length=100,null=True)
    Checkbox2 = models.CharField(max_length=100,null=True)
    taskId = models.ForeignKey(Task, models.CASCADE, null=True)
    userId = models.ForeignKey(User, models.CASCADE, null=True)


class RecommendedTech1(models.Model):
    # 파일들이 여기에 들어가게끔 구현하여서 api를 통한 삽입을 구현 할 수 있다
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2) 
    File = models.FileField(null=True)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)     

    
class RecommendedTech2(models.Model):
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2)
    File = models.FileField(null=True)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)     


class RecommendedTech3(models.Model):
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2)
    File = models.FileField(null=True) 
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)     


class RecommendedTech4(models.Model):
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2) 
    File = models.FileField(null=True)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)     


class RecommendedTech5(models.Model):
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2) 
    File = models.FileField(null=True)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)     


class RecommendedTech6(models.Model):
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2) 
    File = models.FileField(null=True)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)        


class ResultTech(models.Model):
    Performance = models.DecimalField(max_digits=5, decimal_places=2)
    Parameter = models.DecimalField(max_digits=5, decimal_places=2)
    Size = models.DecimalField(max_digits=5, decimal_places=2)
    Computation = models.DecimalField(max_digits=5, decimal_places=2) 
    File = models.FileField(null=True)
    TaskId = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)  


class TestingAiModel(models.Model):
    Modelname = models.CharField(max_length=10, null=True)
    File = models.FileField()


class ContactUs(models.Model):
    company = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    firstName = models.CharField(max_length=10)
    lastName = models.CharField(max_length=20)
    jobTitle = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50)
    message = models.TextField()
    REQUIRED_FIELDS = [ 'company','industry','firstName','lastName','jobTitle','email','message']    