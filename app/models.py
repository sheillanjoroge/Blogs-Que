from . import db
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),unique = True,nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    post = db.relationship('Post', backref='user', lazy='dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)


    def __repr__(self):
        return f'User {self.username}'






class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255),nullable = False)
    post_pic_path = db.Column(db.String())
    post = db.Column(db.Text(), nullable = False)
    category = db.Column(db.String(255), index = True,nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    comment = db.relationship('Comment',backref='post',lazy='dynamic')

    @classmethod
    def clear_post(cls):
        Bloc.post.clear()

    @classmethod
    def get_posts(cls):
        post = Post.query.filter_by(id = id).all()
        return post

    def delete(self, id):
        comments = Comment.query.filter_by(id = id).all()
        for comment in comments:
            db.session.delete(comment)
            db.session.commit()
        db.session.delete(self)
        db.session.commit()


    def __repr__(self):
        return f'Post {self.name}' 




class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))


    @classmethod
    def clear_comment(self):
        Comment.comments.clear()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(post_id = id).all()
        return comments    


    def __repr__(self):
        return f'comment:{self.comment}'

class Quotes:
    '''
    Quote class to define quote objects
    '''


    def __init__(self,author,quote):
        self.author = author
        self.quote = quote
