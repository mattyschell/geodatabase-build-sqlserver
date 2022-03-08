# geodatabase-build-sqlserver

We will enable an ESRI Enterprise Geodatabase on SQL Server.  Friends, this our ESRI Enterprise Geodatabase on SQL Server, our rules, the trick is never to be afraid.

Big facts.  We will:

* Not be granted sysadmin in all environments
* Support geodatabases in cloud providers
* Not always have Windows authentication for ourselves or our users  
* Create sde-schema geodatabases, not dbo ([pros, cons](https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/comparison-geodatabase-owners-sqlserver.htm)


## Tasks

* Install SQL Server (for local development work)
* Create the database and perform SQL Server admin tasks
* Enable the ESRI Enterprise Geodatabase 

## Install SQL Server 

See [How Do I SQL Server](https://github.com/mattyschell/geodatabase-build-sqlserver/blob/main/doc/README.md)

## Create the database and perform SQL Server sysadmin tasks


1. Create the database
2. Set READ_COMMITTED_SNAPSHOT and ALLOW_SNAPSHOT_ISOLATION to ON
3. Create sde login and map sde to the database
4. Create an sde schema and make it the default of the sde user
5. Verify

Set environmentals.  Skip SQLCMDUSER and SQLCMDPASSWORD when using windows authentication.

```bat
>set SQLCMDSERVER=localhost\POTATO
>set SQLCMDDBNAME=master
>set SQLCMDUSER=sa
>set SQLCMDPASSWORD=postgisismydatabae!
>sqlcmd -v dbname ="xxx_yyyy001_zzz" -i src\main\teardown.sql
>sqlcmd -v dbname ="xxx_yyyy001_zzz" -i src\main\database.sql

```


## Enable the Enterprise Geodatabase











