--
CL1
Qualitatives Feedback

- Insgesamt ein schönes Projekt, die Code Qualität ist insgesamt gut und hat nur kleinere Makel + Toll ist, dass es so gut wie keine Fehlfunktionen gibt, die Website ist gut bedienbar
- Formular Aufgabe wurde sehr gut gelöst
- Schön gemachtes Touren Angebot
  Konzept:

* Motivation: Zu allgemein, konkreter Bezug zur Website fehlt
* Technische Umsetzung:
  "für die Integration der Spielfunktion" ist ungenau (nicht nur)
  Backend fehlt
  Allgemein:
* Rechtschreib- und Grammatikfehler, z.B. "Tourenanagbeote" statt "Tourenangebote", "Ladnschaft" statt "Landschaft
* Stil: "Sportaktivitäten, die man betätigen kann"
* In der Schweiz wird das ß generell durch ss ersetzt
  Wireframes:
* Navigation fehlt teilweise
* Texte zu ausformuliert: nicht Teil eines low-fidelity Wireframe
* Legende und Dokumentation: Für die finale Abgabe fehlt noch eine Legende, die die verwendeten Notationen dokumentiert. Dies ist essentiell für das Verständnis.
  Abgabedokument
* Externe Quellen: ChatGPT Sharing Link
* Inhaltsverzeichnis hat viele Darstellungsfehler
* Design: nichts besonderes
* formal unsauber (Fusszeile, "M290 Datenbanken")
  Website:

- Hero Element gut gelungen, gute Positionierung und Farbeffekte
- Navigation: sauber. Hover fehlt

* Logo nicht lesbar
* Look: mehr Design Polishing (zb. footer, übergänge)
* Responsive: etwas zu hoch für Mobile, Layoutfehler bei tours.html. Elemente über Navi
* Inhaltich: Image Slider unklar für welches inhaltliche Element (Text fehlt)

- Game: sehr gut ausgesucht, spassiges kleines TicTacToe Game. Könnte auch gut im Unterricht eingesetzt werden. Gut gelöst mit dem Popup.

* Game: Spielziel klarer formulieren (verliere nicht um zu gewinnen)
* Game: Realistische Interaktion bei Spielende fehlt. Gewinn ist nicht sichtbar für Benutzer
  "Du hast eine Tour gewonnen. Herzlichen Glückwunsch"
* Originalität Inhalt: etwas zu sehr "von der Platte"
  Formular:

- Top!
- "Daten erfolgreich gespeichert"

* forms.js: restartGame: ist falsch
* Schön wäre hier etwas mehr Realismus gewesen: Wirkt unrealistisch, wenn ich für jeden Tag jede Tour buchen kann. Z.B. wäre ein Kalender mit gesperrten Daten (z.B. keine historischen Daten anwählbar).
  Code:

- Form.js: hohe Code Qualität

* Spinner einblenden/ausblenden Logik ist falsch. Es braucht keinen Spinner, wenn es Validierungsfehler gibt. => nur 1x vor und nach dem await.
* Leere index.js Datei
* try/catch sollten nur asynchrone Operationen umfassen, JS Validierung ist nicht ansychron. - form.js:124 Uncaught ReferenceError: restartGame is not defined
  at HTMLButtonElement.<anonymous> (form.js:124:3) (anonymous) @ form.js:124

- gute Doku im Code
- Saubere Struktur der Dateien, common.css fehlt (gemäss Vorgabe) - CSS:
  Doppelte Deklaration form.css, nur ein Selektor für form
- gute Ordnerstruktur im Teams

* nur ein Abgabedokument

Mündliche Prüfung:

- Allgemein: gute Performance, aktiv, immer versucht was zu sagen, gut

* zu wenig technische Expertise

1. Bilder: 1/1
2. CSS: 0.5/1
3. CSS: 0.5/1
4. JS: https://github.com/TamaraTita/CL1_Tamara_Jasmin/blob/main/js/form.js#L12
   => 1/1
5. JS:https://github.com/TamaraTita/CL1_Tamara_Jasmin/blob/main/js/form.js#L26 => 0.5/1
6. JS:https://github.com/TamaraTita/CL1_Tamara_Jasmin/blob/main/js/form.js#L62 => 0/1
7. JS:https://github.com/TamaraTita/CL1_Tamara_Jasmin/blob/main/js/game.js#L9 Gut: Fachbegriff Interpunktion
   => 0.75/1
   Beilage: html Dokument
   Statische Code Analyse mit Entwickler-Tools Hinweis: nicht alles relevant für die Bewertung Abzug gabs fürs inline JS/CSS

--
AL1

