CALL sqlcmd -i src\main\teardown.sql
CALL c:\Progra~1\ArcGIS\Pro\bin\Python\scripts\propy.bat .\src\main\py\create_gdb.py %SQLCMDSERVER% %DBNAME% %AUTHFILE%
REM A TEST HERE WOULD BE GOOD