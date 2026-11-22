---
name: harjoite-laadinta
description: Laadi uusi jalkapalloharjoite harjoitepankkiin luokiteltuna sanasto.yml:n mukaan. Käytä, kun käyttäjä pyytää uutta harjoitetta tai haluaa lisätä harjoitteen pankkiin.
---

# Harjoitteen laadinta

## 1. Lue sanasto
Lue `sanasto.yml`. Käytä vain siinä määriteltyjä avaimia ja noudata `saannot`-osiota.

## 2. Selvitä lähtötiedot
Kysy käyttäjältä puuttuvat tiedot, enintään yhdellä kysymyskierroksella:
- vaihe ja alavaihe (tai opetettava asia, josta ne päätellään)
- pelin keskuksen tilanne ja roolit
- ikäluokka, pelaajamäärä ja kesto
Jos käyttäjä antaa vapaan kuvauksen, päättele luokittelu ja näytä se hyväksyttäväksi.

## 3. Tarkista luokittelu
- Yksi päävaihe ja yksi alavaihe. Jos harjoite opettaa selvästi myös toista
  alavaihetta, lisää se `myos_alavaiheet`-kenttään (enintään 2) ja kerro siitä käyttäjälle.
- Roolit kuuluvat vaiheen `sallitut_roolit`-listaan.
- Tilanteen lukumäärä ja roolit eivät ole ristiriidassa (2v1 → 1H, 2H vs. 1P).
- Paineistaminen: ei, passiivinen, puoliaktiivinen tai aktiivinen (sanasto.yml).
- Kaistat vain, jos harjoite kohdistuu niihin; vasen/oikea hyökkäyssuuntaan.
- Vakiotilanteissa `puoli` ja `tehtavat`.
- Tekninen drilli ilman vastustajaa ja pelin vaihetta: `vaihe: tekniikka`,
  alavaiheeksi harjoiteltava taito, `paineistaminen: ei`; `pelin_keskus` ja `alue` jätetään pois.
- Lämmittelyksi tehty harjoite: `vaihe: alkulammittely`; fyysistä ominaisuutta
  kehittävä harjoite: `vaihe: fysiikka`; harjoituksen lopuksi tehtävä
  fyysinen osio: `vaihe: loppufysiikka`. Kuten tekniikassa, `pelin_keskus` ja `alue`
  jätetään pois (sanastossa `ilman_pelin_keskusta: true`).

## 4. Luo tiedostot
- Tunniste: pienet kirjaimet, ei ääkkösiä, väliviivat. Tarkista, ettei kansiota ole jo.
- Kopioi `harjoitteet/_malli/harjoite.md` → `harjoitteet/<tunniste>/harjoite.md` ja täytä.
- Valmennuspisteet kirjoitetaan pelin keskuksen roolien kautta.
- Jos käyttäjä haluaa kaavion, käytä harjoitekaavio-skilliä ja kirjastoa `tools/kaavio.py`;
  tallenna `kaavio.svg` ja `piirra_kaavio.py` samaan kansioon.
- Kun kaavio on, lisää `harjoite.md`:hen pääotsikon alle kuvaviittaus
  `![<nimi>](kaavio.svg)`. Jos kaaviota ei ole, poista pohjan kuvaviittausrivi.
- Helpotukset ja vaikeutukset tarvittaessa `variaatiot.md`:hen.

## 5. Älä kirjoita
Pelaajien nimiä tai muita joukkuekohtaisia tietoja – repo on julkinen.

Älä myöskään kirjoita harjoitteen tiedostoihin viittauksia lähdemateriaaliin tai
merkintöjä kuten "oma lisäys" tai "ei lähteessä". Kerro arvaukset ja omat lisäykset
käyttäjälle luonnosta esitellessäsi, mutta julkaistava teksti kirjoitetaan valmiina
harjoitteena.
