# DecodeLabs Project 1: Password Strength Checker

## ⚙️ Project Overview
This project serves as a defensive security component designed to evaluate string entropy and categorize password risk classifications into **Weak**, **Medium**, or **Strong** states. The program implements optimization boundaries to remain highly resilient under processing loads.


### 1. Computational Efficiency ($O(n)$ Complexity)
Instead of relying on heavy, non-optimized manual loops that introduce excessive processing overhead, this application utilizes C-optimized string-handling methods coupled with short-circuiting logical expressions (`any()`). This ensures validation execution scales linearly with the input byte stream.

### 2. Character Space Expansion (Unicode Entropy)
Rather than restricting validation to standard 95-character printable ASCII spaces, the logic leverages native character property methods. This expands the defensive pattern evaluation to over 143,000+ characters within the Unicode space, capturing localized and complex character vectors accurately.

---

## 🛡️ Defensive Security Analysis: Volatile Memory Safety

### The Vulnerability: Data in RAM (Page 10 Mitigation)
In standard Python development, strings are **immutable** (they cannot be modified or cleared in place within memory addresses). When a user inputs a password, that plain-text string lingers inside the system's heap memory until the Python Garbage Collector completely wipes it. 

During this window, a security risk known as **RAM Scraping** (e.g., malware like *BlackPOS*) can scan the active memory space and extract the plain-text password directly from RAM.

### Production Mitigation Strategy
To address this volatile security trap in a real-world enterprise production environment, we implement the following:
1. **Use Mutable Data Structures:** Instead of a standard string, user input should be ingested directly into a mutable structure like a `bytearray`.
2. **Immediate Zeroing-Out:** As soon as the password strength evaluation or authentication logic is complete, the `bytearray` must be explicitly overwritten with zeros (`0x00`) in memory, ensuring the plain text never lingers for malware to capture.