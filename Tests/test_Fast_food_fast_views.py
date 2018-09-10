import unittest
import json
from app.views import app


class EndpointsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_home_route(self):
        response = self.client.get("/", content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_successful_registration(self):
        response = self.client.post("/api/v1/auth/register",
                                    data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                                         password="Password", confirm_password="Password")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_already_registered(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/register",
                                    data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 403)

    def test_successful_login(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/login",
                                    data=json.dumps(dict(email="hrigga22@gmail.com",
                                                         password="Password")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_failed_login(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/login",
                                    data=json.dumps(dict(email="hrigga24@gmail.com",
                                                         password="Passwort")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 401)

    def test_successful_logout(self):
        self.client.post("/api/v1/auth/register",
                         dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password"),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="hrigga22@gmail.com",
                                              password="Password")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/logout", content_type="application/json")

        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        self.client.post("/api/v1/auth/reset-password",
                         data=json.dumps(dict(email="hrigga23@gmail.com",
                                              new_password="Passwort", confirm_new_password="Passwort")),
                         content_type="application/json")
        response = self.client.post("/api/v1/auth/reset-password",
                                    data=json.dumps(dict(email="hriga23@gmail.com",
                                                         new_password="Passwort",
                                                         confirm_new_password="Passwort")),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_new_order(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="hrigga22@gmail.com",
                                              password="Password")),
                         content_type="application/json")
        data = {"orderer": "hrigga22@gmail.com", "what_order": "what_order"}
        response = self.client.post("/v1/api/orders",
                                    data=json.dumps(data),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_delete_order(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="hrigga22@gmail.com",
                                              password="Password")),
                         content_type="application/json")
        self.client.post("/v1/api/orders",
                         data=json.dumps(dict(orderer="hrigga22@gmail.com",
                                              what_order="what_order")),
                         content_type="application/json")
        response = self.client.delete("/v1/api/orders/1",
                                      data=json.dumps(dict(orderer="hrigga22@gmail.com")),
                                      content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_view_orders(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="hrigga22@gmail.com",
                                              password="Password")),
                         content_type="application/json")
        self.client.post("/v1/api/orders",
                         data=json.dumps(dict(orderer="hrigga22@gmail.com",
                                              what_order="what_order")),
                         content_type="application/json")
        self.client.post("/v1/api/orders",
                         data=json.dumps(dict(orderer="hrigga22@gmail.com",
                                              what_order="what_order")),
                         content_type="application/json")
        response = self.client.get("/v1/api/orders", content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_view_order_by_id(self):
        self.client.post("/api/v1/auth/register",
                         data=json.dumps(dict(first_name="H", last_name="Rigga", email="hrigga22@gmail.com",
                                              password="Password", confirm_password="Password")),
                         content_type="application/json")
        self.client.post("/api/v1/auth/login",
                         data=json.dumps(dict(email="hrigga22@gmail.com",
                                              password="Password")),
                         content_type="application/json")
        self.client.post("/v1/api/orders",
                         data=json.dumps(dict(orderer="hrigga22@gmail.com",
                                              what_order="what_order")),
                         content_type="application/json")
        response = self.client.get("/v1/api/orders/1",
                                   data=json.dumps(dict(orderId=1)), content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        del self.client
