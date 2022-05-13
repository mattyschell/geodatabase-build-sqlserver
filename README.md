# geodatabase-build-sqlserver

We will create an ESRI Enterprise Geodatabase on SQL Server.  Friends, this our ESRI Enterprise Geodatabase on SQL Server, our rules, the trick is never to be afraid.

Big facts:

* We prefer Windows authentication but support SQL Server authentication  
* We create dbo-schema geodatabases, not sde-schema geodatabases [pros, cons](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/comparison-geodatabase-owners-sqlserver.htm)
* We connect Active Directory groups to database users and schemas.  


## Tasks

* Install SQL Server (optional, for local development)
* As sysadmin Create the database and ESRI Enterprise Geodatabase 
* Create ESRI Geodatabase data owners as needed


## Install SQL Server 

See [How Do I SQL Server](https://github.com/mattyschell/geodatabase-build-sqlserver/blob/main/doc/README.md)


## Create the database

Perform these steps to create a facsimile development environment database. Set the first environmental to the database to be created and the 4 SQLCMD environmentals based on your local install.  

```bat
>set DBNAME=gisxdb
>set SQLCMDSERVER=localhost\POTATO
>set SQLCMDDBNAME=master
>set SQLCMDUSER=sa
>set SQLCMDPASSWORD=postgisismydatabae!
>setup.bat
```


## Create the Enterprise Geodatabase

Here are the [ESRI docs](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/setup-geodatabase-sqlserver.htm#GUID-4CA44E01-D866-4561-A2E5-FAD424AD9ECD)

> set SDEFILE=X:\yyy\\Connections\sqlserver\dev\gisxdb\schell_private\mschell.sde
> set AUTHFILE=XX:\GIS\Internal\Connections\oracle19c\dev\GIS-ditGSdv1\mschell_private\keycodes
> set ARCPY2PATH=C:\Python27\ArcGIS10.7
> enablegdb.bat

## Create Users

https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/add-users-sqlserver.htm











