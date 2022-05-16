import os
import sys
import arcpy

class Gdb(object):

    def __init__(self
                ,server
                ,database):

        self.platform = 'SQL_Server' 
        self.server   = server
        self.database = database

    def create(self
              ,dbadmin
              ,pdbadmincreds
              ,authfile):
            
        try:
            out = arcpy.management.CreateEnterpriseGeodatabase(self.platform
                                                              ,self.server
                                                              ,self.database
                                                              ,'DATABASE_AUTH'
                                                              ,dbadmin
                                                              ,pdbadmincreds
                                                              ,'DBO_SCHEMA'
                                                              ,'' #gdb_admin_name
                                                              ,'' #gdb_admin_password
                                                              ,'' #tablespace_name
                                                              ,authfile)
        
        except:
            print ("{0}".format(arcpy.GetMessages()))
            print ("using {0} and {1}".format(self.sdeconn,
                                              authfile))
            raise ValueError('Failure on enable enterprise gdb from ArcGIS')
        
        print ("".format(arcpy.GetMessages()))

        if out:
            return 0
        else:
            return 1

if __name__ == '__main__':

    pdbadmin      = os.environ['SQLCMDUSER']
    pdbadmincreds = os.environ['SQLCMDPASSWORD']

    pserver   = sys.argv[1]
    pdatabase = sys.argv[2]
    pauthfile = sys.argv[3]

    babygdb = Gdb(pserver
                 ,pdatabase)

    try: 
        outp = babygdb.create(pdbadmin
                             ,pdbadmincreds
                             ,pauthfile)
    except:
        outp = 1

    exit(outp)

