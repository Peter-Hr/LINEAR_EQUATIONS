# Programátorská dokumentace

## Hlavné funkcie
* start
* input_engine
* Gaussian_elimination
* Back_substitution
* Variables_printout

### start
Funkcia start je jediná funkcia spúštaná samostatne; jej vstup je prázdny list. Jej úlohou je spustit funkciu na vstup, následne upravený vstup vložiť do funkcie gaussovej eliminácie a výstup z nej vložiť do spatnej substitúcie, ktorej výstup následne predáva do funkcie Variables_printout
### input_engine
**Prvá** funkcia **spúštaná funckiou start**.\
**Vstup** funkcie **je matica matrix**.

**Podfunkcie:**
* handeling_of_input
* equation_input
* insert

**Výstup** funkcie **je finálna matica a set premenných**.

<details><summary>Click to expand</summary>

#### handeling_of_input
Funkcia je **volaná funkciou input_engine s paratmetrom matrix**.\
Jej úlohou je zistit od užívatela **počet rovníc a následne dané rovnice**. Fukncia spušta funkciu equation_input a následne s parametrami predanými tou funkciou spušta insert.\
**Výstup je finálna matica, a set premenných**.
##### equation_input
Funkcia **volaná funkciou handeling_of_input**.\
**Vstup je rovnica**.\
Úlohou tejto funkcie je **správne naformátovať vstup od užívateľa** t.j. oddeliť pravú stranu rovnice od tej ľavej (premenné a konštanta)
a získať všetky konštanty.\
Výstup je **zoznam touplov premenných s ich koeficientami, konštanta, set premennych**.
##### insert
Funkcia so **vstupnými parametrami terms, constant, matrix**.\
Úloha funkcie je **vložiť koeficienty premenných a konštantu na správne miesto do matice matrix**.\
Funkcia vracia maticu matrix.
</details>