Ist gut rausgekommen. Ihr habt eine starke Schlussphase hingelegt und meine Feedbacks gut verstanden.

Allgemein
+: Klares und modernes Design: einfaches, modernes Layout, das leicht navigierbar ist und die Inhalte gut strukturiert präsentiert.
+: Memory Game: eine kreative und unterhaltsame Möglichkeit, Benutzer zu engagieren
+: Abgabedokument: gut die Aufgaben umgesetzt, sauber und konsistent

Konzept

+: schönes Titelbild

- Motivation: Zu allgemein, konkreter Bezug zur Website fehlt
- 1.4 Backend zu knapp
- Farb Palette zu knapp

Wireframes:
+: gut mit der Text Doku

Website:
+: super habt ihr es mit dem Layout Problem auf der Start Page noch hinbekommen.
+: Texte insgesamt gut umgesetzt. Gute, klare Sprache. Gutes Storytelling, kommt realistisch rüber.
-: an eigenen Stellen zu generisch, zu weitschweifig
-: Design nicht ganz auf professionellem Niveau: wirkt etwas kantig; Header mit professionellem Logo, visuelle Hierarchie und Farbgestaltung könnte besser sein. Dokumentation für Header und Footer.

- einige Bilder sind viel zu gross, zu wenig optimiert für Web
- Slider: ohne Text und ohne klickbare Elemente etwas unfertig.
- Insgesamt noch etwas mehr Feinschliff

- Responsive: https://anjahuser.github.io/AL1_Anja_Lea_Dean/sortiment.html
  Die Produkte Rahmen nicht einheitlich.

- Sortiment.js: der Code ist viel zu kompliziert, das würde in ein paar Zeilen gehen.

Formular:

- Gut mit Meldungen, mit alert() ist unschön (besser im HTML stylen)
- Gut mit UNIQUE für Email in Datenbank. Für den Benutzer gibt es aber keine Fehlermeldung.
- falsches Passwort

Game:
+: Gut umgesetzt, gut spielbar.

- Versuche: wäre logischer, wenn es nur 1x zählt pro Paarauswahl
- Bezug Game und Formular: wäre besser mit Bezug zueinander. Zb. ein Feld mit Code aus dem Game.

Code Analyse:

- Ausser sortiment.js ist der Code einfach und verständlich geschrieben. Gut!
- Einige Fehler und Unschönheiten: inline scripts gemäss Regeln; \* sollte man im CSS nicht verwenden, ein paar Redundanzen

==> Mündl
JS:

- https://github.com/anjahuser/AL1_Anja_Lea_Dean/blob/main/js/sortiment.js#L3C10-L3C25 Wofür steht das c? Wo wird die Funktion aufgerufen?

--
AL3

+: Zwischenabgaben solide und kontinuierlich
+: insgesamt eine solide Arbeit, effizient.

- Quantität etwas mager, Design zu wenig optimiert und ausgefeilt.

Konzept:

- Motivation: zu allgemein, konkreter Bezug zur Website fehlt
- Backend: nicht nur DB. Webserver fehlt.
- Sprache teilweise etwas generisch, weitschweifig

Wireframes:

- teilweise zu klein
- Legende fehlt

Website:

+: tolle Bilder
+: Start Page Hero Element
+: Formular funktional gut umgesetzt, gut bedienbar

- zu wenig Infos über den Shop, Storytelling eines upcoming Online-Shops fehlt.
- Design okay, aber nicht sehr ausgefeilt
- Ausser Formular und Image Slider keine weiteren Interaktionen, Sortiment ist zu statisch.

- Der Slider auf der Homepage kommt gut rüber. Das Interaktionsverhalten ist etwas ungewöhnlich: Besser wäre, wenn ich durch die Slides schnell durchblättern kann. Jetzt muss ich warten bis die Animationen fertig sind und klicke ins Leere.
- Layout Fehler bei https://ahmad-alizada.github.io/AL3_Argjir_Ahmad_Laurin/contact.html: Footer geht nicht bis nach unten
- Header wirkt etwas unfertig

Doku:

- externe Quellen: zu undetalliert, knapp

Datenbank:

- adresse ist nicht atomar

CSS:

- !important sollte man nicht verwenden
- zu wenig CSS files (index.css für alle Pages)

JS:
+: guter Code beim Formular, gut lesbar

- Insgesamt zu wenig JS in der Projektarbeit
- Einige Aufrufe von document.getElementById kommen mehrfach vor, Z.B.
  document.getElementById("nameError")
  Das funktioniert, ist aber schlechter Code Stil. Verwenden Sie Variablen.
  Für die Übersicht ist es besser, wenn alle document.getElementById Aufrufe an einer Stelle sind
