# Energy Guardian
Dit is een project voor de Haagse Hogeschool.

# Download het project
Je kunt het project downloaden door op de groene knop rechtboven te drukken. Vervolgens klik je op download zip.

Pak de zip uit, het maakt niet uit waar.

# Project openen
Als je aan de website wilt werken kan je die bijvoorbeeld openen in vscode. Anders kan je deze stap overslaan.

## Bestanden bewerken
De html bestanden staan in de map templates en het css bestand in de static map. In de static map staan ook alle andere bestanden, zoals afbeeldingen en javascript bestanden.

# MYSQL workbench koppelen
Voordat de server opgestart kan worden moet eerst de database gekoppeld worden. Dit doe je in het bestand `settings.py`. Hier zoek je naar het stukje genaamd databases, hier moet je het een en ander aanpassen. De naam is root en het wachtwoord is het wachtwoord dat je invult als je de workbench gebruikt. Name staat voor database, wat voor in ons geval `energy_guardian` is. Host staat voor welke connectie je gebruikt, meestal als standaard is dat localhost. De poort kan je zo laten, want die is standaard 3306. Deze gegevens moet je ook aanpassen in de bestanden `views.py` en `connect.py`.

# Server opstarten
Open een terminal bijvoorbeeld in die van vscode. Ga naar de map waar het bestand `manage.py` staat. 

Vervolgens voer je het commando `python manage.py runserver`. Als het goed is, is de server nu opgestart. Is dit niet geval kan je het even aan iemand vragen.

