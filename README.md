                                                           DecodeLabs_Internship Projects


Project 1: Password Strength Analyzer

Overview:
An advanced, real-time security application designed to analyze password complexity and evaluate risk classification. Instead of utilizing traditional, performance-heavy loops, this tool features highly optimized Pythonic built-ins to process logic strings instantaneously.

Key Features:
Real-Time Entropy Tracking:Built using an interactive graphical arc gauge that visually updates its coverage based on the password strength score.
Live Compliance Checklist:Dynamic checkboxes that instantly verify password length and the inclusion of numbers, uppercase letters, and special symbols as the user types.
Security Masking:** Implements secure character masking (`*`) within the input credential string field to ensure shoulder-surfing protection.

Logic & Classification:
1. Immediate Length Validation:** Passwords under 8 characters receive an automatic fail rating (`CRITICAL RISK ◆ WEAK`).
2. Entropy Grading:** Passwords meeting length criteria are evaluated on a 4-tier score depending on character variety, scaling seamlessly up to `ENCRYPTED ◆ STRONG` (100%).


Project 2: Cryptographic Matrix Analyzer

Overview:
A real-time data confidentiality tool implementing symmetric mono-alphabetic substitution. This application demonstrates the core mechanics of data protection in transit by encrypting plain-text streams and displaying the structural transformation of characters through mathematical shift functions.

Key Features:
Event-Driven Execution:** Integrated with key-release bindings (`<KeyRelease>`) to perform mathematical encryption on the fly without requiring explicit submission buttons.
Configurable Shift Variable:** Features an embedded, validated cipher key selector allowing shifts between 1 and 25 intervals.
Dynamic Stream Monitoring:** A visual checklist confirming successful payload loading, alphabet detection, and cipher key verification status in real time.

Mathematical Framework:
The core algorithm strictly leverages the modular arithmetic rotation formula to execute reversible data obfuscation:

$$E_n(x) = (x + n) \pmod{26}$$

Where:
* $x$ = The absolute position of the alphabetic character.
* $n$ = The user-defined cipher shift key value.
* $\pmod{26}$ = Ensures structural automated wrapping around the finite 26-letter English alphabet.
