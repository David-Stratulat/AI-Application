@echo off
echo Trimitem datele catre server...

curl -X POST http://127.0.0.1:5000/add_product/ ^
     -H "Content-Type: application/json" ^
     -d "{\"name\":\"Monitor\", \"price\":700}"

echo.
echo Operatiune finalizata.
pause