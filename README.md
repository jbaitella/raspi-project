# raspi-project

Das Ziel dieses Projektes war es ein Spiel zu Programmieren, welches ausschliesslich
mit dem Gesture Sensor gesteuert werden kann. Dazu habe ich mich für das Spiel "PacMan"
entschieden, da dieses nur vier Bewegungsmöglichkeiten hat, welche mit dem Gesture Sensor 
umzusetzen sind. 

Material: 
- Raspberry Pi
- Grove Gesture Sensor
- evt. ein Display
- evt. Kopfhörer mit Kabel

Ziel des Spieles: 

Als PacMan (den gelben Kreis) möglichst viele Punkte im Spiel zu fressen und dabei nicht von den roten "Monstern" berührt zu werden. Der Score wird dabei während dem Spiel links oben angezeigt. 
Das Spiel ist vorbei, sobald PacMan von einem Monster gefressen (berührt) wird, sobald das passiert explodiert PacMan und man gelangt zurück zum Menu.

Ablauf um Spiel zu starten: 
1. Display am Raspberry Pi anschliessen &  evt. Kopfhörer anstecken
  (wenn kein Display zur verfügung steht, kann das Spiel auch auf dem 
  Remotedesktop gespielt werden)
2. Grove Gesture Sensor an Port 12C-3 anschliessen
3. Grove Gesture Sensor so Ausrichten, das "INT" oben links in der Ecke steht
4. Spiel laufen lassen: main.py starten => Fenster wird geöffnet mit START/ABOUT/EXIT
5. Spiel beginnen: Hand zum Senosor hin bewegen
6. PacMan (der gelbe Kreis) durch Gesten (rauf, runter, links, rechts) steuern

Viel Spass!
 



(Das Grundgerüst des Spieles habe ich von einer Website:
https://itsourcecode.com/free-projects/python-projects/pacman-in-python-code/
Diesen Code habe ich versucht auf den Gesture Sensor anzupassen und zu vereinfachern um das Spiel möglichst gut spielen zu können.)

