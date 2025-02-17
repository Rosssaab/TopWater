import os

class Config:
    SECRET_KEY = 'TopWater2024SecretKey'  # You can change this if you want
    
    # Mail Settings for One.com
    MAIL_SERVER = 'send.one.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True  # Note: Using SSL instead of TLS for port 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'info@topwater.uk'
    MAIL_PASSWORD = '1LoveDad#'  # Replace with your actual email password
    MAIL_DEFAULT_SENDER = 'info@topwater.uk'
    
    # IMAP settings
    IMAP_SERVER = 'imap.one.com'
    IMAP_PORT = 993
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///topwater.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 