from flask import Flask, render_template, request
import ssl
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        disease = request.form['disease']
        address = request.form['address']
        mood = request.form['mood']
        stress_level = request.form['stress_level']
        sleep_pattern = request.form['sleep_pattern']
        other_indicator = request.form['other_indicator']
        gender = request.form['gender']
        assigned_doctor_id = request.form['assigned_doctor_id']

        # Here you can send an email to the assigned doctor based on the assigned_doctor_id
        # Example:
        doctors_emails = {
            'd1': 'johnwycliffe1874@gmail.com',
            'd2': 'abinatha_23eca03@kgkite.ac.in',
            'd3': 'indira_23eca43@kgkite.ac.in',
            'd4': 'abirami_23eca07@kgkite.ac.in',
            'd5': 'abinaya_23eca04@kgkite.ac.in'
        }

        assigned_doctor_email = doctors_emails.get(assigned_doctor_id)

        if assigned_doctor_email:
            send_email(assigned_doctor_email, disease, address, mood, stress_level, sleep_pattern, other_indicator, gender)
            return render_template('task_completed_2.html')  # Render task_completed_2.html after successful form submission
        else:
            return 'Error: Assigned doctor not found.'

def send_email(doctor_email, disease, address, mood, stress_level, sleep_pattern, other_indicator, gender):
    # Email configuration
    email_sender = "abik0602@gmail.com"
    email_password = "qwwj snro uaix durj"

    subject = "New Patient Data"
    body = f'Disease: {disease}\nAddress: {address}\nMood: {mood}\nStress Level: {stress_level}\nSleep Pattern: {sleep_pattern}\nOther Indicators: {other_indicator}\nGender: {gender}'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = doctor_email
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, doctor_email, em.as_string())

if __name__ == '__main__':
    app.run(debug=True)
