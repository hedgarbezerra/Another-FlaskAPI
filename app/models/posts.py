import datetime

from app import db, ma



class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(40), nullable=False)
    description= db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    user = db.relationship('Users', back_populates='posts')
    commentaries = db.relationship('Commentaries', backref='posts', lazy=True)

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id


class PostsSchema(ma.Schema):

    class Meta:
        fields = ('id', 'title', 'description', 'user_id', 'created_on')


post_schema = PostsSchema(strict=True)
posts_schema = PostsSchema(many=True)
