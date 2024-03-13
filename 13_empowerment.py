# Create a method that obtains the result of raising one number to another, both 
# numbers must be passed as parameters.
class Calculator:
    def empowerment_recursive(self, base, exponent):
        if exponent >= 1:
            if exponent == 1:
                    return base    
                
            return base * self.empowerment_recursive(base, exponent - 1)
        
        if exponent <= 0: 
            exponent = abs(exponent)   
            if exponent == 0:
                    return 0    
                
            return 1 / (base * self.empowerment_recursive(base, exponent - 1))


calculator = Calculator()

print(f"3^9 = {calculator.empowerment_recursive(3, 9)}.")
print(f"3^-9 = {calculator.empowerment_recursive(3, -9)}.")
print(f"-3^9 = {calculator.empowerment_recursive(-3, 9)}.")
print(f"-3^-9 = {calculator.empowerment_recursive(-3, -9)}.")