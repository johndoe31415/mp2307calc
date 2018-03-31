# mp2307calc
This is a small tool to calculate resistance values required to get a certain
voltage from the MP2307 switched mode power supply IC (3A, 23V, 340kHz
synchronous rectified step-down converter). 

## Mini-360 module
The MP2307 appears as part of the popular "Mini-360" mini regulator boards that
can be found all over eBay. Sometimes they're also erroneously called
"Mini-LM2596" even though they have nothing to do with the LM2596 (just
piggybacking on the popularity of the LM2596).

I discovered that some of these modules are populated with underpowered
components and are faulty, reducing in extreme loss of efficiency (in bad cases
even worse efficiency than a linear regulator). To detect if your Mini-360 is
faulty, I've created a [page that shows exactly what to look out
for](https://johndoe31415.github.io/mp2307calc/).

## Successor
This script is just a one-trick pony. If you're looking for something more
beautiful, more powerful and usable, check out my PyEngineer project. It also
can perform MP2307 calculations, but can do much more on top that's handy for
electronics engineering. [Here are some screenshots so you can get an idea of
how it looks.](https://johndoe31415.github.io/pyengineer/) [And this is the PyEngineer
project page.](https://github.com/johndoe31415/pyengineer/)

## Documentation
  * [Datasheet for MP2307](https://www.monolithicpower.com/pub/media/document/MP2307_r1.9.pdf)
  * [Schematic of Mini-360 and component placement](https://johndoe31415.github.io/mp2307calc/)
  * [PyEngineer Screenshots](https://johndoe31415.github.io/pyengineer/)

## Running the script
Running it is dead simple, you can simply give it a value for R2 that you like
(by default 10k are assumed):

```
$ ./mp2307calc.py 6800
    ----- R2 fixed at 10.0 kOhm -----
  1.0 V: R1 = 811 Ohm (820 Ohm -> 1.0 V)
  1.8 V: R1 = 9459 Ohm (10000 Ohm -> 1.9 V)
  2.0 V: R1 = 11622 Ohm (12000 Ohm -> 2.0 V)
  3.0 V: R1 = 22432 Ohm (22000 Ohm -> 3.0 V)
  3.3 V: R1 = 25676 Ohm (27000 Ohm -> 3.4 V)
  4.0 V: R1 = 33243 Ohm (33000 Ohm -> 4.0 V)
  5.0 V: R1 = 44054 Ohm (47000 Ohm -> 5.3 V)
  6.0 V: R1 = 54865 Ohm (56000 Ohm -> 6.1 V)
  7.0 V: R1 = 65676 Ohm (68000 Ohm -> 7.2 V)
  8.0 V: R1 = 76486 Ohm (82000 Ohm -> 8.5 V)
  9.0 V: R1 = 87297 Ohm (82000 Ohm -> 8.5 V)
 10.0 V: R1 = 98108 Ohm (100000 Ohm -> 10.2 V)
 11.0 V: R1 = 108919 Ohm (100000 Ohm -> 10.2 V)
 12.0 V: R1 = 119730 Ohm (120000 Ohm -> 12.0 V)
 13.0 V: R1 = 130541 Ohm (120000 Ohm -> 12.0 V)
 14.0 V: R1 = 141351 Ohm (150000 Ohm -> 14.8 V)
 15.0 V: R1 = 152162 Ohm (150000 Ohm -> 14.8 V)
```

It'll also calculate for variable values of R2 the ideal resistor combinations
R1/R2:

```
    ----- R1 and R2 variable -----
  1.0: R1 = 220 Ohm, R2 = 2700 Ohm -> 1.0 V (error = +0.0%)
  1.8: R1 = 1000 Ohm, R2 = 1000 Ohm -> 1.9 V (error = +2.8%)
  2.0: R1 = 3900 Ohm, R2 = 3300 Ohm -> 2.0 V (error = +0.9%)
  3.0: R1 = 2700 Ohm, R2 = 1200 Ohm -> 3.0 V (error = +0.2%)
  3.3: R1 = 10000 Ohm, R2 = 3900 Ohm -> 3.3 V (error = -0.1%)
  4.0: R1 = 3300 Ohm, R2 = 1000 Ohm -> 4.0 V (error = -0.6%)
  5.0: R1 = 12000 Ohm, R2 = 2700 Ohm -> 5.0 V (error = +0.7%)
  6.0: R1 = 8200 Ohm, R2 = 1500 Ohm -> 6.0 V (error = -0.3%)
  7.0: R1 = 10000 Ohm, R2 = 1500 Ohm -> 7.1 V (error = +1.3%)
  8.0: R1 = 12000 Ohm, R2 = 1500 Ohm -> 8.3 V (error = +4.1%)
  9.0: R1 = 33000 Ohm, R2 = 3900 Ohm -> 8.8 V (error = -2.8%)
 10.0: R1 = 10000 Ohm, R2 = 1000 Ohm -> 10.2 V (error = +1.8%)
 11.0: R1 = 10000 Ohm, R2 = 1000 Ohm -> 10.2 V (error = -7.5%)
 12.0: R1 = 12000 Ohm, R2 = 1000 Ohm -> 12.0 V (error = +0.2%)
 13.0: R1 = 15000 Ohm, R2 = 1200 Ohm -> 12.5 V (error = -3.9%)
 14.0: R1 = 47000 Ohm, R2 = 3300 Ohm -> 14.1 V (error = +0.7%)
 15.0: R1 = 15000 Ohm, R2 = 1000 Ohm -> 14.8 V (error = -1.3%)
```

Note that modifying the script is trivial as well. It chooses by default resistory from the E12 series:

```
e_series = ESeries.standard(12)
```

And calculates a set of voltages:

```
voltages = [ 1, 1.8, 2, 3, 3.3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
```

That can be modified as you see fit. Have fun!

## License
GNU GPL-3.
