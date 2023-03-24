from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from main import login_manager
# database
db = SQLAlchemy()

bcrypt = Bcrypt()



@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	joined = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
	bots = db.Column(db.Integer, default=0)
	mailcamp_user_group = db.relationship('mailcamp_user_group', backref='creator', lazy=True)
	mailcamp_template_list = db.relationship('mailcamp_template_list', backref='creator', lazy=True)
	mailcamp_sender_list = db.relationship('mailcamp_sender_list', backref='creator', lazy=True)
	mailcamp_live = db.relationship('mailcamp_live', backref='creator', lazy=True)
	tb_log = db.relationship('tb_log', backref='creator', lazy=True)

	def __repr__(self):
		return "User('{}')".format(self.username)


# --
# -- Table structure for table `tb_core_mailcamp_user_group`
# --

# CREATE TABLE `tb_core_mailcamp_user_group` (
#   `user_group_id` varchar(111) NOT NULL,
#   `user_group_name` varchar(50) NOT NULL,
#   `user_data` mediumtext DEFAULT NULL,
#   `date` varchar(111) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


class mailcamp_user_group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_group_name = db.Column(db.String(100), unique=False, nullable=False)
    user_data = db.Column(db.String(60), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    owner = db.Column(db.String(120), db.ForeignKey('user.username'), nullable=False)
   
    def __repr__(self):
        return "mailcamp_user_group('{}')".format(self.user_group_name)
    
    
    


# CREATE TABLE `tb_core_mailcamp_template_list` (
#   `mail_template_id` varchar(111) NOT NULL,
#   `mail_template_name` varchar(111) DEFAULT NULL,
#   `mail_template_subject` varchar(1111) DEFAULT NULL,
#   `mail_template_content` mediumtext DEFAULT NULL,
#   `timage_type` tinyint(1) NOT NULL DEFAULT 0,
#   `mail_content_type` varchar(111) DEFAULT '{}',
#   `attachment` varchar(1111) DEFAULT NULL,
#   `date` varchar(111) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;



class mailcamp_template_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mail_template_name = db.Column(db.String(100), unique=True, nullable=False)
    mail_template_subject = db.Column(db.String(100), nullable=False)
    mail_template_content = db.Column(db.String(100), nullable=False)
    timage_type = db.Column(db.String(30), nullable=False)
    mail_content_type = db.Column(db.String(20), nullable=False)
    attachment = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    owner = db.Column(db.String(120), db.ForeignKey('user.username'), nullable=False)
   
    def __repr__(self):
        return "mailcamp_template_list('{}')".format(self.mail_template_name)




# -- Table structure for table `tb_core_mailcamp_sender_list`
# --

# CREATE TABLE `tb_core_mailcamp_sender_list` (
#   `sender_list_id` varchar(111) NOT NULL,
#   `sender_name` varchar(50) NOT NULL,
#   `sender_smtp_server` varchar(50) NOT NULL,
#   `sender_from` varchar(111) NOT NULL,
#   `sender_acc_username` varchar(111) NOT NULL,
#   `sender_acc_pwd` varchar(50) NOT NULL,
#   `auto_mailbox` tinyint(1) NOT NULL DEFAULT 0,
#   `sender_mailbox` varchar(1111) DEFAULT NULL,
#   `cust_headers` varchar(1111) DEFAULT NULL,
#   `dsn_type` varchar(111) DEFAULT NULL,
#   `date` varchar(111) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;



class mailcamp_sender_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100), unique=True, nullable=False)
    sender_smtp_server = db.Column(db.String(60), nullable=False)
    sender_from = db.Column(db.String(111), nullable=False)
    sender_acc_username = db.Column(db.String(111), nullable=False)
    sender_acc_pwd = db.Column(db.String(60), nullable=False)
    auto_mailbox = db.Column(db.Boolean, nullable=False)
    sender_acc_pwd = db.Column(db.String(60), nullable=False)
    sender_mailbox = db.Column(db.String(1111), nullable=False)
    cust_headers = db.Column(db.String(1111), nullable=False)
    dsn_type = db.Column(db.String(111), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    owner = db.Column(db.String(120), db.ForeignKey('user.username'), nullable=False)
   
    def __repr__(self):
        return "mailcamp_sender_list('{}')".format(self.username)
    

# -- Table structure for table `tb_data_mailcamp_live`
# --

# CREATE TABLE `tb_data_mailcamp_live` (
#   `rid` varchar(15) NOT NULL,
#   `campaign_id` varchar(15) DEFAULT NULL,
#   `campaign_name` varchar(50) DEFAULT NULL,
#   `sending_status` tinyint(11) NOT NULL DEFAULT 0,
#   `send_time` varchar(50) DEFAULT NULL,
#   `user_name` varchar(50) DEFAULT NULL,
#   `user_email` varchar(111) DEFAULT NULL,
#   `send_error` varchar(1111) DEFAULT NULL,
#   `mail_open_times` mediumtext DEFAULT NULL,
#   `public_ip` mediumtext DEFAULT NULL,
#   `ip_info` mediumtext DEFAULT NULL,
#   `user_agent` mediumtext DEFAULT NULL,
#   `mail_client` mediumtext DEFAULT NULL,
#   `platform` mediumtext DEFAULT NULL,
#   `device_type` mediumtext DEFAULT NULL,
#   `all_headers` mediumtext DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
    
    
class mailcamp_live(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_name = db.Column(db.String(60), nullable=False)
    sending_status = db.Column(db.Boolean, nullable=False)
    send_time = db.Column(db.DateTime, default=datetime.utcnow(), nullable=True)
    user_name = db.Column(db.String(60), nullable=True)
    user_email = db.Column(db.String(111), nullable=True)
    send_error = db.Column(db.String(1111), nullable=True)
    mail_open_times = db.Column(db.String(100), nullable=True)
    public_ip = db.Column(db.String(60), nullable=True)
    ip_info = db.Column(db.String(60), nullable=True)
    user_agent = db.Column(db.String(60), nullable=True)
    mail_client = db.Column(db.String(60), nullable=True)
    platform = db.Column(db.String(60), nullable=True)
    device_type = db.Column(db.String(60), nullable=True)
    all_headers = db.Column(db.String(60), nullable=True)
    owner = db.Column(db.String(120), db.ForeignKey('user.username'), nullable=False)
   
    def __repr__(self):
        return "mailcamp_live('{}')".format(self.username)





# CREATE TABLE `tb_log` (
#   `id` int(11) NOT NULL,
#   `username` varchar(111) DEFAULT NULL,
#   `log` text DEFAULT NULL,
#   `ip` varchar(55) DEFAULT NULL,
#   `date` varchar(111) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


class tb_log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.String(60), nullable=False)
    ip = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    owner = db.Column(db.String(120), db.ForeignKey('user.username'), nullable=False)
   
    def __repr__(self):
        return "mailcamp_template_list('{}')".format(self.username)


