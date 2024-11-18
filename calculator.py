class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        # รองรับกรณีที่ b < 0
        negative_result = False
        if b < 0:
            b = -b
            negative_result = True
        
        result = 0
        for _ in range(b):
            result = self.add(result, a)

        if negative_result:
            return -result
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        result = 0
        is_negative = (a < 0) != (b < 0)  # ตรวจสอบว่าผลลัพธ์ควรเป็นลบหรือไม่
        a, b = abs(a), abs(b)

        while a >= b:
            a = self.subtract(a, b)
            result += 1

        return -result if is_negative else result
    
    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo with zero")

        is_negative = a < 0
        a, b = abs(a), abs(b)

        while a >= b:
            a = self.subtract(a, b)

        return -a if is_negative else a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))           # 3
    print("Example: subtraction: ", calc.subtract(4, 2))  # 2
    print("Example: multiplication: ", calc.multiply(2, 3))  # 6
    print("Example: division: ", calc.divide(10, 2))      # 5
    print("Example: modulo: ", calc.modulo(10, 3))        # 1