- index.js wird nicht verwendet

--
AL4

+: schönes Titelbild

Konzept:

- Bezug zu Website fehlt bei Motivation
- Farben: Farbschema ohne konkrete Farben
- Technisches Setup: zu generisch, zu wenig Kontext zum Modul
- "Vorgabe: Verwenden Sie den Link von "3.1 Datenbank aufsetzen" aus ihrer Abgabe des Moduls 290."
- GitHub: Website Link fehlt

Wireframes:
+: saubere Umsetzung

- zu klein
- Legende fehlt

Datenbank:

- gut umgesetzt

Website:

- Design okay, aber nicht sehr ausgefeilt, etwas lieblos
- Header Design rudimentär
- insgesamt zu wenig Inhalte
- zu wenig Interaktionen, CSS Effekte

Game:
+: Hangman Game: schöne Variante, gut

- Beschreibung/Anleitung fehlt für Benutzer
- Layout "You Lose!!" Screen
- Integration: kein Bezug, was wird wie gewonnen

Formular:
+: gut mit Ländervorwahl (atomare Daten, gut)

- alert() Fehlermeldungen
- Email mit HTML5 Regex
- Spinner: Layout Fehler
- Spinner Logik: sollte im Validierungsvorgang nicht kommen, nur für Datenbank.

CSS:

- .content gehört ins common.css
- common.css und game.css enthalten teilweise dieselben Selektoren (body)
- common.css und index.css enthalten teilweise dieselben Selektoren (body).
  Das muss getrennt sein. Achtet auf die Vorgaben.

-- AL2
+: Umfangreiche und gut gelungene Umsetzung. Super!
+: Toller persönlicher Bezug mit eigenen, berufsnahen Aufgabenstellungen.
+: Grossartige Arbeit bei der Erstellung eurer Website! Es ist beeindruckend zu sehen, dass ihr die klassische Methode mit PHP und HTML verwendet habt. Das zeigt, dass ihr eine solide Grundlage habt und durch eigenständiges Lernen bereits viel erreicht habt.

- Beim Konzept für die Website hätte die Feature Auswahl passender sein können. Feature Auswahl nicht stringent und , zu wenig konsequent umgesetzt.

Konzept:
+: Well done
-: DB Doku ist technisch unvollständig

Abgabedoument:

+: Gutes Design, gut lesbar
+: Beeindruckende Quellensammlung
+: Gut mit "Disclaimer"

Website:
+: Top Background
+: Startpage: tolle Bilder und Animationen
+: Schöne Bilder
+: Top Animationen bei Buttons und Navi
-: Anzeige des aktiven Links fehlt
-: Storytelling upcoming Online-Shops fehlt, etwas zu generisch
-: "in 10 bis 2147483647 Arbeitstagen" Realismus fehlt. Die Features Registrierung und Login sind schon recht ausgefeilt

- Shop: https://www.galaxy-drinks.com/shop.php?type=4 ausgewählte Kategorie nicht markiert
- "Meine Daten aktualisieren": gespeicherte Daten fehlen
- Layout ist bei gewissen Grössen etwas unruhig, es fehlt eine klare Ankerlinie.
  Beispiel: "Dino im All" Text bei schmalen Screens. "Wir sind..." sind eingemittet
- Formular bei https://www.galaxy-drinks.com/product_details.php?product_id=626
- PHP Output oben an der Website. zb. "Bestellung erfolgreich aufgegeben."
- https://www.galaxy-drinks.com/order_product.php Header fehlt
- Texte teilweise zu generisch, weitschweifig
- "Straße": in CH "ss"

CSS:
+: Variablen, Flexbox, Custom Checkboxes (shop.css):
-: Etwas zu viele media queries. Das ist fast schon adaptive und nicht responsive Design an manchen Stellen.
Guter CSS Code ist knapp und funktioniert für alle Screens, das erleichtert die Wartung.
-: Important Rule Overuse (game.css, shop.css)
-: game.css mit game-rock-01, 02, ... Voll okay so. Rock variations würde ich in JS coden, weniger Schreibarbeit und flexibler

Game:
+: gut gelungen, gut spielbar
+: Audio Umsetzung
+: Top mit Highscore
+: Collision Detection, der Fehler ist korrigiert.
-: Spielidee, Bezug zum Shop etwas weit weg für mich.

PHP:
+: gute Skills, gut verstanden: Session Management, Datenbankverbindung
+: Prepared Statements (schützt für SQL Injections), Form Handling, Password Hashing, HTML Special Characters Encoding
-: Input Validation: z.B. in order_product.php. Es braucht immer auch eine Serverside Validierung.
Hier könnte ein Hacker eigenes SQL an die Datenbank senden.

