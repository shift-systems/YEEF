# from server.tests.base_config import BaseTestCase
# from rest_framework import status
# from server.api.authentication.models import User
# from . import (new_user, data2, invalid_email, invalid_password,
#                short_password, dup_username, user_login)


# class AccountTests(BaseTestCase):
#     """handles user registration tests"""

#     def test_new_user_registration(self):
#         """check if new user can be registered"""
#         response = self.register_user(new_user)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn("token", response.data)

#     def test_user_login(self):
#         """new user can be logged in\
#         and token returned on successful login"""
#         self.verify_user(new_user)
#         response = self.login_user(user_login)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("token", response.data)

#     def test_wrong_token_header_prefix(self):
#         """invalid prefix header provided"""
#         self.client.credentials(HTTP_AUTHORIZATION='hgfds ' + 'iuytr')
#         response = self.client.get("/api/user/", format="json")
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_for_invalid_token(self):
#         """validates token"""
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'werty')
#         response = self.client.get("/api/user/", format="json")
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_no_token_in_header(self):
#         """no token in header"""
#         self.add_credentials(response='')
#         response = self.client.get("/api/user/", format="json")
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_create_super_user(self):
#         """checks for registration of a super user in the User model"""
#         user = User.objects.create_superuser(
#             username='gabriel',
#             password='sampletestcase')
#         self.assertIn(str(user), str(user.username))

#     def test_create_non_user(self):
#         """check for registration of a client user in the User model"""
#         user = User.objects.create_user(
#             email='gabriel@gmail.com',
#             username='gabriel',
#             password='sampletestcase')
#         self.assertIn(str(user), str(user.email))

#     def test_duplicate_username(self):
#         "user with same username provided exists"""
#         self.register_user(new_user)
#         response = self.register_user(dup_username)
#         self.assertIn(response.data["errors"]["username"][0],
#                       'user with this username already exists.')
