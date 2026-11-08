# Lab 08 – Salted Hashes

Password-hash recovery investigation for the **Secure Communication and Cryptography** module (MACS H6014, MSc Cyber Security, TU Dublin).

The scripts recover salted SHA-1 password hashes from a database dump, given the clues in the lab brief. The confirmed construction is `SHA1(salt + password)` with the shared salt `www.exploringsecurity.com`.

## Files

| File | Purpose |
|------|---------|
| `hashes.txt` | The six `username:hash` pairs from the database dump |
| `02_hash_type_check.py` | Checks each hash is 40-char hexadecimal (SHA-1 candidate) |
| `03_salt_test.py` | Tests the suspected salt; brute-forces 5–7 digit numeric passwords |
| `04_numeric_results.py` | Re-hashes and verifies the recovered numeric passwords |
| `05_alphanumeric_dictionary.py` | Filtered dictionary attack on the newer alphanumeric accounts |
| `06_username_mutation_attack.py` | Username-derived candidate passwords |
| `08_word_number_attack.py` | Word + number targeted attack on the remaining accounts |
| `18_final_results.py` | Final verification of every recovered password |
| `jillc_verification.py` | Independent verification of JillC → `Q2w13sA` |
| `07_remaining_john.txt` | John the Ripper input – unrecovered hashes (dynamic SHA-1) |
| `15_jillc_only.txt` | John the Ripper input – JillC hash only (mask attack) |

## Results (6 of 6 recovered)

| Username | Password | Method | Status |
|----------|----------|--------|--------|
| Tomtom | 54321 | numeric brute force | Verified |
| security | 121298 | numeric brute force | Verified |
| superman | qwerty | filtered dictionary | Verified |
| Mark123 | Mark123 | filtered dictionary | Verified |
| Sparky | Admin09 | mask `?u?l?l?l?l?d?d` | Verified |
| JillC | Q2w13sA | mask `?u?d?l?d?d?l?u` | Verified |

All six passwords were recovered and independently verified against the stored hashes.

## Team

- Ram Siddharth Ramasamy Raja – A00083573
- Jeyanth Kannan – A00083529
