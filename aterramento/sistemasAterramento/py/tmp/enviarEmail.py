import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

sendemail(from_addr    = 'felipeband18@gmail.com', 
          to_addr_list = ['felipeband18@gmail.com'],
          cc_addr_list = ['RC@xx.co.uk'], 
          subject      = 'Howdy', 
          message      = 'Howdy from a python function', 
          login        = 'felipeband18@gmail.com', 
          password     = 'fbsilva19830991fe1983ba')
