from locust import HttpUser, task, between

class MyAppUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def send_json(self):
        self.client.post("/", json={
            "student": "Emilia",
            "age": "25",
            "facultad": "ingenieria",
            "disciplina": 1
        })
