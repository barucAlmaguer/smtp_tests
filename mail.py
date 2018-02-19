import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from usernpass import username, password, sender, recipient

class MailSender:
    def __init__(self):
        self.text = ""
        self.subject = None
        self.sender_mail = None
        self.sender_name = None
        self.recipient = None
        #datos smtp2go
        self.smtp2go_user = username
        self.smtp2go_pass = password
    def setSubject(self, sub):
            self.subject = sub
    def setSenderName(self, sn):
        self.sender_name = sn
    def setSenderMail(self, sm):
        self.sender_mail = sm
    def setRecipient(self, rec):
        self.recipient = rec
    def setText(self, text):
        self.text = text
    def appendText(self, text):
        if len(text) == 0:
            self.text = text
        else:
            self.text += "\n" + text
    def sendMail(self):
        #genera encabezados
        print("\tenlazando encabezados a correo...")
        msg = MIMEMultipart('mixed')
        msg['Subject'] = self.subject
        if self.sender_name is not None:
            msg['From'] = "{} <{}>".format(self.sender_name, self.sender_mail)
        else:
            msg['From'] = self.sender_mail
        msg['To'] = self.recipient
        #enlaza mensaje
        text_message = MIMEText(self.text, 'plain')
        msg.attach(text_message)
        print("\tiniciando envio de correo a nombre de {}...".format(sender))
        #envia mail
        mailServer = smtplib.SMTP('mail.smtp2go.com', 2525) # 8025, 587 and 25 can also be used.
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.smtp2go_user, self.smtp2go_pass)
        mailServer.sendmail(self.sender_mail, self.recipient, msg.as_string())
        mailServer.close()
        print("\tenvio de correo finalizado")



def send_mail(_sender = None, _recipient = None, _subject = "", _text = ""):
    msg = MIMEMultipart('mixed')
    msg['Subject'] = _subject
    msg['From'] = _sender if _sender is not None else sender
    msg['To'] = _recipient if _recipient is not None else recipient

    text_message = MIMEText(_text, 'plain')
    msg.attach(text_message)
    mailServer = smtplib.SMTP('mail.smtp2go.com', 2525) # 8025, 587 and 25 can also be used.
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(username, password)
    mailServer.sendmail(sender, _recipient, msg.as_string())
    mailServer.close()

if __name__ == "__main__":
    m = MailSender()
    print("Generando encabezados del correo...")
    m.setSenderName("Baruquillo")
    m.setSenderMail("baruc.almaguer@gmail.com")
    m.setRecipient("baruc@disruptiveangels.com")
    m.setSubject("Phishing baruc")
    m.setText("Probando 1 2 3")
    m.appendText("2da linea")
    m.appendText("3ra linea")
    m.appendText("4ta linea")
    print("Enviando correo...")
    m.sendMail()
