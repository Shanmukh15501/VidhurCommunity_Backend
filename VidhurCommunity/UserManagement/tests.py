from django.test import TestCase

class UsersManagersTests(TestCase):
    # Create your tests here.
    pass  # You can add tests specific to UsersManagers here if needed.

class NumbersTest(TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(2, 6,2):
            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",i);
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
