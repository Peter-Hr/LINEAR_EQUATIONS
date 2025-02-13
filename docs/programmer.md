# Programátorská dokumentace

## Hlavné funkcie
* Start
* Input_engine
* Gaussian_elimination
* Back_substitution


### Start
Funkcia Start je **jediná funkcia spúštaná samostatne**; jej **vstup je prázdny list**.\
Jej úlohou je **spustit funkciu na vstup**, následne **upravený vstup vložiť do funkcie gaussovej eliminácie** a **výstup z nej vložiť do spatnej substitúcie**, **ktorá vstup spracuje a správne interpretuje užívatelovi**.
### Input_engine
**Prvá** funkcia **spúštaná funckiou Start**.\
**Vstup** funkcie **je matica matrix**.

**Podfunkcie:**
* Handeling_of_input
* Equation_input

**Výstup** funkcie **je finálna matica a set premenných**.

<details><summary>Click to expand</summary>

#### Handeling_of_input
Funkcia je **volaná funkciou Input_engine s paratmetrom matrix**.\
Jej úlohou je zistit od užívatela **počet rovníc a následne dané rovnice**. Fukncia spušta funkciu Equation_input a následne s parametrami predanými tou funkciou vytvára maticu a set premenných.\
**Výstup je finálna matica, a set premenných**.
##### Equation_input
Funkcia **volaná funkciou Handeling_of_input**.\
**Vstup je rovnica**.\
Úlohou tejto funkcie je **správne naformátovať vstup od užívateľa** t.j. oddeliť pravú stranu rovnice od tej ľavej (premenné a konštanta)
a získať všetky konštanty.\
Výstup je **zoznam touplov premenných s ich koeficientami, konštanta, set premennych**.
</details>

### Gaussian_elimination
Funkcia berie **vstup priamo z funkcie Input_engine** t.j. **matrix**.\
**Úloha** funkcie **je upraviť maticu do trojuholníkového tvaru bez zaokrúhľovacej chyby**.
Využíva pri tom prácu s listom, a riadkové úpravy.\
**Výstup** funkcie **je matica**.

### Back_substitution
**Vstupné dáta** funkcie **sú upravená trojuholníková matica a  premenných**.
Funckia **vykonáva** obyčajnu **spatnú substituciu**, pri **ktorej môžu nastať 3 prípady**, matica **má práve jedno riešenie**, matica má **nekonečne veľa riešení** a matica **nemá riešenie**.\
Funkcia správne **vypíše výstup celého programu**.








