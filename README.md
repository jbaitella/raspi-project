# raspi-project

Meine Idee war es ein Spiel zu Programmieren, welches mit dem Gesture Sensor gesteuert werden kann. 
Dazu habe ich mich für das Spiel "PacMan" entschieden, da dieses nur 4 Bewegungsmöglichkeiten hat, 
welche mit dem Gesture Sensor umzusetzen sind. 

Material: 
- Raspberry pi
- Grove Gesture Sensor
- evt. ein Display

Ablauf um Spiel zu starten: 
1. Display am Raspberry pi anschliessen 
  (wenn kein Display zur verfügung steht, kann das Spiel auch auf dem Remotedesktop gespielt werden)
2. Grove Gesture Sensor an Port 12C-3 anschliessen
3. Grove Gesture Sensor so Ausrichten, das "INT"Oben Links in der Ecke steht. 
4. Spiel laufen lassen: main.py starten => Fenster wird geöffnet mit START/ABOUT/EXIT
5. Spiel beginnen (Hand zum Senosr bewegen)
6. PacMan (der Gelbe Kreis) durch Gesten (rauf, runter, link, rechts) Steuern

Ziel des Spieles: 
Als PacMan (der Gelbe Kreis) möglichst viele Punkte im Spiel zu fressen und dabei nicht von den roten Montstern berührt zu werden. 
Das Spiel ist vorbei, sobald PacMan von einem Monser gefressen wird .

 