Anhang:
Für zukünftige Projekte: Moderne Webanwendungen nutzen oft AJAX. Hier einige Vorteile:
Bessere Benutzererfahrung: Daten laden, ohne die Seite neu zu laden.
Trennung von Logik und Darstellung: PHP liefert Daten, JavaScript übernimmt die Präsentation.

PRUEFUNG:

- htmlspecialchars: wofür ist das?
- JS: dino.style.top = `${DINO_INITIAL_TOP}px`; ?

--AL5
+: Tolle Comic Bilder
+: Guter JS/CSS Code, gute Debugging Skills, Sie haben einige, nicht einfache Probleme selbst gelöst

- Wie schon bei M290, bessere Fotos wären gut, man kann die Zeichnungen nicht wirklich erknnen

Konzept:

+: Design, guter Text, Farben/Schriften fehlen

- Motivation: zu wenig Kontext zur Website
- Technisches Setup: Server fehlt (nicht nur DB)
- Links im PDF gehen nicht alle
- Texte: teilweise zu generisch, weitschweifig

Wireframes:

- etwas zu detailliert (kein low-fidelity Wireframe)
- zu wenig Fokus auf Interaktionselemente (auch in Notation)

Doku:
+: schön mit Validierungskonzept und Eigenständigkeitserklärung (war nicht Aufgabe)
+: gute Quellen Dokumentation

Abgabedokument:
+: Gutes Design
-: kleine formale Fehler im Inhaltsverzeichnis

Website:
+: Gute Hero Elemente mit Bild im Text
+: schöne Animation bei about-us.html. Etwas random aber grafisch top.
+: Schöne Bild-Filter Effekte bei products.html

- Mix von englisch/deutsch
- Fonts/Typographie: etwas zu grosser Unterschied von Titel und Caption Text (z.B. Home Page "Disocver..").
- Header und Footer könnten sich visuell noch etwas mehr abgrenzen vom Content, Struktur nicht gut erkennbar
- "Play Game": etwas aufdringlich ("Nag-Screen"), sollte nicht immer wiederkommen, wenn ich es mal weggeklickt habe
- etwas wenig Inhalte/Storytelling eines upcoming Shops

Game:

- Anleitung fehlt
- etwas schwierig mit den kleinen Bildern, Farben hätten geholfen

Formular:
+: sehr gut mit Email Check und Spinner, technisch sehr gute Umsetzung. Spinner ist etwas gross.
-: Formular bleibt nach Absenden stehen, ich kann nochmals Submit drücken
-: Layout Sprung bei Fehlermeldungen Anzeige

JS:
+: gut beim Formular, gut mit showErrorMessage() Funktion
+: Super mit index.js displayRandomProducts, top Feature!
+: Zu components.js: gute Idee, moderne Frontend Programmierung ist komponentenbasiert. Finde ich spannend wie Sie das umgesetzt haben.

CSS:

- Variablen Definition teilweise dupliziert.

Anhang:
components.js: In der Praxis etwas umständlich, das Erstellen von Komponenten haben Frameworks schon für Sie gelöst. Sie könnten sich in ein Framework wie React oder Vue einarbeiten. Für Jobs ist es relevant, dass man mit solchen Frameworks arbeiten kann.

--
CL2

Konzept:

- Design: etwas mehr Bezug zum Thema (warum diese Stile)
- "2-4 marktwirtschaftlich relevante Ziele," stehen gelassen
- Technisches Setup: Server fehlt (nicht nur DB)
- Validierungskonzept gut, war aber nicht Aufgabe

Wireframes:

- Notation: fehlt

Doku:
+: inhaltlich gut

- Bilder fehlen bei Highlights

Abgabedokument:
+: top Titelbild, sieht sehr gut aus
+: solides Design, guter Header

Website:
+: tolle Bilder, schönes Start Bild
+: Schöne Call-to-Action mit animiertem Button

- Inhaltlich: ihr schreibt, was bei euch bei besonders ist beim Sortiment.
  "Bei Phone Flow bestimmst du nicht nur das Betriebssystem, sondern auch Farbe und Speicherplatz. "
  Im Shop dann aber nur Standard-Geräte und ein Standard Handyhüllen-Angebot.
- Design: insgesamt, wirkt nicht sehr ausgefeilt, es fehlen Verfeinerungen
- Typographie: Schriftgrössen Unterschied zu gross
- Logo Text etwas klein
- Navigation: Schriftfarben nicht optimal (Kontast bei aktiver Link, hellblau als neue Farbe)
- "Wähle deine Komponenten": Interaktionskonzept unklar, man denkt, man kann hier klicken
- Shop Page, Game Page: Text klebt am Rand
- "ß" in der Schweiz "ss"

