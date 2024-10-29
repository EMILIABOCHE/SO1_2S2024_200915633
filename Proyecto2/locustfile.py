from locust import HttpUser, task, between
import random

class FacultyUser(HttpUser):
    wait_time = between(1, 5)  # Tiempo de espera entre peticiones

    @task
    def send_traffic(self):
        faculty_type = random.choice(["Ingeniería", "Agronomía"])
        discipline = random.choice([1, 2, 3])  # 1=Natación, 2=Atletismo, 3=Boxeo
        
        payload = {
            "faculty": faculty_type,
            "discipline": discipline
        }

        self.client.post("/ingress-path", json=payload)
