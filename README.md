# geodatabase-build-sqlserver

We will create an ESRI Enterprise Geodatabase on SQL Server.  Friends, this our ESRI Enterprise Geodatabase on SQL Server, our rules, the trick is never to be afraid.

Big facts:

* We prefer Windows authentication for users and support SQL Server authentication for applications
* We create dbo-schema geodatabases, not sde-schema geodatabases ([pros, cons](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/comparison-geodatabase-owners-sqlserver.htm))
* We mainly grant access to SQL Server databases from Active Directory groups to individual database user schemas.  


## Tasks

* Install SQL Server (optional, for local development)
* As sysadmin create the database and ESRI Enterprise Geodatabase 
* Create ESRI Enterprise Geodatabase data owners as needed


## Install SQL Server 

See supplemental readme [How Do I SQL Server](https://github.com/mattyschell/geodatabase-build-sqlserver/blob/main/doc/README.md)


## Create an Enterprise Geodatabase

Requires a system administrator connection. Set the first environmental to the database you wish to create. Here are the [ESRI docs](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/setup-geodatabase-sqlserver.htm#GUID-4CA44E01-D866-4561-A2E5-FAD424AD9ECD)


```bat
>set DBNAME=XXX_yyyyyy_Zzz
>set AUTHFILE=C:\xxx\keycodes
>set SQLCMDSERVER=localhost\POTATO
>set SQLCMDDBNAME=master
>set SQLCMDUSER=sysadminuser
>set SQLCMDPASSWORD=postgisismydatabae!
>setup.bat %SQLCMDSERVER% %DBNAME% %AUTHFILE%
```


## Create Users - Local Dev 

[ESRI's user creation tools](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/add-users-sqlserver.htm) must be run by system administrators which we don't expect to have access to in production systems. When planning a systematic approach to data management in ESRI Enterprise Geodatabases on SQLServer know that:

* All users must have a schema
* User names and schema names must be identical

We'll expect read-only and ad hoc users to connect to Enterprise Geodatabases in SQL Server with Windows groups (ex domain\jdoe).  If necessary these users will create data under wretched auto-created schemas like "domain\jdoe.countyboundaries."

On a local development PC create a mock login, user, and schema with dummy password PostGISIsMyDatabae! here:


```bat
>set DBUSER=depravedapplication
>set DBNAME=XXX_yyyyyy_Zzz
>set SQLCMDSERVER=localhost\POTATO
>set SQLCMDDBNAME=master
>set SQLCMDUSER=sysadminuser
>set SQLCMDPASSWORD=postgisismydatabae!
>createuser.bat 
```

## Create Users On Real Infrastrucutre

When system admins provide new logins on a server and database we must complete additional steps to make the new login ready for ESRI. Don't be afraid to click to success in SQL Server Management Studio, this is the way.


If you have just created the enterprise geodatabase, first map logins to users

1. From the top level expand "Security"
2. Expand "Logins"
3. Double click a login and select the "User Mapping" page
4. Map the login to the database and a user with the same name
5. Leave default schema as dbo or empty for now

 As DBO or sysadmin:

1. Under the database name expand "Security"
2. Right click on "Schemas" and select "New Schema" 
3. Enter a schema name that matches the login name.  
4. Make the new login the schema owner.  Use the Search box to be sure it is good.

If the DBO user is sysadmin or has permission to alter other logins:

5. Under the server expand "Security" and "Logins"
6. Right click the login, select "Properties"
7. Select the "User Mapping" page
8. Verify that the new login is mapped to the database
9. Change the default schema mapping to the new schema with the same name as the user
10. Under "database role membership" for the selected database check db_owner

If the admin user does not have permission, connect as the new login

5. Under the server expand "Security" and "Logins"
6. Right click on the current login, probably the only one visible, select properties
7. Select the "User Mapping" page
8. Verify that the new login is mapped to the database
9. Change the default schema mapping to the new schema with the same name as the user
10. (if possible) Under "database role membership" for the selected database check db_owner

























