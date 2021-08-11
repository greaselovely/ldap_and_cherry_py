import ldap
import ldap.schema

########################################################################
class SchemasIPA(object):

    __ldaps = ldap.schema

    #----------------------------------------------------------------------
    def __init__(self, url):
        """Constructor"""
        ldap._trace_level = 0
        ldap.set_option(ldap.OPT_DEBUG_LEVEL,0)
        subschemasubentry_dn, self.schema = ldap.schema.urlfetch(url,ldap._trace_level)
        self.oc_tree = self.schema.tree(ldap.schema.ObjectClass)        
        self.at_tree = self.schema.tree(ldap.schema.AttributeType)        

    def getobjectclasses(self):
        """
        trae la listas de objectclasses de un servidor dado
        """
        allobjc = {}
        for a in self.oc_tree.keys():
            objc = self.schema.get_obj(ldap.schema.ObjectClass, a)

            if objc != None:
                allobjc[objc.oid] = (objc.names, objc.must, objc.may, objc.sup, objc.obsolete)

olschemas = SchemasIPA(url='ldap://1.2.3.4')

objectclassTypes = ['top', 'person', 'posixAccount', 'organizationalPerson']
for type in objectclassTypes:
    pa = olschemas.schema.get_obj(olschemas._SchemasIPA__ldaps.ObjectClass, 'posixaccount')
    print()
    print('Required Attributes: ', pa.must) #going to print all the attributes that can't be null's
    print('Optional Atributes: ', pa.may) #going to print all the attributes that are optional's
