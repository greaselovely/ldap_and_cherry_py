#!/usr/bin/python3

# I updated the /etc/openldap/ldap.conf with the BASE and URI for this test.


import sys
import subprocess
from subprocess import Popen as run
from subprocess import check_output
from subprocess import Popen, PIPE


search = "ldapsearch -x -LLL uid=username"
search = search.split(' ')

admingrp = "ldapsearch -x -LLL -b cn=groups,dc=ss-syn-01,dc=pants,dc=com uid"
admingrp = admingrp.split(' ')

pipe = Popen(admingrp, stdout=PIPE)
output = pipe.communicate()[0]

output = output.decode('utf-8')
output = output.split('\n')

del output[:3]

for i in output:
    print(i)

