from django.db.models import Model, DateTimeField, CharField, EmailField, TextField, BooleanField, ForeignKey, CASCADE


class AbstractModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractModel):
    username = CharField(max_length=56)
    full_name = CharField(max_length=56)
    email = EmailField(max_length=56)
    birthday = DateTimeField()
    bio = TextField()

    def __str__(self):
        return self.username


class Post(AbstractModel):
    title = CharField(max_length=256    )
    body = TextField()
    is_active = BooleanField(default=True)
    user_id = ForeignKey(User, CASCADE, related_name='posts')

    def __str__(self):
        return self.title


class Comment(AbstractModel):
    body = TextField()
    post_id = ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    user_id = ForeignKey(User, on_delete=CASCADE, related_name='comments')


class Like(AbstractModel):
    user_id = ForeignKey(User, on_delete=CASCADE, related_name='likes')
    post_id = ForeignKey(Post, on_delete=CASCADE, related_name='likes')