# geodatabase-build-sqlserver

We will enable an ESRI Enterprise Geodatabase on SQL Server.  Friends, this our ESRI Enterprise Geodatabase on SQL Server, our rules, the trick is never to be afraid.

Big facts.  We will:

* Not use sysadmin access in any database
* Plan to primarily build on-premise geodatabases
* Prefer Windows authentication but support SQL Server authentication for some users  
* Create dbo-schema geodatabases, not sde-schema geodatabases [pros, cons](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/comparison-geodatabase-owners-sqlserver.htm)
* Create agency/project Active Directory groups that map to database users and schemas.  


## Tasks

* Install SQL Server (for local development work)
* Create the database and perform SQL Server admin tasks
* Enable the ESRI Enterprise Geodatabase 

## Install SQL Server 

See [How Do I SQL Server](https://github.com/mattyschell/geodatabase-build-sqlserver/blob/main/doc/README.md)


## Create the database and perform SQL Server sysadmin tasks

1. Create the database
2. Create a phony active directory DBO login and map it to DBO on the database
3. Create a user to match the DBO login with default dbo schema

Set environmentals and run setup.  These mimic steps to be performed by the DBAs as syssadmin.  

```bat
>set DBOPASS=iluvesri247
>set DBOLOGIN=gs-dit_yyyy_dbo
>set DBNAME=gisx
>set SQLCMDSERVER=localhost\POTATO
>set SQLCMDDBNAME=master
>set SQLCMDUSER=sa
>set SQLCMDPASSWORD=postgisismydatabae!
>sqlcmd -i src\main\teardown.sql
>sqlcmd -i src\main\database.sql
>sqlcmd -i src\main\login.sql

```


## Enable the Enterprise Geodatabase











