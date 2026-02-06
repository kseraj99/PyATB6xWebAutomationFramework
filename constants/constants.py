"""
it is a file that contain your all urls.
whenever you make the function as static means you can use directly.
if you will not make static method then you have to create an object then we can use
that function.
"""

class Constants:

    def __init__(self):
        print("constants loaded")


    @staticmethod
    def app_url():
        return "https://app.vwo.com"

    @staticmethod
    def app_dashboard_url(self):
        return "https://app.vwo.com/#/dashboard"