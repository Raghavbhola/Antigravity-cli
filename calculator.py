import math
import sys

def print_header():
    print("=" * 45)
    print("         PYTHON INTERACTIVE CALCULATOR         ")
    print("=" * 45)
    print("Supported Operations:")
    print("  [+] Addition        [-] Subtraction")
    print("  [*] Multiplication  [/] Division")
    print("  [^] Exponentiation  [%] Modulo")
    print("  [r] Square Root     [q] Quit")
    print("=" * 45)

def get_number(prompt):
    while True:
        try:
            val = input(prompt).strip()
            if val.lower() == 'q':
                return 'q'
            # Convert to float, but show as int if it's a whole number
            num = float(val)
            return int(num) if num.is_integer() else num
        except ValueError:
            print("Error: Invalid number. Please try again.")

def format_num(val):
    if isinstance(val, (int, float)):
        return int(val) if float(val).is_integer() else val
    return val

def main():
    while True:
        print_header()
        
        op = input("Choose an operator (+, -, *, /, ^, %, r) or 'q' to quit: ").strip().lower()
        if op == 'q':
            print("\nThank you for using the Python Interactive Calculator. Goodbye!")
            sys.exit(0)
            
        if op not in ['+', '-', '*', '/', '^', '%', 'r']:
            print("Error: Invalid operator chosen. Please select from the list.")
            input("\nPress Enter to continue...")
            continue
            
        if op == 'r':
            num = get_number("Enter the number: ")
            if num == 'q':
                print("\nThank you for using the Python Interactive Calculator. Goodbye!")
                sys.exit(0)
            if num < 0:
                print("Error: Cannot take the square root of a negative number in real numbers.")
            else:
                result = math.sqrt(num)
                print(f"\nResult: √{format_num(num)} = {format_num(result)}")
        else:
            num1 = get_number("Enter the first number: ")
            if num1 == 'q':
                print("\nThank you for using the Python Interactive Calculator. Goodbye!")
                sys.exit(0)
                
            num2 = get_number("Enter the second number: ")
            if num2 == 'q':
                print("\nThank you for using the Python Interactive Calculator. Goodbye!")
                sys.exit(0)
                
            n1_f = format_num(num1)
            n2_f = format_num(num2)
            
            if op == '+':
                result = num1 + num2
                print(f"\nResult: {n1_f} + {n2_f} = {format_num(result)}")
            elif op == '-':
                result = num1 - num2
                print(f"\nResult: {n1_f} - {n2_f} = {format_num(result)}")
            elif op == '*':
                result = num1 * num2
                print(f"\nResult: {n1_f} * {n2_f} = {format_num(result)}")
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    result = num1 / num2
                    print(f"\nResult: {n1_f} / {n2_f} = {format_num(result)}")
            elif op == '^':
                try:
                    result = math.pow(num1, num2)
                    print(f"\nResult: {n1_f} ^ {n2_f} = {format_num(result)}")
                except OverflowError:
                    print("Error: Result is too large (Overflow).")
                except ValueError:
                    print("Error: Invalid operation (e.g., negative base with fractional exponent).")
            elif op == '%':
                if num2 == 0:
                    print("Error: Modulo by zero is undefined.")
                else:
                    result = num1 % num2
                    print(f"\nResult: {n1_f} % {n2_f} = {format_num(result)}")
                    
        input("\nPress Enter to continue...")
        print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCalculator terminated. Goodbye!")
