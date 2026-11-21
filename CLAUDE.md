# CLAUDE.md – Futisvalmennus: harjoitepankki

Tämä repo on avoin jalkapallon harjoitepankki. Jokainen harjoite on oma kansionsa,
ja harjoitteet luokitellaan yhteisellä sanastolla (`sanasto.yml`).

## Rakenne

```
sanasto.yml                 # luokittelun sallitut arvot ja säännöt – AINOA totuuden lähde
harjoitteet/
  _malli/harjoite.md        # pohja uudelle harjoitteelle
  <tunniste>/
    harjoite.md             # frontmatter + kuvaus
    kaavio.svg              # kenttäkaavio (valinnainen)
    variaatiot.md           # helpotukset/vaikeutukset (valinnainen)
.claude/skills/
  harjoite-laadinta/        # uuden harjoitteen laatiminen
  harjoituspaiva-kokoaminen/# harjoituspäivän kokoaminen pankista
```

## Toimintaohjeet

- Lue `sanasto.yml` ennen kuin luokittelet tai haet harjoitteita. Käytä vain siinä
  määriteltyjä avaimia (esim. `murtautuminen`, `1H`, `oikea_sisempi_laitakaista`).
  Älä keksi uusia termejä – ehdota sanastomuutosta käyttäjälle.
- Noudata `sanasto.yml`:n `saannot`-osion luokittelusääntöjä.
- Harjoitteen tunniste = kansion nimi: pienet kirjaimet, ei ääkkösiä, sanat
  väliviivoilla (esim. `syottopeli-4v4-2`). Tunniste ei muutu julkaisun jälkeen,
  koska harjoituspäivät viittaavat siihen.
- Uusi harjoite tehdään `harjoite-laadinta`-skillillä ja pohjasta `harjoitteet/_malli/`.
- Kaaviot piirretään harjoitekaavio-skillillä (tyyli D), roolit merkitään
  lyhenteillä 1H–3H ja 1P–3P, kaistat lyhenteillä VLK, VSLK, KK, OSLK, OLK.

## Tärkeät termit

- **Avaaminen** = pallon hallittu avaaminen omalta kolmannekselta.
- **Rakentaminen** = keskikolmanneksen vaihe, EI omalta alueelta avaamista.
- **Pelin keskus** = pallon ympäristö: hyökätessä 1H, 2H, 3H; puolustaessa 1P, 2P, 3P.
- **Vasen/oikea** katsotaan aina harjoittelevan joukkueen hyökkäyssuuntaan.

## Tietosuoja

Repo on julkinen. Älä koskaan kirjoita tänne pelaajien nimiä, poissaoloja,
terveystietoja tai muita joukkuekohtaisia tietoja. Ne kuuluvat yksityiseen
joukkuerepoon, joka viittaa tämän pankin harjoitteisiin tunnisteella.

## Kieli

Sisältö kirjoitetaan suomeksi.
