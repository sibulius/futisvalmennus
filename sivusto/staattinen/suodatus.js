// Harjoitelistan suodatus (vaihesivut ja Kaikki harjoitteet). Valinnat tallentuvat
// osoitteeseen (?alavaihe=…&tilanne=…), joten suodatetun näkymän voi jakaa linkkinä.
(function () {
  const lomake = document.getElementById("suodattimet");
  const kortit = Array.from(document.querySelectorAll(".kortti"));
  const ryhmat = Array.from(document.querySelectorAll(".ryhma"));
  const maara = document.getElementById("maara");
  const tyhja = document.getElementById("tyhja");
  const lisat = document.getElementById("lisasuodattimet");
  const vaiheValikko = lomake.elements.vaihe;          // vain Kaikki harjoitteet -sivulla
  const alavaihe = lomake.elements.alavaihe;          // select tai radionapit
  const kentat = ["haku", "vaihe", "alavaihe", "alue", "tilanne", "rooli",
                  "paineistaminen", "ika", "kaista", "puoli", "kesto", "pelaajat"];
  const kaikkiaan = new Set(kortit.map((k) => k.dataset.tunniste)).size;
  const lisaKentat = kentat.filter((k) => k !== "vaihe" && k !== "alavaihe");

  function arvot() {
    const a = {};
    for (const k of kentat) {
      const el = lomake.elements[k];
      if (el && el.value.trim() !== "") a[k] = el.value.trim();
    }
    return a;
  }

  function sopii(d, a) {
    const lista = (s) => (s ? s.split(" ") : []);
    if (a.haku && !d.teksti.includes(a.haku.toLowerCase())) return false;
    if (a.vaihe && !lista(d.vaiheet).includes(a.vaihe)) return false;
    if (a.alavaihe && !lista(d.alavaiheet).includes(a.alavaihe)) return false;
    for (const k of ["alue", "tilanne", "paineistaminen", "puoli"]) {
      if (a[k] && d[k] !== a[k]) return false;
    }
    if (a.rooli && !lista(d.roolit).includes(a.rooli)) return false;
    if (a.ika && !lista(d.ika).includes(a.ika)) return false;
    if (a.kaista && !lista(d.kaistat).includes(a.kaista)) return false;
    if (a.kesto && Number(d.kesto) > Number(a.kesto)) return false;
    if (a.pelaajat && Number(d.pelaajat) > Number(a.pelaajat)) return false;
    return true;
  }

  // Kaikki harjoitteet -sivulla alavaihevalikossa näytetään vain valitun vaiheen alavaiheet.
  function paivitaAlavaiheet() {
    if (!vaiheValikko || !alavaihe.options) return;
    const vaihe = vaiheValikko.value;
    for (const opt of alavaihe.options) {
      if (!opt.value) continue;
      opt.hidden = opt.disabled = !!vaihe && opt.dataset.vaihe !== vaihe;
    }
    if (alavaihe.selectedOptions[0] && alavaihe.selectedOptions[0].disabled) alavaihe.value = "";
  }

  function paivita(tallenna) {
    paivitaAlavaiheet();
    const a = arvot();
    // Sama harjoite voi olla kahdessa ryhmässä (myos_alavaiheet): lasketaan tunnisteet.
    const nakyvat = new Set();
    for (const k of kortit) {
      const nakyy = sopii(k.dataset, a);
      k.hidden = !nakyy;
      if (nakyy) nakyvat.add(k.dataset.tunniste);
    }
    const n = nakyvat.size;
    for (const r of ryhmat) r.hidden = !r.querySelector(".kortti:not([hidden])");
    maara.textContent = n + " / " + kaikkiaan + " harjoitetta";
    tyhja.hidden = n !== 0;
    if (tallenna) {
      const q = new URLSearchParams(a).toString();
      history.replaceState(null, "", q ? "?" + q : location.pathname);
    }
  }

  function kelpaa(el, arvo) {
    if (el.tagName === "SELECT") return Array.from(el.options).some((o) => o.value === arvo);
    if (el instanceof RadioNodeList) return Array.from(el).some((r) => r.value === arvo);
    return true;
  }

  // Lue alkutila osoitteesta. Valinnaksi kelpaa vain tarjolla oleva arvo.
  const q = new URLSearchParams(location.search);
  for (const k of kentat) {
    const el = lomake.elements[k];
    if (!el || !q.has(k) || !kelpaa(el, q.get(k))) continue;
    el.value = q.get(k);
  }
  if (vaiheValikko && alavaihe.value && !vaiheValikko.value) {
    vaiheValikko.value = alavaihe.selectedOptions[0].dataset.vaihe;
  }

  // Lisäsuodattimet auki leveällä näytöllä tai kun jokin niistä on käytössä.
  if (window.matchMedia("(min-width: 760px)").matches ||
      lisaKentat.some((k) => lomake.elements[k] && lomake.elements[k].value)) {
    lisat.open = true;
  }

  lomake.addEventListener("input", () => paivita(true));
  lomake.addEventListener("change", () => paivita(true));
  lomake.addEventListener("reset", () => setTimeout(() => paivita(true), 0));
  lomake.addEventListener("submit", (e) => e.preventDefault());
  paivita(false);
})();
