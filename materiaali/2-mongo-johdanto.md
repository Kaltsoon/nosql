# Johdanto MongoDB-tietokantajärjestelmään

Kurssin toisesessa osiossa tutustutaan MongoDB-tietokantajärjestelmään, joka on eräs suosituimmista NoSQL-tietokantajärjestelmistä. Tämän osion aikana opit mm. TODO.

MongoDB-tietokantajärjestelmä on laajalti käytössä oleva NoSQL-tietokantajärjestelmä. Vuoden 2023 [State of Database](https://stateofdb.com/) -kyselyn perusteella MongoDB on kolmen tunnetuimman ja käytetyimmän tietokantajärjestelmän joukossa. MongoDB on dokumentti-pohjainen (document-oriented) tietokantajärjestelmä. Tutustu dokumentti-pohjaisiin tietokantoihin lukemalla artikkeli [What is a Document Database](https://www.mongodb.com/resources/basics/databases/document-databases). Sen jälkeen on aika tutustua MongoDB-tietokantajärjestelmän perusteisiin ja tietomalliin lukemalla artikkelit [MongoDB Basics](https://www.mongodb.com/resources/products/fundamentals/basics) ja [Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/). Lopuksi, osoita osaamisesi vastaamalla tähän kyselyyn Moodlessa. 

## MongoDB:n asennus

Jotta pääsemme harjoittelemaan MongoDB:n käyttöä käytännössä, tulee tietokantajärjestelmä asentaa tietokoneellemme. Asennusohjelman voi ladata [täältä](https://www.mongodb.com/try/download/community).

> [!IMPORTANT]  
> Valitse omalle käyttöjärjestelmällesi (esim. Windows tai macOS) sopiva asennusohjelma.

## Käyttöliittymiä tietokannan hallintaan

- MongoDB Shell https://www.mongodb.com/docs/mongodb-shell/
- MongoDB Compass https://www.mongodb.com/products/tools/compass
- MongoDB Vs Code extension https://www.mongodb.com/products/tools/vs-code

1. Luo tietokanta `Y` ja luo tietokantaan kokoelma (collection) `X`
2. Vie tietokantaan tämän CSV-tiedoston sisältö seuraamalla [Import and Export Data](https://www.mongodb.com/docs/compass/current/import-export/) -ohjeen ohjeita
3. Selvitä, miten dokumentteja haetaan tietokannasta lukemalla [Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/) -ohje. Toteuta sen jälkeen kysely, joka hakee kaikki dokumentit kokoelmasta `X`

⏭️ [Siirry seuraavaan osioon](./3-mongo-operaatiot.md)
