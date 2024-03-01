from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Time between requests

    @task
    def test_homepage(self):
        self.client.get("/")  # Simulate GET request to homepage

# Run the test with `locust -f locustfile.py`