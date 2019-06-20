import datetime

from app import db, ma


class Commentaries(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commentary = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    user = db.relationship('Users', back_populates='commentaries')
    post = db.relationship('Posts', back_populates='commentaries')

    def __init__(self, commentary, user_id, post_id):
        self.commentary = commentary
        self.user_id = user_id
        self.post_id = post_id


class CommentariesSchema(ma.Schema):

    class Meta:
        fields = ('id', 'commentary', 'user_id', 'post_id', 'created_on')


commentary_schema = CommentariesSchema(strict=True)
commentaries_schema = CommentariesSchema(many=True)
