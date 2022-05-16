# geodatabase-build-sqlserver

We will create an ESRI Enterprise Geodatabase on SQL Server.  Friends, this our ESRI Enterprise Geodatabase on SQL Server, our rules, the trick is never to be afraid.

Big facts:

* We prefer Windows authentication but support SQL Server authentication  
* We create dbo-schema geodatabases, not sde-schema geodatabases [pros, cons](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/comparison-geodatabase-owners-sqlserver.htm)
* We link Active Directory groups to database users and schemas.  


## Tasks

* Install SQL Server (optional, for local development)
* As sysadmin create the database and ESRI Enterprise Geodatabase 
* Create ESRI Enterprise Geodatabase data owners as needed


## Install SQL Server 

See supplemental readme [How Do I SQL Server](https://github.com/mattyschell/geodatabase-build-sqlserver/blob/main/doc/README.md)


## Create an Enterprise Geodatabase

Perform these steps to create a facsimile development environment database. Set the first environmental to the database you wish to create.

Here are the [ESRI docs](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/setup-geodatabase-sqlserver.htm#GUID-4CA44E01-D866-4561-A2E5-FAD424AD9ECD)


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

https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/add-users-sqlserver.htm











