from locust import HttpUser, task, between

class IntegralLoadTest(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_integral_endpoint(self):
        self.client.get("/integral/0/3.14159")
