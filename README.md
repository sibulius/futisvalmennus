# Futisvalmennus – harjoitepankki

Avoin jalkapallon harjoitepankki valmentajille. Harjoitteet luokitellaan pelin
vaiheiden, alavaiheiden, pelin keskuksen roolien, kenttäalueiden ja kaistojen
mukaan, jotta niitä voi hakea ja yhdistellä harjoituspäiviksi.

## Luokittelu lyhyesti

| Vaihe | Alavaiheet |
|---|---|
| Hyökkääminen | avaaminen, rakentaminen, murtautuminen, viimeistely |
| Puolustaminen | prässääminen, keskialueen puolustaminen, syvyyden puolustaminen, maalin puolustaminen |
| Siirtymä hyökkäykseen | vastahyökkäys, pallon turvaaminen |
| Siirtymä puolustukseen | vastaprässi, uudelleenjärjestäytyminen |
| Vakiotilanne | kulmapotku, vapaapotku, rajaheitto, maalipotku, aloitus, rangaistuspotku |

- **Pelin keskus:** 1H, 2H, 3H (hyökätessä) ja 1P, 2P, 3P (puolustaessa)
- **Kenttäalueet:** oma kolmannes, keskikolmannes, hyökkäyskolmannes, rangaistusalue
- **Kaistat:** VLK, VSLK, KK, OSLK, OLK

Täydet määritelmät ja säännöt: [`sanasto.yml`](sanasto.yml).

## Uuden harjoitteen lisääminen

1. Kopioi `harjoitteet/_malli/` uudeksi kansioksi, jonka nimi on harjoitteen tunniste.
2. Täytä frontmatter `sanasto.yml`:n arvoilla ja kirjoita kuvaus.
3. Lisää halutessasi `kaavio.svg` ja `variaatiot.md`.

4. Aja tarkistus: `pip install pyyaml jsonschema && python tools/tarkista.py`

Claude Codella sama hoituu `harjoite-laadinta`-skillillä. GitHub Actions ajaa
tarkistuksen jokaisesta pushista ja pull requestista.

## Lisenssit

- Harjoitteet ja sanasto: [CC BY 4.0](LICENSE)
- Skillit (`.claude/skills/`): [MIT](LICENSE-skills)
