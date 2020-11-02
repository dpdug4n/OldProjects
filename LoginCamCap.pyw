#set to trigger via login event on Windows Viewer

import cv2, time, email, smtplib, ssl
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#get video & picture of user logging in
Time = str(datetime.now())
video_capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
UserLoggingIn = cv2.VideoWriter('capture.avi',fourcc, 20.0, (640,480), True)

check, frame = video_capture.read()
cv2.imwrite('capture.png', frame)
video_capture.release()

for _ in range(60):
    check, frame = video_capture.read()
    UserLoggingIn.write(frame)
    cv2.waitKey(1)
    time.sleep(.25)

video_capture.release()
UserLoggingIn.release()


#send video to security account via email
#set headers
message = MIMEMultipart()
message["From"] = '<email>'
message["To"] = '<email>'
message["Subject"] = Time
#attach video file
message.attach(MIMEText("Someone logged in.", "plain"))
filename = ['capture.png','capture.avi']
for _ in filename:
    with open(_, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {_}",
    )
    message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login('<email>', '<password>' )
    server.sendmail('<email>', <email>', text)
