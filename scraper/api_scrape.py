import requests
import xlwt
# import csv
from xlwt import Workbook
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from constants import MY_PASS

BASE_URL = "https://remoteok.com/api"
REQUEST_HEADER = {
    'Accept-language': 'en-US, en;q= 0.5',
}
def get_responses():
    response = requests.get(BASE_URL, headers = REQUEST_HEADER)
    return response.json()

def head_sheet(data):
    wb = Workbook()
    job_sheet = wb.add_sheet('Jobs')
    headers = list(data[0].keys())

    for i in range(0, len(headers)):
        job_sheet.write(0, i, headers[i])
    # wb.save('Jobs.xls')

    for i in range(0, len(data)):
        job = data[i]
        values = list(job.values())
        for x in range(0, len(values)):
            job_sheet.write(i+1, x, values[x])
    wb.save('Jobs.xls')

def send_mails(send_from, send_to, subject, text, attach_files = None):
    # assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['from'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime= True)
    msg['subject'] = subject
    msg.attach(MIMEText(text))

    for i in attach_files or []:
        with open(i, 'rb') as fil:
            part = MIMEApplication(fil.read(), Name = basename(i))
        part['Content-Disposition'] = f'attachment; filename = "{basename(i)}"'
        msg.attach(part)
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(send_from, MY_PASS)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()




if __name__ == "__main__":
    json = get_responses()[1:]
    head_sheet(json) 
    send_mails('abdulkabirbadru@gmail.com', 'abdulkabiropeyemi7@gmail.com', 'Job Postings','Please, find the attached for your reference', attach_files= [r"C:\Users\Kaybee\Videos\py_automation\scraper\Jobs.xls"])