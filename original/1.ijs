NB. Part 1
cons_sum =. [: +/ 2 (=/ * {.)\ ] , {.
answer =. [: cons_sum "."0

NB. Part 2
cons_sum_2 =. (# % 2:) ([: +/ ] * ] = |.) ]
answer =. [: cons_sum_2 "."0
