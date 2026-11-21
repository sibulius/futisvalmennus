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
- Yksi päävaihe ja yksi alavaihe.
- Roolit kuuluvat vaiheen `sallitut_roolit`-listaan.
- Tilanteen lukumäärä ja roolit eivät ole ristiriidassa (2v1 → 1H, 2H vs. 1P).
- Kaistat vain, jos harjoite kohdistuu niihin; vasen/oikea hyökkäyssuuntaan.
- Vakiotilanteissa `puoli` ja `tehtavat`.

## 4. Luo tiedostot
- Tunniste: pienet kirjaimet, ei ääkkösiä, väliviivat. Tarkista, ettei kansiota ole jo.
- Kopioi `harjoitteet/_malli/harjoite.md` → `harjoitteet/<tunniste>/harjoite.md` ja täytä.
- Valmennuspisteet kirjoitetaan pelin keskuksen roolien kautta.
- Jos käyttäjä haluaa kaavion, käytä harjoitekaavio-skilliä ja tallenna `kaavio.svg` samaan kansioon.
- Helpotukset ja vaikeutukset tarvittaessa `variaatiot.md`:hen.

## 5. Älä kirjoita
Pelaajien nimiä tai muita joukkuekohtaisia tietoja – repo on julkinen.
