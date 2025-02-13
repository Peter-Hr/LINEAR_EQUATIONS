# Ukázky použití

Vstup zdávam v tvare: 
* Počet rovníc - jeden riadok
* Každá dalšia rovnica v novom riadku

## Vstupy 
### 2 rovnice o dvoch neznámich(nuly)
* `2`
* `y=5`
* `x=6`
##### Vystup
* x = 6.0
* y = 5.0
* Unique solution
### 2 rovnice o dvoch neznámich
* `2`
* `-x+3y=5`
* `4x+y=6`
##### Vystup
* x = 1.0
* y = 2.0
* Unique solution
### 3 rovnice bez riešenia
* `3`
* `x+y+z=3`
* `2x+2y+2z=6`
* `3x+3y+3z=12`
##### Vystup
* No solution
### 4 rovnice s riešením
* `4`
* `2x+3y-z+4w=10`
* `4x-y+5z-2w=5`
* `3w+2z+6y-x=8`
* `3x-2y+4z+w=7`
##### Vystup 
* w = 1.53
* x = 1.37
* y = 0.59
* z = 0.63
* Unique solution
### 3 rovnice s parametrizovaným riešením
* `3`
* `2x+3y-z=5`
* `-4y+z=-2`
* `0x=0`
##### Vystup 
* x = (5.0-(3.0)*y-(-1.0)*z)/2.0
* y = (-4.0-(2.0)*z)/-8.0  
* z = z
* Infinite solutions
### 2 rovnice s parametrizovaným riešením
* `2`
* `8z+3y+1x-9=0`
* `2z-4=0`
##### Vystup 
* x = (9.0-(3.0)*y-(8.0)*z)/1.0
* z = (4.0)/2.0
* y = y
* Infinite solutions