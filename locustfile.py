from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task
    def get_closest(self):
        self.client.get("/closest?longitude=-86&latitude=-82&limit=10")

    @task
    def get_nearby(self):
        self.client.get("/nearby?longitude=-86&latitude=-82&limit=100&radius=10000")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
