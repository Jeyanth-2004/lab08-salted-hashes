#!/usr/bin/env python3
"""
Lab 08 - Salted Hashes
Independent verification of the recovered JillC password.

JillC was the last account recovered, using a John the Ripper
mixed-position mask (?u?d?l?d?d?l?u). This script re-hashes the
recovered password with the known salt and checks it against the
original stored hash.
"""
import hashlib

SALT = "www.exploringsecurity.com"            # common salt (from the case file)
JILLC_HASH = "f44f3b09df53c1c11273def13cacd8922a86d48c"
JILLC_PASSWORD = "Q2w13sA"                     # recovered via mask ?u?d?l?d?d?l?u

def salted_sha1(salt, password):
    return hashlib.sha1((salt + password).encode()).hexdigest()

if __name__ == "__main__":
    calc = salted_sha1(SALT, JILLC_PASSWORD)
    ok = calc == JILLC_HASH
    print("LAB 08 - JillC VERIFICATION")
    print("-" * 40)
    print(f"Username : JillC")
    print(f"Password : {JILLC_PASSWORD}")
    print(f"Salt     : {SALT}")
    print(f"SHA1     : {calc}")
    print(f"Stored   : {JILLC_HASH}")
    print(f"Verified : {ok}")
