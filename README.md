# geodatabase-build-sqlserver

We will create an ESRI Enterprise Geodatabase on SQL Server.  Friends, this our ESRI Enterprise Geodatabase on SQL Server, our rules, the trick is never to be afraid.

Big facts:

* We prefer Windows authentication but support SQL Server authentication  
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


## Create Users

[ESRI create user tools](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/add-users-sqlserver.htm) must be run by system administrators which we shouldn't expect in production systems. When planning a more systematic approach to data management in Enterprise Geodatabases on SQLServer know that:

* All users must have a schema
* User names and schema names must be identical

We'll expect read-only and ad hoc users to connect to Enterprise Geodatabases in SQL Server via Windows groups (ex domain\jdoe).  If necessary these users will create data under wretched auto-created schemas like "domain\jdoe.countyboundaries."

For more formal data management create a development environment user and schema using this.























