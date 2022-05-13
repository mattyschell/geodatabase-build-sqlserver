# How Do I SQL Server

## Installation on our Government-Issued Windows PC Computers

You will likely be asked to reboot during these steps.

## Install Microsoft ODBC Driver 17 for SQL Server

Microsoft says: "Version 17.9.1 is the latest general availability (GA) version of the 17.x driver. "

ESRI says: "Supported SQL Server clients" are SQL Server 2019 (any version) and Microsoft ODBC Driver 17 for SQL Server

I say: Go [here](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15) and download _Microsoft ODBC Driver 17 for SQL Server (x64)_

## Install SQL Server

1. Go [here](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) and scroll down to _download a free specialized edition_. 
2. Download and install _SQL Server 2019 Developer_
3. Go here [here](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?redirectedfrom=MSDN&view=sql-server-ver15) and install _SQL Server Management Studio_.  


![drakeisthesqlserverofmusic](https://github.com/mattyschell/geodatabase-build-sqlserver/blob/main/doc/sqlserver2019.PNG)


## Install Another Server

This can be helpul when performing development work, or when you (aka me) inevitably forget how to connect to the mess you set up in the past.  For example, you may have set up a server with Windows authentication and would like to compare with mixed mode.

1. Start - Microsoft SQL Server 2019 - SQL Server 2019 Installation Center
2. Select the installation menu
3. Select New SQL Server stand-alone installation

When prompted for installation media point the thing to something like C:\SQL2019\Developer_ENU.  



## sqlcmd: Not great, even if you're into this sort of thing

Test like this:
```bat
C:\Users\mschell>set SQLCMDSERVER=localhost

C:\Users\mschell>set SQLCMDDBNAME=master

C:\Users\mschell>sqlcmd
1> select 1;
2> go

-----------
          1

(1 rows affected)
```

Use a variable in a script.  A file named whywasthe6scared.sql like so:

```
SELECT CONCAT ( 'because ',  $(Numbertest)) AS haha;
```

```bat
C:\Users\mschell>sqlcmd -v NumberTest ="789" -i c:\Temp\whywasthe6scared.sql
haha
--------------------
because 789
```


# How do I ESRI Enterprise Geodatabase

* ArcGIS Pro 2.8
    * https://pro.arcgis.com/en/pro-app/2.8/help/data/geodatabases/manage-sql-server/setup-geodatabase-sqlserver.htm
