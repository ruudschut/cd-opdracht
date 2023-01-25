# Eindopdracht WINC Back-end Development

Bij deze opdracht is de basis al redelijk uitgebreid behandeld in de voorgaande lessen. Het aanmaken van een droplet, maar nu met SSH verbinding is de eerste aanpassing. Droplet geeft hier een duidelijke stap voor stap handleiding voor dus dat was niet het ingewikkeldste stuk.
De volgende stappen waren om ook hier NGINX en Gunicorn op te activeren, dit is ook al eerder gedaan dus even de commando's opgezocht en het was actief

## Flask app
Ik heb een bestaande Flask App gebruikt die we in eerste instantie alleen lokaal hebben gebruikt. Ik heb eerst deze werkend proberen te krijgen door de bestanden via de terminal op te halen buiten de acties. Dit om wat meer thuis te raken in het gebruik. Nadat deze werkend was ben ik met het volgende onderdeel aan de slag gegaan

## Secrets
Zoals bij veel van de opdrachten zijn er duidelijke tutorials te vinden. In eerste instantie was er een voorbeeld waarop duidelijk was welke 'secrets' er gemaakt moesten worden, HOST, KEY en USER. Waar ik hierbij tegenaan liep is dat het me niet helemaal duidelijk was welke KEY ik nu moest gebruiken, de KEY die reeds gemaakt was voor de SSH verbinding? Maar die was lokaal gegenereeerd. Via [deze tutorial](https://medium.com/swlh/how-to-deploy-your-application-to-digital-ocean-using-github-actions-and-save-up-on-ci-cd-costs-74b7315facc2) heb ik een key op de server gemaakt en toegevoegd aan GITHUB.

## Actions
Daar zit wel wat trial en error werk in. Om eerst te zien dat ik verbinding kon maken ging het om wat simpele commando's als 'touch foo.txt' in een geopende directory. Grootste probleem zat hem in de keys. Op een gegeven moment kon ik niet meer via mijn terminal inloggen op mijn droplet via een SSH verbinding. Acces denied met een melding over een onjuiste Key. Hmm, hier heb ik blijkbaar wat verkeerde dingen aangepast. Gelukkig kun je via je Digital Ocean omgeving inloggen via een Console en een nieuw key genereren en die weer op je computer bewaren en toevoegen aan authorized_keys. Geeft dan toch wel voldoening wanneer er wel weer verbinding gemaakt kan worden. Maar uiteindelijk lukt het ook om via de actions een verbinding te maken via SSH met droplet. 