Game:
+: gute Grafiken, guter Sound
+: Gute Story

- noch etwas ungeschliffen.. zu wenig weit gekommen
- Game Animationen sollten am Anfang ausgeschaltet sein
- Spielende unklar (Spiel stoppt nicht richtig)
- Integration mit Formular

Formular:
+: gut mit Fehlermeldungen
+: Code ist einfach, gut lesbar
+: gut mit Reset der Daten nach Abschicken. Besser: Erfolgsmeldung einblendenund Formular ausblenden

- wenig Eigenleistung
- "schreibe uns in der Nachricht, wie hoch dein Highscore war": Unrealistisch. Besser mit Game verknüpfen und Score nicht durch Benutzer eingeben lassen. Unrealistisch.
- Submit Button nicht gestyled
- keine Erfolgsmeldung für Benutzer
- Texte: "Wir werden dann jemanden auslosen, damit du nicht wie Jan, einen so schwierigen Weg zu deinem ersten PhoneFlow-Handy hast." umständliche Formulierung

Code:

- index.js: leere Datei
- myFunction: schlechter Name
- var statt const/let
- insgesamt wenig eigener Code bei JS (sehr nahe an Vorlagen)

--
CL3

Konzept:
+: gutes Fachwissen bei Autos, etwas lang mit den Beschreibungen
+: Design ist gut beschrieben

- immersives Erlebnis: wird auf der Website nicht ganz eingelöst
- Über die Website: Zwecke zu wenig auf Inhalte auf der Website bezogen. Fahrzeugverkäufe gibt es nicht.
- Sprachlich teilweise etwas zu generisch, inhaltlich zu wenig auf den Kontext einer Schularbeit bezogen
- Technisches Setup: Webserver fehlt (nicht nur DB). Sonst gut.

Wireframes:
+: Insgesamt gut, guter Fokus auf Interaktionselemente, sehr gute Doku

- Lesbarkeit: zu klein, nicht alle Texte lesbar
- Lesbarkeit: Seitenumbrüche bei Bilder

Doku:
+: soweit gut

Abgabedokument:

- Inhaltsverzeichnis nicht gemäss Vorgabe. Unnötige Abschnitte wie "5 Ausblick Content und Design"

Website:
+: Schöne Textanimation, kommt gut
+: Guter Call-to-Action Button mit Gewinnspiel
+: guter Scroll-Effekt mit JS
+: Schöne Bilder

- "Über uns" ist nicht geglückt: nicht einheitlich mit den anderen Pages; nicht responsive, einige Layoutfehler, dupliziertes CSS
- Design allgemein: etwas ungeschliffen, es fehlen Feinheiten
- Navigation bei Mobile: Layout Fehler
- Shop: schöner Hover-Effekt, aber inhaltlich etwas mager
- Typographie: Schriften teilweise zu klein. Kleiner als 16px sieht man selten.
- Buttons sollten immer einen Hover haben
- Design des Headers sollte besser sein, wirkt zu langweilig, zu wenig ausgefeilt. Hover unschön.
- insgesamt etwas wenig Inhalte. Keine weiteren interaktiven Elemente
- Texte: Storytelling des upcoming Shops mit orignellem Sortiment kommt nicht rüber. Texte teilweise zu generisch, weitschweifig

Formular:
+: gut mit Select Element

- Fehlermeldungen mit alert()
- "Bitte füllen Sie alle Felder korrekt aus." zu allgemein, der Benutzer weiss nicht genau, was er verbessern muss. Z.b. wenn er "D" eingibt beim Nachnamen.
- im Code: vorbereitet für Fehlermeldungen im HTML, aber nicht fertig umgesetzt: email.classList.add("error");
- created_at: new Date(): das Datum sollte von der Datenbank erzeugt werden. Das Feld sollte nicht geschickt werden.

Game:

- Bezug zur Website, Integration
- etwas wenig Inhalt, bleibt für den Benutzer unklar, was das Ziel ist und wie es funktioniert
- Grafiken: Guter Hintergrund, das Polizeiauto ist zu klein
- wenig Features

Code:

- insgesamt zu wenig JS Features / Funktionalitäten auf der Website

--
CL4

+: toll mit persönlichem Bezug zur Website
+: Top Artwork
-: Technisch zu wenig (JS Features, CSS Design)

- Einig Punkte verschenkt mit unsauberer Arbeit im Abgabedokument
- ihr wart schon nicht so gut dabei, und habt am Schluss nicht mehr genug Gas gegeben.
- Feedbacks sehr mangelhaft umgesetzt

