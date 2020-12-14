from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Hobbies','Hobbies'),('Experiences','Experiences'),('Skills','Skills')],validators=[Required()])
    post = TextAreaField('Your Post...', validators=[Required()])
    post_pic_path = StringField('Upload image url...')
    submit = SubmitField('Save')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment here',validators=[Required()])
    submit = SubmitField('Comment')

class UpdatePostForm(FlaskForm):   
    title = StringField('Title', validators=[Required()])
    category = SelectField('Category', choices=[('Hobbies','Hobbies'),('Experiences','Experiences'),('Skills','Skills')],validators=[Required()])
    post = TextAreaField('Your post...', validators=[Required()])
    post_pic_path = StringField('Upload image url...')
    submit = SubmitField('Save')

