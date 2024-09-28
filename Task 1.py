import queue
import random
import time

class ServiceCenter:
    def __init__(self):
        # Створення черги заявок
        self.request_queue = queue.Queue()
        self.request_id = 1

    def generate_request(self):
        # Генеруємо нову заявку з унікальним номером
        request = f"Request-{self.request_id}"
        self.request_id += 1
        print(f"Згенеровано нову заявку: {request}")
        # Додаємо заявку до черги
        self.request_queue.put(request)

    def process_request(self):
        if not self.request_queue.empty():
            # Видаляємо заявку з черги
            request = self.request_queue.get()
            print(f"Обробляється заявка: {request}")
            # Імітуємо час на обробку заявки
            time.sleep(1)
        else:
            print("Черга пуста, немає заявок для обробки.")

    def run(self, cycles=5):
        # Циклічне виконання
        for _ in range(cycles):
            self.generate_request()
            self.process_request()
            time.sleep(1)

if __name__ == "__main__":
    service_center = ServiceCenter()
    service_center.run(cycles=3)