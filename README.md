# raspi-project

Das Ziel dieses Projekts war es ein Spiel zu programmieren, welches ausschliesslich
mit dem Gesture Sensor gesteuert werden kann. Dazu habe ich mich für das Spiel "PacMan"
entschieden, da dieses nur vier Bewegungsmöglichkeiten hat, welche mit dem Gesture Sensor 
umzusetzen sind. 

Material: 
- Raspberry Pi
- Grove Gesture Sensor
- evt. ein Display
- evt. Kopfhörer mit Kabel


Ablauf um das Spiel zu starten: 
1. Display am Raspberry pi anschliessen & Kopfhörer anstecken
  (wenn kein Display zur verfügung steht, kann das Spiel auch auf dem 
  Remotedesktop gespielt werden)
2. Grove Gesture Sensor an Port 12C-3 anschliessen
3. Grove Gesture Sensor so ausrichten, dass "INT" oben links in der Ecke steht
4. Spiel laufen lassen: main.py starten => Fenster wird geöffnet mit START/ABOUT/EXIT
5. Spiel beginnen: Hand zum Senosor hinbewegen
6. PacMan (der gelbe Kreis) durch Gesten (rauf, runter, link, rechts) steuern 

Viel Spass!

Ziel des Spieles: 
Als PacMan (der gelbe Kreis) möglichst viele Punkte im Spiel zu fressen und dabei nicht von den roten "Monstern" berührt zu werden. Der Score wird dabei während dem Spiel links Oben angezeigt. 
Das Spiel ist vorbei, sobald PacMan von einem Monster gefressen wird, sobald das passiert, explodiert PacMan und man gelangt zurück zum Menu. 



Das Grundgerüst des Spieles habe ich von einer Website:
https://itsourcecode.com/free-projects/python-projects/pacman-in-python-code/
Diesen Code habe ich versucht auf den Gesture Sensor anzupassen und zu vereinfachen um das Spiel möglichst gut spielen zu können.  

