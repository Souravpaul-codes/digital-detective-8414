# Mission 5 — Numbers and data

## 1. Task / objective
Convert numbers between decimal, binary and hexadecimal by hand, verify with Python, build a number converter program and explain text encoding.

## 2. Work completed
- Did manual number conversions with step-by-step working
- Verified all conversions using Python
- Built `number_converter.py` and tested with 3 inputs
- Explained ASCII, UTF-8 and text encoding

## 3. Commands / tools used

| Command / function | Purpose |
|-------------------|---------|
| `python3` | Opened the Python interactive shell to verify conversions |
| `bin()` | Python built-in that converts a decimal number to binary string |
| `hex()` | Python built-in that converts a decimal number to hexadecimal string |
| `int("1010", 2)` | Converts a binary string to decimal |
| `int("1F", 16)` | Converts a hexadecimal string to decimal |
| `input()` | Gets user input in the converter program |
| `ord()` | Returns the ASCII code of a character |
| `python3 number_converter.py` | Runs the converter program |

## 4. My understanding

### Task 5.1 — Manual number conversions

**Convert decimal 13 to binary:**
```
13 ÷ 2 = 6 remainder 1
6  ÷ 2 = 3 remainder 0
3  ÷ 2 = 1 remainder 1
1  ÷ 2 = 0 remainder 1
Read remainders bottom to top: 1101
Answer: 1101
```

**Convert decimal 25 to binary:**
```
25 ÷ 2 = 12 remainder 1
12 ÷ 2 = 6  remainder 0
6  ÷ 2 = 3  remainder 0
3  ÷ 2 = 1  remainder 1
1  ÷ 2 = 0  remainder 1
Read remainders bottom to top: 11001
Answer: 11001
```

**Convert binary 1010 to decimal:**
```
1×2³ + 0×2² + 1×2¹ + 0×2⁰
= 1×8 + 0×4 + 1×2 + 0×1
= 8 + 0 + 2 + 0
Answer: 10
```

**Convert binary 1101 to decimal:**
```
1×2³ + 1×2² + 0×2¹ + 1×2⁰
= 1×8 + 1×4 + 0×2 + 1×1
= 8 + 4 + 0 + 1
Answer: 13
```

**Convert hexadecimal A to decimal:**
```
A = 10 in decimal
Answer: 10
```

**Convert hexadecimal 1F to decimal:**
```
1×16¹ + F×16⁰
= 1×16 + 15×1
= 16 + 15
Answer: 31
```

**Convert binary 1111 to hexadecimal:**
```
1111 in decimal = 1×8 + 1×4 + 1×2 + 1×1 = 15
15 in hex = F
Answer: F
```

### Task 5.2 — Python verification

| Expression | Python result | Matches manual? |
|-----------|---------------|-----------------|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `hex(10)` | `0xa` | Yes (A = a) |
| `int("1F", 16)` | `31` | Yes |
| `hex(15)` | `0xf` | Yes (F = f) |

All results matched my manual calculations. Python adds `0b` prefix for binary and `0x` prefix for hex.

### Task 5.3 — Number converter program

The program (`number_converter.py`) asks the user for a decimal number, then uses `bin()` and `hex()` to convert and display results.

**Test runs:**

| Test number | Binary output | Hexadecimal output |
|------------|---------------|-------------------|
| 10 | 0b1010 | 0xa |
| 255 | 0b11111111 | 0xff |
| 42 | 0b101010 | 0x2a |

- `bin()` converts a decimal integer to its binary representation as a string with `0b` prefix
- `hex()` converts a decimal integer to its hexadecimal representation as a string with `0x` prefix

### Task 5.4 — How is text stored?

- The ASCII decimal code for uppercase **A** is **65**
- The ASCII decimal code for lowercase **a** is **97**

**Why computers need encoding:** A computer can only store numbers (bits). An encoding standard like ASCII or UTF-8 is a lookup table that maps each character to a specific number. Without it, the computer would not know what number represents which letter.

**Character not in basic ASCII:** The emoji 😊 is not part of basic ASCII. It needs UTF-8 (or Unicode) encoding to be stored and displayed.

## 5. Difficulties faced
I initially forgot that Python adds `0b` and `0x` prefixes to binary and hex outputs, so my first comparison looked wrong.

## 6. How I resolved them
I realised the prefixes are just labels — the actual digits matched my manual answers. So `0b1101` is the same as `1101` in binary.

## 7. Evidence / files
- `number_converter.py` — working Python converter program
- This README with all manual calculations, Python verification and test results

## 8. Commit details
- Commit message: **"Build number converter and practise data representation"**
- Pushed to GitHub and verified.
