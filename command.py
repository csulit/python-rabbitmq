#!/usr/bin/env python
from subprocess import PIPE, Popen

sudo_password = '032815'

def cli():
  command = 'ufw status'.split()

  p = Popen(['sudo'] + command, stdin=PIPE, stdout=PIPE, stderr=PIPE,
            universal_newlines=True)
  
  output = p.communicate(sudo_password + '\n')
  
  print(output)
  
  

  

    