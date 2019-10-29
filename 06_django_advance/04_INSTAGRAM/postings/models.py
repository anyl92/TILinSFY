from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from django.urls import reverse

User = get_user_model()  # 우회해서 가져온당
# p = Posting.objects.first()
# p.author  # 작성자


class HashTag(TimeStampedModel):
    content = models.CharField(max_length=20, unique=True)


class Posting(TimeStampedModel):
    like_users = models.ManyToManyField(User, related_name='like_posts')
    # MTMF 컬럼이 아니고 테이블이 생기는데 뭐랑 뭐를 엮어주냐 (posting, user)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postings')  # get_user_model
    content = models.CharField(max_length=140)
    hashtags = models.ManyToManyField(HashTag, blank=True, related_name='postings')

    class Meta:
        ordering = ('-created', )

    def get_absolute_url(self):
        return reverse("postings:posting_detail", kwargs={"posting_id": self.pk})


class Image(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='images')
    file = ProcessedImageField(
        processors=[ResizeToFit(600, 600, mat_color=(45, 45, 45))], 
        upload_to='postings/images',
        format='JPEG',
        options={'quality': 90},
    )


class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=140)

# p = Posting.objects.last()
# p.image_set.all()  # related_name 이 default
# p.image.all()  # related_name='images'

