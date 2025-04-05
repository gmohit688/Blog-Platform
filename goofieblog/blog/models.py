from django.db import models
from django.contrib.auth.models import User
from faker import Faker
import random

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Delete")
)

# Create your models here.
class posts(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    metades = models.CharField(max_length=300,default = "new post")
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
        def __str__(self):
            return self.title

fake = Faker()

for _ in range(10):  # Adjust the range to create the desired number of entries
    post = posts(
        title=fake.sentence(),
        slug=fake.slug(),
        author=User.objects.order_by('?').first(),  # Randomly select an existing user
        content=fake.paragraph(nb_sentences=5),
        metades=fake.sentence(),
        status=random.choice([0, 1, 2])
    )
    post.save()

print("Random posts created successfully!")