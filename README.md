# Lab 08 – Salted Hashes

Password-hash recovery investigation for the **Secure Communication and Cryptography** module (MSc Cyber Security, TU Dublin).

The scripts recover salted SHA-1 password hashes from a database dump, given the clues in the lab brief. The confirmed construction is `SHA1(salt + password)` with the shared salt `www.exploringsecurity.com`.

## Files

| File | Purpose |
|------|---------|
| `hashes.txt` | The six `username:hash` pairs from the database dump |
| `02_hash_type_check.py` | Checks each hash is 40-char hexadecimal (SHA-1 candidate) |
| `03_salt_test.py` | Tests the suspected salt; brute-forces 5–7 digit numeric passwords |
| `04_numeric_results.py` | Re-hashes and verifies the recovered numeric passwords |
| `05_alphanumeric_dictionary.py` | Filtered dictionary attack on the newer alphanumeric accounts |
| `06_username_mutation_attack.py` | Username-derived candidate passwords (case, reversal, numbers, leetspeak) |
| `08_word_number_attack.py` | Word + number targeted attack on the remaining accounts |
| `18_final_results.py` | Final independent verification of every recovered password |
| `07_remaining_john.txt` | John the Ripper input – two unrecovered hashes (dynamic SHA-1) |
| `15_jillc_only.txt` | John the Ripper input – JillC hash only (incremental attack) |

> Note: `05_alphanumeric_dictionary.py` expects a filtered wordlist `05_candidates_5_7.txt` and `08_word_number_attack.py` expects `rockyou.txt`; these large wordlists are not included.

## Results (5 of 6 recovered)

| Username | Password | Status |
|----------|----------|--------|
| Sparky | Admin09 | Verified |
| Mark123 | Mark123 | Verified |
| superman | qwerty | Verified |
| security | 121298 | Verified |
| Tomtom | 54321 | Verified |
| JillC | — | Not recovered |

## Usage

```bash
python3 02_hash_type_check.py    # identify hash type
python3 03_salt_test.py          # confirm salt + crack numeric passwords
python3 18_final_results.py      # verify all recovered passwords
```

## Team

- Ram Siddharth Ramasamy Raja – A00083573
- Jeyanth Kannan – A00083529
