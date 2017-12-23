# The way you're supposed to do today's part 2 is to read obfuscated
# assmebly. The outer loop goes from b to c, incrementing by 17 each time
# (so iterating 1000 times). There are two inner loops which consist of
# taking the product of d and e which are two arbitrary numbers in the 
# range [2, b] and subtracting that from b. f is set to zero 
# if and only if d*e ever equals b, so this is a brute-force primality test,
# since if f is 0, h is incremented (the output we want is the value of h).
set b 67
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
