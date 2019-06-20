import smtplib
toemail=input("Enter the receiver mail_id:")
msg=input("Enter the message:")
#tomail="arjun.sayonetech@gmail.com"
try:
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('shelson.sayonetech@gmail.com','*****')
    #content={subject:}
    mail.sendmail('shelson.sayonetech@gmail.com',toemail,msg)
    mail.close()
except Exception as e:
    print(str(e))
