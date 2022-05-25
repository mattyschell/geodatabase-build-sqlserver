USE [$(dbname)]
GO

CREATE USER [$(dbuser)] FOR LOGIN [$(dbuser)] WITH DEFAULT_SCHEMA=[$(dbuser)]
GO

EXEC sp_addrolemember 'db_ddladmin', [$(dbuser)] 
GO

