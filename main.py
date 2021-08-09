import ldap3
from ldap3 import ALL

server = ldap3.Server('1.2.3.4', get_info=ALL)
password = 'ThxforAllTheFish!'
baseDN = 'dc=ss-syn-01,dc=pants,dc=com'
bindDN = 'uid=root,cn=users,' + baseDN
groupDN = 'cn=groups,' + baseDN
objectclassTypes = ['top', 'person', 'posixAccount', 'organizationalPerson', '*']

conn = ldap3.Connection(server, bindDN, password, auto_bind=True)

#server.schema

for type in objectclassTypes:
    try:
        conn.search(baseDN, '(&(objectclass=' + type + '))')
        entries = conn.entries
    except ldap3.core.exceptions.LDAPInvalidFilterError as e:
        print(e, conn.search)

print(entries[::-1])
