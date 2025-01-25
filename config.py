import os

class Config:
    SECRET_KEY = 'your-secret-key-here'  # Change this to a random string
    
    # Mail Settings for One.com
    MAIL_SERVER = 'send.one.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True  # Note: Using SSL instead of TLS for port 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'info@topwater.uk'
    MAIL_PASSWORD = 'your-email-password'
    MAIL_DEFAULT_SENDER = 'info@topwater.uk'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///topwater.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 