class Calculator:
    @staticmethod
    def add(a, b):
        if not isinstance(a, (int, float)):
            raise ValueError
        if not isinstance(b, (int, float)):
            raise ValueError
        return a + b

    @staticmethod
    def mul(a, b):
        if not isinstance(a, (int, float)):
            raise ValueError
        if not isinstance(b, (int, float)):
            raise ValueError
        return a * b


if __name__ == "__main__":
    print(Calculator.add(5, 6))  # 11
    print(Calculator.mul(5, 6))  # 30
