from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру і видаляємо пробіли
    s = s.lower().replace(' ', '')
    # Створюємо двосторонню чергу (deque)
    char_deque = deque(s)
    
    while len(char_deque) > 1:
        # Виймаємо символи з обох кінців черги
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

if __name__ == "__main__":
    example_str = "A man a plan a canal Panama"
    result = is_palindrome(example_str)
    print(f"Рядок '{example_str}' {'є' if result else 'не є'} паліндромом.")