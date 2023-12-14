
"""
 Kilowatt = power, which is the rate that energy is generated or used.
 Kilowatt-Hour = energy, which is the rate that we use fuel over a specific period.

 P(W) = U(V) * I(A)
 E(kWh) = (P(W) * t(h)) / 1000
"""


def wattage(U, I):
    return U * I


def kilowatt_hour(P, t):
    E = (P * t) / 1000
    return E