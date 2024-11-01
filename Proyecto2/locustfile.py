from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    faculties = ["Ingeniería", "Agronomía"]
    disciplines = [1, 2, 3]  # Natación, Atletismo, Boxeo

    @task
    def send_request(self):
        faculty = random.choice(self.faculties)
        discipline = random.choice(self.disciplines)
        path = "/ingenieria" if faculty == "Ingeniería" else "/agronomia"
        self.client.post(path, json={
            "faculty": faculty,
            "discipline": discipline
        })
