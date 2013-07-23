# -*- coding: utf-8 -*-
# Felipe Bandeira da Silva
# Fortaleza-CE, 29/06/2013
# felipeband18@gmail.com
# graduando em Engenharia Elétrica

from uuid import getnode as get_mac
import smtplib
from getpass import getuser
import time

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

if __name__ == '__main__':

  msg = """
  Data = %s
  Usuario = %s
  MAC = %s
  """ % (time.ctime(), getuser(), str(get_mac()))

  print 'Enviando...'

  try:
    sendemail(from_addr    = 'felipeband18@gmail.com',
              to_addr_list = ['felipeband18@gmail.com'], 
              cc_addr_list = [''], 
              subject = 'endereco mac', 
              message = msg,  
              login = 'felipeband18@gmail.com',  
              password = 'fbsilva19830991fe1983ba')
  except:
    print 'Erro'
  print 'Processo finalizado'

  
  a = raw_input('[ENTER] para sair')
