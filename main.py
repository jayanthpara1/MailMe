import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(recipient_email, name, internship_name, pdf_path):
    # Email credentials
    sender_email = "iamnotahuman1990@gmail.com"
    password = "holicow22"  # Consider using an app password for security

    # Create the email content from the template
    with open('mail_template.txt', 'r') as file:
        template = file.read()
    
    body = template.replace('<name>', name).replace('<internship_name>', internship_name)

    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Internship Information"

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_attachment = MIMEApplication(pdf_file.read(), _subtype='pdf')
            pdf_attachment.add_header('Content-Disposition', 'attachment', filename='internship_details.pdf')
            msg.attach(pdf_attachment)
    except Exception as e:
        print(f"Error attaching PDF: {e}")
        return

    # Send the email
    try:
        # Connect to the Gmail SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(sender_email, password)  # Login to your email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    recipient_name = input("Enter the recipient's name: ")
    recipient_email = input("Enter the recipient's email: ")
    internship_name = input("Enter the internship name: ")
    pdf_path = input("Enter the path to the PDF file: ")

    send_email(recipient_email, recipient_name, internship_name, pdf_path)
