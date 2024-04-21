from google.auth import impersonated_credentials
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

# def load_credentials(json_file):
#     with open(json_file) as f:
#         credentials_data = json.load(f)
#     return credentials_data

# def authenticate_with_google_api(json_file, scopes):
#     credentials_data = load_credentials(json_file)
#     credentials = service_account.Credentials.from_service_account_info(credentials_data, scopes=scopes)
#     return credentials

# credentials_file = "/credentials/punnett-square-1aa9227aadb2.json"
# scopes = ['https://www.googleapis.com/auth/gmail.send']

# Email configuration
sender_email = "geneticdisorderstest@gmail.com"
password = "thkf lqih wbch bita"
# password = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDJO4FAVEVx0bGq\nwNvV+bMJmzSpfGV+GxTRzIPkCw1en54Am+qW93w1wjW+PgJON/9XaHa+f/3vyRQw\nF9BFrhcP0usdG3WLWil1NACmSrdxIuE38BhnaeLF01M4bZiS1jhsccDol9JjOJAv\nsXtJJtcNLG2TMI0jkKrwTs7QuuOxFL7q+/2BQdThQQcKDdkwEYz5sC4kXeNFDYKq\nKrg0f4subvOnzWNLZajpmlnEfh8agSvYVyvlu6dpqPhSo8ws0ZU0WrS7eQWfp9+K\nYD3M3TJD9lt5z2/DgE7fEb9IBLUE+2cS8KD6wxafzbCYiOVO6VJk4pNwxdg8Bkjw\nFPAlMqe1AgMBAAECggEALNtv33gplsqosSiWmKc1ytFnNtS9BxRgWrgdOmtgSpSI\nMxiOfaKjdJRbSJIoD2maKNDnj2WWpKoNLv9P9QhuqZ9Zu75QQIUTssWp02faZoTg\n8Yg62GqZG4IVDgIYPbs1Dq940iBtzKJiOc91bQQUciJSNrpe6+umvzTCE3NlqCZT\nJhjbP1wdv+lgFzbgrGjtEKaO0A3o6Iwqo7jpzc3P/KHUKKJFPD9crnfA1nNr2rvn\nNV0jpcjZ8JQww/z9GzNjDkXXRyU8P57D+EsEmkNsFGO/mcIQ7rxDMlLTfhuer285\nZzikJHwUJFTBM1KocZjZehZ0KQ7BLadW6TGaHVe/DQKBgQD4AZJJm3SDDq/vyNKh\nb9Xs2FLgHYaNYPKcF5CPJMusvLSesxed31MW8yA5yvY3E2FOxyYmQHb1vClroCqJ\n00UCPZTxDoc7aSSPB7ngrFipDRhIfnue+v50NoawLCfKV8hi2Lf90urXdF6YeThS\nG1ao8v6krVxuHpnnOyhpjPUy4wKBgQDPt/qrC2al2NIIXfhnIReNzuffQBPctVnp\nZVjS4tB0DTdz8l81KPt5uxmZtN6W6Lm86C431YTnn/fFnDSnOpyRiHJcUpEtHie1\niC/+pzhSDccr0jSqD1Vl+h1LnlKyBbY3pqNUyeFQG489jREKAYVTRAPkHh1XUpkS\n9uz+VVaGhwKBgQDf54tLKS5npDrzITwIxA8/ZY5tCDsSKRTgF+ZLVc0MhtIK9WW9\nAoLhlV7iznq7/qM7nFC0+D5uXRKIOHIvPK5w92gguh0dZi+7ch4+2VqyRUBHMuoo\n/jH8eb3gD/1ckSQ5GbADWQjsvAMrZUWT21rB7aA4zMtGIBqSyLYTlU9KQQKBgE4/\nkD4+3Tw8oWJlg93VqXnSJ6cCDHloF6bEduF6b+xHzkvvUc5E0fbZdJtidzeCE/YF\nwONnm9lleYEHhw44FiL8s5fzwpysb2kDFJFpjN3cMttfJFerzw/LWJ3T1nMZk7sD\nGyQlqKr0ttEJAxIx4Hetd4nHjmYGx4NNYZmtrBqhAoGBAIPx6cZA6FFNrD63XJ87\nAHdOcqfqkw2gw3Aeu/r62HdZUHapITm7X1IJ9k4zbS0XPqCf69wa6iqiCcrqwzDB\n6sqdNhC/o+aEsbOLBq/EidYg9tIyQO65T5C7NcEQTnFqfZCMqt94jiXOtFeKyBZp\nSJ2YIdin9iFBqdBIWAdLWlfy\n-----END PRIVATE KEY-----\n"
# sender_email = "geneticdisorderstest@punnett-square.iam.gserviceaccount.com"

def email_results(recipient_email, prob_dict):
    sent = False
    # Create a multipart message
    message = MIMEMultipart()
    # credentials = authenticate_with_google_api(credentials_file, scopes)
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = "Results for Genetic Disorders"
    # Add body to email
    body = parse_dict(prob_dict)
    print(body)

    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.set_debuglevel(1)
        server.starttls()  # Start TLS encryption
        server.ehlo()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        sent = True
    return sent


def parse_dict(prob_dict):
    txt = ''
    for key, value in prob_dict.items():
        txt += 'Probability of the offspring having ' + key + ' is ' + str(value) + '%\n'
    return txt
    