Konzept:

- Zwecke: "Zudem werden auf einer Unterseite unsere Produkte verkaufen" keine Funktionalität im Shop, Konzept nicht nah genau an Aufgabe
- Design: Farbpalette ungenau
- Setup: Webserver fehlt, zu knapp; Bezug "Anleitung "3.1 Datenbank aufsetzen" "

Wireframes
+: Beschreibungstext: gut, hilft fürs Verständnis

- Notation: zu knapp
- "Notch" unklar bei Wireframes macht man das nicht
- teilweise zu knapp, z.B. Header bei Produkt Page
- Navigation kommt nicht klar rüber / Hamburger gibt es nicht bei Desktop

Doku:

- Highlights Screenshots fehlen
- Highlights: zu detailliert, "Name des Elements" falsch eingefüllt

Abgabedokument:

- Ein paar Schreibfehler: "Mit hilfe von"
- Design: okay, nichts besonderes, ein paar formale Fehler (zb. Seite 13)
- Texte stehen lassen aus der Aufgabe, z.B. "Gemäss Projektauftrag im OneNote (auf der nächsten Seite)"

Website:
+: Tolle Bilder
+: Interessante Variante mit der Startseite
+: Startseite ist designed
+: Shop: schön mit Produktdetails, gut gelöst mit Link auf Event Page, kommt realistisch rüber
+: Animationen: gute Hover Effekte, kommen gut. Sonst bei Animationen zu mager.

- Navigation: sollte auf allen Pages gleich aussehen. Ich komme nur über Events zum Game.
- Navigation: Kontrast Schriftfarbe
- Bilder teilweise viel zu gross
- Navigation zu wenig gestyled
- Design: guter eigener Stil, an vielen Stellen wirkt es noch ungeschliffen (Footer, Header)
- gut mit eigenen Pages für Impressum / Datenschutz. Ist aber zweimal derselbe Link.
- Impressum: Header fehlt, ich kann nicht mehr zurücknavigieren
- Typographie: nicht mehrere Schriftarten verwenden
- Events Page: schlechtes Design,
- Inhaltlich: Rave Anmeldung, es fehlt ein Text wozu und warum.
- Events und Garments: Header nicht einheitlich, springt im Layout beim Wechseln
- insgesamt zu wenig Inhalte (vorallem viel zu wenig JS)

Formular:

- HTML5 Validierung (required). Das habe ich ihnen 3x geschrieben...
- kein JS geladen
- Telefonformat: passt nicht für CH
- keine Erfolgsmeldung für Benutzer
- Code: unnötiger Page Reload (event.preventDefault() fehlt)

Game:
+: Toller Dancer, top Sound
+: Toller Hintergrund

- Gute Idee mit "Screenshot", es sollte klarer sein, was in den Screenshot soll (Highscore?)
- Texte: etwas zu kurz, Anleitung fehlt (Spacebar drücken)
- Dancer hüpft aus Spielfläche
- Design der Page sehr rudimentär

Ihr habt euch viel zu wenig auf die Aufgaben konzentriert.
Meine Empfehlung am Wochenende nachzulegen seid ihr nicht nachgekommen.
Auch mit viel Goodwill, dass ihr etwas persönliches gemacht habt => das ist eine 3 im Zeugnis.
Soll euch nicht entmutigen weiterzumachen mit eurem Projekt.
Vermutlich ist es besser, wenn ihr eine erste Version mit einem Baukasten-Tool baut.

-- CL5

+: Lustige Idee mit Dienstag
+: wenig Support gebraucht, selbstständig gearbeitet
-: Potential der Gruppe nicht ausgeschöpft.

Konzept:

- Design: Farbpalette fehlt
- Setup: Backend ist falsch. Komponenten, nicht Software (Web Server, DB)

Abgabedokument:
+: schönes Titelbild
+: gutes Design

Wireframes:
+: gute Umsetzung, klarer Fokus auf die Anforderungen eines low-fidelity Wireframes

- Notation fehlt

Doku:
+: schön mit Aufteilung nach Gruppenmitglieder bei Code Highlights

- Bild fehlt bei Game.
- externe Quellen: zu wenig Details (Nachvollziehbarkeit)

Website:

+: Logo Animation gefällt mir. Würde nerven bei einer normalen Website, für eine Promo Website gut geeignet.
+: Design: Top Element ist grafisch gut gelungen
+: Design: Highlights mit grünen Farbverläufen und Bildeffekten sieht professionell aus

