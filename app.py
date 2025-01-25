from flask import Flask, render_template, flash, redirect, url_for
from flask_mail import Mail, Message
from forms import ContactForm
from config import Config
import smtplib

app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            msg = Message(
                subject=f"TopWater UK Contact: {form.subject.data}",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[app.config['MAIL_USERNAME']],
                reply_to=form.email.data,
                body=f"""
                New message from TopWater UK website:
                
                Name: {form.name.data}
                Email: {form.email.data}
                Subject: {form.subject.data}
                
                Message:
                {form.message.data}
                """
            )
            mail.send(msg)
            
            # Send auto-reply to the user
            auto_reply = Message(
                subject="Thank you for contacting TopWater UK",
                sender=app.config['MAIL_DEFAULT_SENDER'],
                recipients=[form.email.data],
                body=f"""
                Dear {form.name.data},
                
                Thank you for contacting TopWater UK. We have received your message and will get back to you shortly.
                
                Best regards,
                TopWater UK Team
                """
            )
            mail.send(auto_reply)
            
            flash('Your message has been sent successfully! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
            
        except smtplib.SMTPAuthenticationError:
            flash('Error: Could not authenticate with email server. Please try again later or email us directly.', 'danger')
        except smtplib.SMTPException as e:
            flash(f'An error occurred while sending the message. Please try again later.', 'danger')
        except Exception as e:
            flash('An unexpected error occurred. Please try again later.', 'danger')
            app.logger.error(f'Error sending email: {str(e)}')
    
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=8090) 