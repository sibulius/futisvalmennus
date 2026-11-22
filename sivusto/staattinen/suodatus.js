// Harjoitelistan suodatus. Valinnat tallentuvat osoitteeseen (?vaihe=…&alue=…),
// joten suodatetun näkymän voi jakaa linkkinä.
(function () {
  const lomake = document.getElementById("suodattimet");
  const kortit = Array.from(document.querySelectorAll("#lista .kortti"));
  const maara = document.getElementById("maara");
  const tyhja = document.getElementById("tyhja");
  const alavaihe = lomake.elements.alavaihe;
  const kentat = ["haku", "vaihe", "alavaihe", "alue", "tilanne", "rooli",
                  "paineistaminen", "ika", "kaista", "kesto", "pelaajat"];

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
    for (const k of ["vaihe", "alavaihe", "alue", "tilanne", "paineistaminen"]) {
      if (a[k] && d[k] !== a[k]) return false;
    }
    if (a.rooli && !lista(d.roolit).includes(a.rooli)) return false;
    if (a.ika && !lista(d.ika).includes(a.ika)) return false;
    if (a.kaista && !lista(d.kaistat).includes(a.kaista)) return false;
    if (a.kesto && Number(d.kesto) > Number(a.kesto)) return false;
    if (a.pelaajat && Number(d.pelaajat) > Number(a.pelaajat)) return false;
    return true;
  }

  // Alavaihevalikossa näytetään vain valitun vaiheen alavaiheet.
  function paivitaAlavaiheet() {
    const vaihe = lomake.elements.vaihe.value;
    for (const opt of alavaihe.options) {
      if (!opt.value) continue;
      opt.hidden = opt.disabled = !!vaihe && opt.dataset.vaihe !== vaihe;
    }
    if (alavaihe.selectedOptions[0] && alavaihe.selectedOptions[0].disabled) alavaihe.value = "";
  }

  function paivita(tallenna) {
    paivitaAlavaiheet();
    const a = arvot();
    let n = 0;
    for (const k of kortit) {
      const nakyy = sopii(k.dataset, a);
      k.hidden = !nakyy;
      if (nakyy) n++;
    }
    maara.textContent = n + " / " + kortit.length + " harjoitetta";
    tyhja.hidden = n !== 0;
    if (tallenna) {
      const q = new URLSearchParams(a).toString();
      history.replaceState(null, "", q ? "?" + q : location.pathname);
    }
  }

  // Lue alkutila osoitteesta. Valinnaksi kelpaa vain valikossa oleva arvo.
  const q = new URLSearchParams(location.search);
  for (const k of kentat) {
    const el = lomake.elements[k];
    if (!el || !q.has(k)) continue;
    if (el.tagName === "SELECT" && !Array.from(el.options).some((o) => o.value === q.get(k))) continue;
    el.value = q.get(k);
  }
  // Alavaihe-linkki valitsee myös vaiheen.
  if (alavaihe.value && !lomake.elements.vaihe.value) {
    lomake.elements.vaihe.value = alavaihe.selectedOptions[0].dataset.vaihe;
  }

  lomake.addEventListener("input", () => paivita(true));
  lomake.addEventListener("change", () => paivita(true));
  lomake.addEventListener("reset", () => setTimeout(() => paivita(true), 0));
  lomake.addEventListener("submit", (e) => e.preventDefault());
  paivita(false);
})();
