from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from models import mailcamp_template_list
class addCampaign(FlaskForm):
    campaign_name = StringField('Campaign name', validators=[DataRequired(), Length(max=16)])
    user_group = SelectField(validators= [DataRequired()])