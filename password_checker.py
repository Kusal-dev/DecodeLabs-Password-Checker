import sys

def check_password_strength(password: str) -> str:
    """
    Evaluates password strength using C-optimized linear scans O(n)
    and short-circuiting as required by DecodeLabs.
    """
    # 1. Length Verification Gate (< 8 chars is immediate fail)
    if len(password) < 8:
        return "Weak"
        
    # 2. Pattern Recognition (Using C-optimized built-ins for Unicode support)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() and not char.isspace() for char in password)
    
    # 3. Risk Classification Logic
    criteria_met = sum([has_upper, has_digit, has_symbol])
    
    if criteria_met == 3:
        return "Strong"
    elif criteria_met == 2:
        return "Medium"
    else:
        return "Weak"

if __name__ == "__main__":
    print("\n=== DECODELABS: PASSWORD STRENGTH CHECKER ===")
    
    # Allows testing directly in the terminal
    user_input = input("Enter password to evaluate: ")
    
    result = check_password_strength(user_input)
    print(f"Risk Classification Result: -> {result} <-\n")