from django.db import models
import uuid 
from django.contrib.auth.models import User


class BaseModel(models.Model):
	uid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
	create_date=models.DateField(auto_now_add=True)
	updated_at=models.DateField(auto_now_add=True)

	class Meta:
		abstract=True


class Blog(BaseModel):
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
	title=models.CharField(max_length=200)
	descriptiom=models.TextField()
	images=models.ImageField(upload_to="images_blog")


	def __str__(self):
		return self.title






