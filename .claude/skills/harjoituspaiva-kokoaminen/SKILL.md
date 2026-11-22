---
name: harjoituspaiva-kokoaminen
description: Kokoa harjoituspäivä harjoitepankin harjoitteista annetun teeman, keston ja pelaajamäärän perusteella. Käytä, kun käyttäjä pyytää harjoitusta, harjoituspäivää tai harjoitusrunkoa.
---

# Harjoituspäivän kokoaminen

## 1. Lähtötiedot
Selvitä: teema (vaihe/alavaihe, pelin keskuksen tilanne), kokonaiskesto,
pelaajamäärä, ikäluokka ja käytettävissä oleva kenttä. Lue `sanasto.yml`.

## 2. Hae harjoitteet
Suodata `harjoitteet/*/harjoite.md` frontmatterin perusteella. Ohita `_malli`.
Alavaiheella haettaessa huomioi `alavaihe`-kentän lisäksi `myos_alavaiheet`.

## 3. Rakenna eteneminen
- Tekniikkaharjoitteet (`vaihe: tekniikka`) sopivat lämmittelyyn tai rastiksi,
  kun teeman taito (alavaihe, esim. `vastaanotto`) vastaa harjoituspäivän teemaa.
- Alkulämmittelyharjoitteet (`vaihe: alkulammittely`) harjoituksen alkuun ja
  fysiikkaharjoitteet (`vaihe: fysiikka`) teeman mukaan, esim. nopeus heti
  lämmittelyn jälkeen ja kestävyys loppuun.
- Lämmittely → pienestä keskuksesta (1v1, 2v1) laajempaan (3v2, 3v3) → peli.
- Hyödynnä `vastinpari`-kenttää: pelissä toinen joukkue harjoittelee alavaihetta,
  toinen sen vastinparia.
- Kestojen summa = kokonaiskesto; varaa aikaa siirtymiin ja juomatauoille.

## 4. Tulos
Listaa harjoitteet järjestyksessä: aika, tunniste, nimi, kesto, painopiste.
Viittaa harjoitteisiin tunnisteella – älä kopioi niiden sisältöä.
Jos pankista puuttuu sopiva harjoite, ehdota uuden laatimista harjoite-laadinta-skillillä.
