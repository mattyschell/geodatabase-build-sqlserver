set PROPY=c:\Progra~1\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe
echo tearing down %DBNAME% if it exists
CALL sqlcmd -i src\main\teardown.sql
echo. creating Enterprise Geodatabase %DBNAME% 
CALL %PROPY% .\src\main\py\create_gdb.py %SQLCMDSERVER% %DBNAME% %AUTHFILE%
set SQLCMDDBNAME=%DBNAME% 
CALL sqlcmd -i src\test\test_setup.sql -o src\test\test_setup.txt
fc src\test\test_setup_expected src\test\test_setup.txt > nul
if errorlevel 1 (
    echo. something went wrong
) else (
    echo. success!
)
