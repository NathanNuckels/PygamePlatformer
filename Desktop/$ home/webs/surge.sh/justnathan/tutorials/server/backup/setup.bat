@echo off
color a
echo this is only 1.12.2 minecraft
pause
echo starting minecraft server...
java -Xmx1024M -Xms1024M -jar server.jar nogui
pause
start eula.txt
echo aggree to the eula.
pause
java -Xmx1024M -Xms1024M -jar server.jar nogui
pause
start server.properites
start http://minecraft.tools/en/motd.php
echo add a server motd
pause
