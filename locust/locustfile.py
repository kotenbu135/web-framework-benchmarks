from locust import HttpUser, task


class SampleApi(HttpUser):

    @task(1)
    def root(self):
        self.client.get('/')