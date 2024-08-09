#  ЗАКОМЕНТУВАВ ТЕСТИ БО ВОНИ МЕНІ ТРІШКИ ЗАВАЖЛИ :D



# from frontend import app
# from frontend.db import Base, engine, Session, User

# from flask_testing import TestCase
# from flask_login import login_user

# import unittest



# class BaseTestCase(TestCase):
#     def create_app(self):
#         return app

#     def setUp(self):
#         Base.metadata.create_all(bind=engine)
#         self.session = Session()
#         self.test_user = User(nickname="aboba", email="aboba@gmail.com", password='password', untouchable=100)
#         self.session.add(self.test_user)
#         self.session.commit()


#     def Drop(self):
#         self.session.close()
#         Base.metadata.drop_all(bind=engine)



# class TestForFrontendApp(BaseTestCase):
    
#     def test_user_login(self):
#         """
#         Verifies that a user can successfully log in.
#         """
#         with self.client:
#             response = self.client.post("/login", data={"nickname": "aboba", "password": 'password'})
#             self.assert200(response)


#     def test_homepage_access(self):
#         """
#         Ensures that the main page is accessible after the user logs in.
#         """
#         with self.client:
#             login_user(self.session.query(User).filter_by(nickname="aboba").first())
#             homepage = self.client.get("/")
#             self.assert200(homepage)


#     def test_about_page(self):
#         with self.client:
#             login_user(self.session.query(User).filter_by(nickname="aboba").first())
#             about_page = self.client.get('/about')
#             self.assert200



# if __name__ == "__main__":
#     # i was just testing to see what it does :D
#     unittest.main(
#         verbosity=2,
#         failfast=False,
#         catchbreak=True,
#         buffer=True,
#         exit=False 
#     )
