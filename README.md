# Montana Counties License Plate Lookup 

**Author:** Molly O'Connor  
**Date:** January 22, 2026  

##  Project Overview

This Python program allows users to look up **Montana counties** based on the **numeric prefix** found on standard (non‑personalized) Montana license plates.

In Montana, each of the state's **56 counties** is represented by a unique number that appears at the beginning of a license plate. For example:

- `1-AAA12345` → **Butte-Silver Bow County**
- `5-BBB98765` → **Lewis and Clark County**
- `12-12345AB` → **Hill County**

This program lets users:
- Enter a license plate prefix (1–56)
- Choose what information to display:
  - County name
  - County seat
  - Both
- Make unlimited queries until they choose to exit

County data is loaded from a CSV file and stored in a dictionary for fast and efficient lookups.

---

## Files Included

- `main.py` (or your Python file name)
- `MontanaCounties.csv` – contains:
  - `prefix`
  - `county`
  - `county_seat`
- `README.md`

---

## How It Works

1. The program reads county data from `MontanaCounties.csv`.
2. Data is stored in a dictionary using the license plate prefix as the key:
   ```python
   { prefix: (county_name, county_seat) }
   ```
3. The user is prompted to:
   - Start or exit the program
   - Enter a county prefix (1–56)
   - Choose what information to display (`c`, `s`, or `b`)
4. The program continues running until the user types `x` to exit.

---

##  How to Run

1. Make sure you have **Python 3** installed.
2. Place `MontanaCounties.csv` in the same directory as the Python file.
3. Run the program:

```bash
python main.py
```

4. Follow the on-screen prompts.

---

##  Example Interaction

```text
Ready to play? (type y/n): y
Please enter a number (1-56) or type 'x' to exit: 5
What information would you like? County ('c'), Seat ('s'), or Both ('b'): b

License plate prefix number 5
County: Lewis and Clark --- County Seat: Helena
```

---
