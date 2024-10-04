# Tietokantaoperaatiot MongoDB-tietokantajärjestelmässä

Opintojakson kolmannessa osiossa tutustutaan tietokantaoperaatiohin MongoDB-tietokantajärjestelmässä. Tämän osion aikana opit mm. TODO.

## CRUD-operaatiot

[CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete)-operaatiot (create, read, update, delete) ovat yleisimpiä tietokantaoperaatioita. Harjoitellaan seuraavaksi niiden käyttöä MongoDB-tietokantajärjestelmässä.

Ennen tehtävien aloittamista, avaa MongoDB Compass -ohjelma ja edellisessä osiossa käytetty `library`-tietokanta MongoDB Shell:issä.

TODO: https://chatgpt.com/share/66ffb828-3890-8006-9e05-2f0914ca8c80

### Dokumenttien lisääminen

> [!IMPORTANT]  
> Kun luet MongoDB-dokumentaatiota, valitse koodiesimerkkien kieleksi "Select your language"-valikosta "MongoDB Shell".

Lue ohje [Insert Documents](https://www.mongodb.com/docs/manual/tutorial/insert-documents/). Lisää sen jälkeen `book`-kokoelmaan dokumentti seuraavilla tiedoilla käyttämällä `insertOne`-metodia:

| title                 | author        | year | genres                            | copies |
| --------------------- | ------------- | ---- | --------------------------------- | ------ |
| "Pride and Prejudice" | "Jane Austen" | 1813 | ["Romance", "Classic", "Fiction"] | 3      |

Listaa tämän jälkeen kaikki `book`-kokoelman dokumentit. Huomaa, että kaikille dokumenteille on generoitu `_id`-attribuutti, joka toimii dokumentin yksilöllistävänä pääavaimena.

Lisää vielä seuraavat dokumentit yhtäaikaisesti käyttämällä `insertMany`-metodia:

| title                   | author                      | year | genres                                                     | copies |
| ----------------------- | --------------------------- | ---- | ---------------------------------------------------------- | ------ |
| "War and Peace"         | "Leo Tolstoy"               | 1869 | ["Historical Fiction", "Classic", "Philosophical Fiction"] | 84     |
| "The Lord of the Rings" | "John Ronald Reuel Tolkien" | 1954 | ["Fantasy", "Adventure", "Epic"]                           | 0      |
| "Brave New World"       | "Aldous Huxley"             | 1931 | ["Dystopian", "Science Fiction", "Classic"]                | 11     |
| "The Hobbit" | "John Ronald Reuel Tolkien" | 1937 | ["Fantasy", "Classic"]                           | 17      |

Listaa tämän jälkeen kaikki `book`-kokoelman dokumentit.

### Dokumenttien hakeminen

Lue ohje [Query Documents](https://www.mongodb.com/docs/manual/tutorial/query-documents/). Toteuta sen jälkeen seuraavat komennot:

1. Hae kirja, jonka nimi on "War and Peace"
2. Hae vuoden 1900 jälkeen julkaistut kirjat
3. Hae saatavilla olevat kirjat (kirjat, joiden kopioita on enemmän kuin 0)
4. Hae kirjat, jotka kirjailija "John Ronald Reuel Tolkien" on kirjoittanut ennen vuotta 1950
5. Hae "Fantasy"-genren kirjat. Vihje: [Query an Array](https://www.mongodb.com/docs/manual/tutorial/query-arrays/)

### Dokumenttien päivittäminen

Lue ohje [Update Documents](https://www.mongodb.com/docs/manual/tutorial/update-documents/). Toteuta sen jälkeen seuraavat komennot:

1. Muuta kirjan "Brave New World" julkaisuvuodeksi 1932
2. Aseta kaikkien kirjailijan "John Ronald Reuel Tolkien"-kirjailijan kirjojen kopioiden määräksi 0
3. Kasvata kaikkien vuoden 1900 jälkeen julkaistujen kirjojen kopioiden määrää kahdella. Vihje: [$inc](https://www.mongodb.com/docs/manual/reference/operator/update/inc/)-operaattori
4. Lisää kirjalle "The Hobbit" genre "Adventure". Vihje: [$push](https://www.mongodb.com/docs/manual/reference/operator/update/push/#mongodb-update-up.-push)-operaattori

### Dokumenttien poistaminen

Lue ohje [Delete Documents](https://www.mongodb.com/docs/manual/tutorial/remove-documents/). Toteuta sen jälkeen seuraavat komennot:

1. Poista kirja "Pride and Prejudice"
2. Poista kirjat, joiden kopioiden määrä on 0

## Embedded Data Versus References

https://www.mongodb.com/docs/manual/data-modeling/concepts/embedding-vs-references/

## Aggregointi-operaatiot

- Creating Collections and Documents
- Retrieval and Update Commands
- Implementing CRUD Operations in MongoDB
- Aggregation

⏭️ [Siirry seuraavaan osioon](./4-mongo-python.md)