- Responsive: Die Start Page ist wegen dem Game nicht responsive, es gibt unten einen Scrollbar. Bei eurem Game wäre das gut responsive gegangen.
- Navigation: Aktiver Link "Shop" funktioniert nicht
- Navigation: Mobile: "Shop" Navigation bleibt stehen
- Navigation: Mobile sieht es so aus, als wäre das Gewinnspiel die aktive Page
- Grafik-Fehler: Mobile Navigation überlappt mit Highlights Element
- Weiteres grösseres Feature: Ihr habt Navigation, Formular und Game. Leider fehlt ein weiteres Element wie ein interaktiver Shop oder ähnliches.
- Storytelling: kommt nicht gut rüber mit der Geschichte eines upcoming Shops mit speziellem Sortiment, etwas zu generisch, zu wenig Kontext, es gibt zu wenig Infos über den Shop
- Schreibfehler "Schade, ledier hast du nicht gewonnen"
- Bilder sind etwas zu gross
- Responsive: insgesamt gut! kleine Fehler, zB. Footer Text klebt am Rand bei 620px

Game:
+: Für den Rahmen dieser Arbeit gut ausgesucht. Kleines Mini-Game.

- Anleitung fehlt. Was ist das Spielziel? Was ist die Story? Braucht mehr Text.
- UX: Was ist das Spielziel? Für den Benutzer ist nicht klar, wieviele Klicks es braucht. Ich gebe nach 2-3 Versuchen auf, wenn ich nicht weiss, wieviele Klicks ich schaffen muss.
- UX: Noch etwas mehr Features: das Game wird schnell langweilig, um Benutzer zu animieren das Game mehrmals zu spielen (z.B. Highscore verbessern, weitere Spielinhalte)
- Restart Button fehlt

Formular:
+: Gute Umsetzung, sehr gute Fehlermeldungen
+: gut lesbarer JS Code

- DOMContentLoad braucht es nicht
- etwas mager bei den zusätzlichen Features (Spinner einbauen, Email Check,..)
- "Kontaktiere uns bei Fragen", kein Incentive für Benutzer

  Code:

- index.js leere Datei

--
B1

Abgabedokument:
+: Schönes Titelbild
+: gutes Konzept, Aufgabe gut umgesetzt
+: Design: gut mit Verweis auf web safe fonts.

- Technische Umsetzung: Web Server fehlt
- Ziele: zu wenig Bezug zu konkreten Elementen auf der Website

Wireframes:

- Lesbarkeit: zu klein

Datenbank:

+: gut mit "address" für Anrede, gut mit enum

--
B2

Konzept:

- "Virtuelle Anprobe: Kunden testen Brillen virtuell." keine Umsetzung
- Ziele: zu wenig Bezug zu konkreten Elementen auf der Website
- Design: Farbschemata ohne genaue Farben
- Technische Umsetzung: Web Server fehlt
- Text teilweise zu generisch, weitschweifig; Schriftfehler bei Motivation

Abgabedokument:
+: Schönes Titelbild

Datenbank:
+: gut, viele Attribute

- PLZ sollte eine Zahl sein

--
B3

Konzept:
+: Design: top mit Moodboard
+: gutes Konzept

- Alleinstellungsmerkmal überzeugt mich nicht ganz (gute Produkte haben alle)
- "Feedback zu einzelnen Produkten zu geben" nicht so umgesetzt
- Technische Umsetzung: Web Server fehlt. Sonst gute Texte.

Abgabedokument:
+: Tolles Titelbild

Website:
+: Farbkomposition kommt super rüber. Das Moodboard lässt grüssen.

- Header: Logo könnte noch edler rüberkommen, harter Übergang mit Bild
- Kontrast: besser, noch nicht ganz gut. Würde ich lösen mit Bildbearbeitung: Weichzeichnen des Bilds, transparency, brightness, ..
- Schriften zu klein (z.b. im Header) oder Footer: bei Webdesign werden selten Schriften mit weniger als 16px verwendet.

Game:
+: tolles Game: Grafiken und Ton sind super.

- Code: wäre übersichtlicher wenn alle document.getElementById() oben als Variablen deklariert sind.

--
B4

Konzept:

+: sehr gutes Konzept, tolle Idee. Gebe euch max. Punkte.
+: Design: top

- Technische Umsetzung: Web Server fehlt. Sonst gut.
- "selbst porgrammierten"

Wireframes:

- spannende Klassifizierung mit den Farben, gefällt mir mit den Kategorien.
- Die Notation mit Farben ist etwas ungewöhnlich bei Wireframes, wirkt eher ablenkend. Wichtig ist die Notation für Interaktionselemente. Andere Elemente sind weniger wichtig.

Abgabedokument:
+: Tolles Titelbild
+: ausführliches Inhaltsverzeichnis, gute Gliederung

