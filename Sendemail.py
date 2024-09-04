import sys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_with_attachment(to_email, attachment_path):

    SMTP_SERVER = 'smtp.gmail.com'  # Example: Gmail SMTP server
    SMTP_PORT = 587
    EMAIL = 'jashandeepgarry2003@gmail.com'  # Replace with your email address
    PASSWORD = 'ksvq hqvu oxlp psts'  # Replace with your email password or app password

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_email
    msg['Subject'] = 'Zipped Images Attached'

    # Attach the body of the email
    body = 'Please find the attached ZIP file containing the images.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the ZIP file
    with open(attachment_path, 'rb') as f:
        part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
        msg.attach(part)

    # Send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

    print(f"Email sent to {to_email} with attachment {attachment_path}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python send_zip_email.py <input_zip_file> <email_address>")
        return

    input_zip_file = sys.argv[1]
    email_address = sys.argv[2]

    # Validate input zip file
    if not (os.path.isfile(input_zip_file) and input_zip_file.lower().endswith('.zip')):
        print(f"Error: {input_zip_file} is not a valid ZIP file.")
        return

    # Send the ZIP file via email
    send_email_with_attachment(email_address, input_zip_file)

if __name__ == "__main__":
    main()
