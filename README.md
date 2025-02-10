# Zápočtový program

## Specifikace

Program za vstup berie počet rovníc ktoré chce užívateľ zadať, následne užívateľ zadáva rovnice. Program "očistí" vstup a vytvorí z neho maticu. Najskôr vykonáva Gaussovu elimínáciu, pri ktorej nedochádza k chybám zaokrúhlovania, následne sa spúšta spatná substitúcia, kde program vie zistiť, že matica nie je regulárna a jej  riešenie teda "neexistuje". Na konci prichádza jednoduchý konzolový výpis s hodnotou každej premennej.

## Instalace a spuštění

Jediný vstup užívateľa je konzolový. Doležitý dodatok k vstupu; každá nula musí byť explicitne napisaná napr. 0x, v prípade jednotky to neplatí, x <=> 1x.

Program se spustí příkazem: `python LINEAR_EQUATIONS.py`

## Dokumentace
* [Uživatelská dokumentace](docs/user.md)
* [Ukázky použití](docs/examples.md)
* [Programátorská dokumentace](docs/programmer.md)
