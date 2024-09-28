def are_brackets_balanced(expression):
    stack = []
    # Відповідність відкриваючих і закриваючих дужок
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for char in expression:
        # Якщо це відкриваюча дужка, додаємо до стеку
        if char in '([{':
            stack.append(char)
        # Якщо це закриваюча дужка
        elif char in ')]}':
            # Перевіряємо, чи є стек пустим або чи є верхній елемент стеку відповідною відкриваючою дужкою
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    # Якщо стек порожній, всі дужки були збалансовані
    return not stack

if __name__ == "__main__":
    example_expression = "( { [ ] ( 1 + 3 ) } )"
    result = are_brackets_balanced(example_expression)
    print(f"'{example_expression}': {'Симетрично' if result else 'Несиметрично'}")