import os, sys, smtplib, getpass


try:

    W = '\033[0m'  #White
    R = '\033[31m' #Red
    G = '\033[32m' #Green
  
    
    os.system("clear")
  
#!/usr/bin/python
    ye = input("Subscribed to me? (y/n): ")
    if ye == "y":
       subprocess.call("python main.py",shell=True)
    if ye == "n":
         print ("Subscribe to me because i really spent much time on it :D )")
         time.sleep(1)
         os.system("exit")#!/usr/bin/python

    
    
    print (G +              Email-Spammer | Aynaet:Git              )

    server = raw_input ('Mail-Server Gmail/Yahoo: ')

    if server == 'gmail' or server == 'Gmail':

        smtp_server = 'smtp.gmail.com'
        port = 587
        set_server = "gmail"

    if server == 'yahoo' or server == 'Yahoo':

        smtp_server = 'smtp.mail.yahoo.com'
        port = 25
        set_server = "yahoo"

    else:

        print(R + "Error - This script only works on Gmail or Yahoo." + W)
        sys.exit()

    email_user = raw_input('Your Mail: ')
    passwd     = getpass.getpass('Password: ')
    email_to   = raw_input('\nTarget: ')
    subject    = raw_input('Subject: ')
    body       = raw_input('Message: ')
    total      = input('Amount of Sendings (Max 90): ')

    try:

        server = smtplib.SMTP(smtp_server,port) 
        server.ehlo()

        if set_server == "gmail":
            server.starttls()

        server.login(email_user,passwd)

        print("\n\n\n - Target : {} -\n".format(email_to))

        for i in range(1, total+1):

            msg = 'From: ' + email_user + '\nSubject: ' + subject + '\n' + body

            server.sendmail(email_user,email_to,msg)

            print(G + "\rEmail Sent - {}".format(i))

            sys.stdout.flush()

        server.quit()

        print( R + "\n\n-Proccess Terminated-" + W)


    except KeyboardInterrupt:

        print(R + "\nError - Keyboard Interrupt" + W)
        sys.exit()

    except smtplib.SMTPAuthenticationError:

        print( R + "\nError - Authentication error, Are you sure the password or the username is correct?" + W)
        sys.exit()

except smtplib.SMTPAuthenticationError:

    sys.exit()
