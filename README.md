# Seminararbeit: GO
___
## INFO
___

    
## REGELN
___
### SPIEL
    Go ist ein Spiel für zwei Spieler, genannt Schwarz und Weiß.Go ist ein Spiel für zwei Spieler, genannt Schwarz und Weiß.
    Das Spielbrett ist ein Gitter aus 19 horizontalen und 19 vertikalen Linien, die 361 Schnittpunkte bilden. Das ist meist
    ein Gitter schwarzer Linien auf einem Holzbrett. Zur optischen Orientierung, aber ohne Bedeutung für den Spielverlauf,
    sind einige Schnittpunkte durch etwas fettere Punkte markiert (Hoshis). Auf diese werden bei einer Vorgabepartie die
    Vorgabesteine gesetzt. Ein Brett der Größe 19×19 ist der Standard. Es kann jedoch auch auf Brettern anderer Größen
    gespielt werden, zum Beispiel 9×9 oder 13×13. Die Regeln sind für alle Brettgrößen gleich.
    https://de.wikipedia.org/wiki/Go-Regeln (15.08.23)

### ABLAUF
    Auf das zunächst leere Spielfeld legt zuerst Schwarz, dann Weiß und Schwarz abwechselnd jeweils einen Spielstein ihrer
    Farbe auf einen freien Schnittpunkt oder passen.

### GRUPPEN & LIBERTIES
    Die Gruppe ist wie folgt definiert:
    - jeder Stein auf dem Brett gehört zu genau einer Kette
    - zwei Steine mit gleicher Farbe auf benachbarten Schnittpunkten gehören zur selben Kette
    - verschiedenfarbige Steine gehören zu verschiedenen Ketten
    - zwei gleichfarbige Steine, zwischen denen es keine Verbindung über sämtlich von Steinen dieser Farbe besetzte
      Schnittpunkte gibt, gehören zu verschiedenen Ketten
    Die Nachbarschaft der Schnittpunkte wird durch die Linien des Bretts vermittelt, darum können Steine nur horizontal oder
    vertikal benachbart sein, jedoch nicht diagonal.

    Die Liberties einer Gruppe sind leere Schnittpunkte, die zu einem Stein der Kette benachbart sind. Besteht eine Gruppe
    beispielsweise nur aus einem einzelnen Stein, so kann sie bis zu vier Liberties haben, da in der Brettmitte jeder 
    Schnittpunkt vier Nachbarpunkte hat, während ein Stein am Rand drei und ein Stein in der Ecke nur zwei Nachbarpunkte
    hat.

### SCHLAGEN
    Wenn es nach dem Setzen eines Steins gegnerische Gruppen ohne Freiheit gibt, dann werden deren Steine vom Brett
    entfernt. Dieses Entfernen ist Bestandteil des Zugs. Wenn es auch eigene Steine ohne Freiheit gibt, werden diese nicht
    entfernt. Es kann vorkommen, dass es nach dem Setzen eigene Steine ohne Freiheit gibt, während alle gegnerischen Steine
    noch eine Freiheit haben (Stichwort: Selbstmord). Ein solches Setzen nicht erlaubt.

### KŌ & SELBSTMORD
    Um endlose Wiederholungen zu unterbinden oder sinnlos zu machen, wird Stellungswiederholung eingeschränkt. Zwei 
    aufeinander folgende Züge (außer Passen) dürfen nicht die ursprüngliche Stellung wiederherstellen(Kō).

    Ein Zug ist verboten, wenn dadurch eigene Steine geschlagen werden würde.

### BEWERTUNG
    Das alternierende Ziehen endet entweder, wenn ein Spieler passt und dann sogleich der andere Spieler auch passt, oder
    wenn ein Spieler keinen Zug mehr machen kann.

___
