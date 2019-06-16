import requests,smtplib,time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
r =requests.get('https://www.codechef.com/JUNE19B/')
while(1):
    if('(Challenge)' in r.text):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sender_gmail_id", "password")
        msg= MIMEMultipart("alternative")
        msg["Subject"]="Challenge Problem added"
        msg["From"]="sender_gmail_id"
        msg["To"]="receiver_gmail_id"
        text="I guess challenge problem is added in long challenge,check it on codechef."
        html="<h4>I guess challenge problem is added in long challenge,check it on codechef.</h4><br/><a href='https://www.codechef.com/'>Click here to visit. </a>"
        msg.attach(MIMEText(html, "html"))
        s.sendmail("sender_gmail_id","receiver_gmail_id",msg.as_string())
        s.quit()
        print('sent')
        break
    print('Sleeping...')
    time.sleep(3600)
    print('Trying again...')
