#!/usr/bin/python3
#	mp2307calc - MP2307 switched mode IC calculator
#	Copyright (C) 2018-2018 Johannes Bauer
#
#	This file is part of mp2307calc.
#
#	mp2307calc is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	mp2307calc is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with mp2307calc; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>
import sys
from ESeries import ESeries

e_series = ESeries.standard(12)
voltages = [ 1, 1.8, 2, 3, 3.3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]

if len(sys.argv) >= 2:
	fixed_r2 = float(sys.argv[1])
else:
	fixed_r2 = 10e3


def mp2307_uout(r1, r2):
	return 0.925 * (r1 + r2) / r2

def mp2307_r1(vout, r2):
	return ((vout / 0.925) - 1) * r2

print("    ----- R2 fixed at %.1f kOhm -----" % (fixed_r2 / 1e3))
for vout in voltages:
	r1 = mp2307_r1(vout, fixed_r2)
	closest_r1 = e_series.closest(r1)
	vout_actually = mp2307_uout(closest_r1.value, fixed_r2)
	print("%5.1f V: R1 = %.0f Ohm (%.0f Ohm -> %.1f V)" % (vout, r1, closest_r1.value, vout_actually))

print()
print("    ----- R1 and R2 variable -----")
for vout in voltages:
	combinations = [ ]
	for r2 in e_series.from_to(1000, 10000):
		r1 = mp2307_r1(vout, r2)
		closest_r1 = e_series.closest(r1)
		vout_actually = mp2307_uout(closest_r1.value, r2)
		error = (vout_actually - vout) / vout
		combinations.append((error, closest_r1.value, r2))
	combinations.sort(key = lambda x: abs(x[0]))

	(error, r1, r2) = combinations[0]
	vout_actually = mp2307_uout(r1, r2)
	error = (vout_actually - vout) / vout
	print("%5.1f: R1 = %.0f Ohm, R2 = %.0f Ohm -> %.1f V (error = %+.1f%%)" % (vout, r1, r2, vout_actually, 100 * error))
