# M291-2024/2025

# Demo T-Rex-Runner Erweiterungen

## Vorlage aus den Übungen

- https://jsfiddle.net/r_hatz/rh8ma5e3/

## Features

- Spiel startet erst, wenn der Benutzer klickt.
- Alle Animationen gestoppt, wenn das Spiel nicht läuft.
- Hintergrundmusik und Sound Effekte
- Zwei Background Layers, animiert mit unterschiedlicher Geschwindkeit (Parallax Effekt)
- Animierte Spielfiguren mit transparenten GIFs
- Das Hindernis bewegt sich mit zufälliger Geschwindigkeit.

## Weitere Feature Ideen

- Tag/Nacht-Zyklus hinzufügen: Ändern Sie das Hintergrundbild von Tag zu Nacht und umgekehrt. Zum Beispiel, immer wenn 100 Punkte erreicht werden auf Nacht- oder Tag umschalten.
  `gameBox.classList.add("night");`
- Mehr Hindernisse hinzufügen.
- Leben hinzufügen: Erlaubt dem Spieler, mehrere Leben zu haben, bevor das Spiel endet.
- Power-Ups hinzufügen: Power-Ups hinzufügen, die zufällig erscheinen und dem Spieler Vorteile verschaffen.
- Charakteranpassung hinzufügen: Erlaubt den Spielern, verschiedene Charaktere zu wählen.
- Pausen- und Fortsetzungsfunktionalität hinzufügen: Der Spieler kann das Spiel pausieren und fortsetzen.

## Code-Praktiken

- **Kein Inline CSS oder Inline JS**: JavaScript Code muss in `.js` Dateien, CSS-Code in `.css`-Dateien stehen.
- **Keine Code-Duplikate**: In HTML-Dateien darf HTML-Code mehrfach vorkommen (z.B. derselbe Code für Header und Footer). Derselbe CSS- und JS-Code darf jedoch nicht mehrfach vorkommen, weder in derselben Datei noch über alle Dateien hinweg.
- **Kein überflüssiger Code**: Code, der keinen Effekt hat, oder nicht verwendet wird, gibt Abzug.

## Verwendung externer Quellen

- Die Verwendung externer Quellen ist erlaubt. Trennen Sie eigenen Code und kopierten Code in separaten Dateien.
- Alle externen Quellen müssen durch einen Link dokumentiert werden. Dieser Link muss den kopierten Code enthalten.
- Lehrmaterial gilt nicht als externe Quelle und muss nicht dokumentiert werden.
