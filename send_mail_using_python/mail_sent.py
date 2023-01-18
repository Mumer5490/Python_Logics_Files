def all_continue():
    pass
# Python code to illustrate Sending mail from
# your Gmail account
    import smtplib as s

    # creates SMTP session
    obj=s.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    obj.starttls()

    # Authentication
    obj.login("muhammadumer5490@gmail.com", "tzrftriwynljpwam")  #stqgskhnzphyysju ya google account sy generate kia 
    # gia hai password hai.
    #  sb sy phy new tab pr jay gy us k bad right side pr google app pr ja kr create kry gy
    subject="Mail with Admin"   # ya commant b must hai
    body="Water indicator Alert!"  # ya commant b must hai
    message = "subject:{}\n\n{}".format(subject,body)   # ya commant b must hai
    listofadress=["ranaumaradvocate521@gmail.com"]

    # sending the mail
    obj.sendmail("muhammadumer5490@gmail.com",listofadress,message)
    print('send succfullly')

    # terminating the session


all_continue()