Datenbank:
+: gut mit enum

--
B5

Konzept:

+: gutes Konzept
+: "Zudem zeigt der Slogan auch, dass wir für Authentizität und eine direkte Ansprache" Gute Formulierung, Kein Abzug für "profanity" :)
+: Design: top erklärt

- Technische Umsetzung: Web Server fehlt (nicht nur DB)

Abgabedokument:
+: Tolles Titelbild
+: gutes Design des Dokuments

- Name: Name => Vorname, Nachname

--
B6

Konzept:

- Technische Umsetzung: Web Server fehlt (nicht nur DB)

Abgabedokument:
+: Tolles Titelbild

Website:
+: Wirklich tolle Bilder.
+: Toller Font mit Pflanzen auf den Buchstaben sieht gut aus. Geschmackvoll.
+: Gutes Storytelling, Geschichte des upcoming Shops kommt gut rüber
+: Sehr viele Animationen für Einblendungen (Shop, Game, Home). Finde ich gut! Praxis: für eine Showcase/Promotion Website ist es ok, auf einer normalen Online-Shop Website würde die Menge an Animationen schnell nerven.

- Homepage: Buttons "Jetzt spielen", "Anmelden". Das Grau sieht etwas aus wie deaktiviert. Sieht besser aus mit dem grün beim Hover.
- Unsere Produkte Page ist nicht ganz responsive. Es gibt bei ca. 1000px Breite unten einen Scrollbalken.
- Schriften etwas zu klein. 16px ist am unteren Rand, was man im Web braucht. Inputfelder wie im Formular müssen grösser sein.
- Header ist zu hoch, vorallem auf Mobile zu viel Platz verbraucht. padding mit % ist nicht. % funktioniert oft nicht so gut bei Responsive, weil es dann Mobile zu viel Platz verbraucht.

Formular:
+: top mit Fehlermeldungen und Spinner

- UX: Formular bleibt nach dem Absenden stehen und man kann immer wieder speichern klicken. Das ist unlogisch.
- Die Fehlermeldung könnten aussagekräftiger sein (mindestens 2 Buchstaben).
- Detail bei der Validierung: es gibt Vornamen mit 2 Buchstaben.

Game:

- Nicht responsiv, es braucht einen sehr breiten Bildschirm. Das Grid fürs Game ist ok, aber memory-text müsste anders platziert werden.
- Mauszeiger sollte ein Pointer sein bei den Cards
- Anleitung für Benutzer fehlt. Kein Text (Story of the Game, How to Play, What to Win)
- Responsiv wäre schön gewesen. Etwas aufwendig bei ihrem Code, wäre gegangen.

--
B7

Konzept:
+: gutes Konzept
+: Design: tolles Bild und gut erklärt

- "einzigartige Möglichkeit aus, ein hervorragendes Steak mit Beilage selbst zusammen zu stellen" etwas unklar, was genau die Möglichkeiten sind. Beilage und Sauce wählen können ist nicht sehr originell.
- "Kundenbewertungen und Testimonials" nicht umgesetzt
- Technische Umsetzung: Web Server fehlt (nicht nur DB); "Für das komplette Hosting" ungenau, was heisst komplett

Abgabedokument:
+: Tolles Titelbild

Website:
+: Texte: gute Marketing Texte, teilweise etwas zu reisserisch
+: Schönes Hero Element
+: Design: auf einem guten Level, einige Stellen brauchen noch Feinschliff.

- Navigation: Hover kaum sichtbar. Guter aktiver Link
- Einrücken: "Bestellung" und Menus nicht mit gleichem Abstand am linken Rand. Beide sollten gemeinsam angeordnet werden.
- Design: Schriftgrössen leicht zu klein für Lesbarkeit.
- Eigenes Element: es hätte noch ein interaktives JS Element mehr sein sollen.
- Inhaltlich beim Menu: aus UX Sicht sollten die Menuvorschläge bestellbar sein.
  Z.b: bei Klick auf ein bestimmtes Menu werden die Formularfelder angepasst.
  Wirkt so etwas unklar.
- Mehr Realismus: schön wäre ein Price Calculator, wenn ich im Formular verschiedene Werte auswähle.

Formular:
+: gutes Design, kommt professionel rüber
+: Formular ist gut geworden, toll!

Game:
+: Spielidee gefällt mir, kommt witzig rüber für mich.
+: Tolle Animation beim Messer
+: guter Effekt bei Game Over, kommt gut

- etwas wenig Features: kein Restart, keine Musik, Game ändert sich nicht mit der Zeit.
- Integration: Spielidee gefällt mir, der morbide Charakter passt nicht ganz zum edlen Ton sonst auf der Website
