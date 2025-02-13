import requests
from requests.exceptions import RequestException


class LeapYear:
    """
    Class to manage API calls and check leap years.

    Args:
    link (str): The API endpoint link.
    """

    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def check_connection(self) -> int:
        """
        Checks the API connection.

        Returns:
        int: The status code of the API response.
        """
        try:
            response = requests.get(self.endpoint)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.status_code
        except RequestException as e:
            print(f"Error checking connection: {e}")
            return None

    def check_leap_year(self, year: str) -> bool:
        """
        Gets the API response data to check leap year.

        Returns:
        str: The content of the API response.
        """
        try:
            response = requests.get(f"{self.endpoint}/?year={year}")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            if response.status_code == 200 and response.json()["leapyear"] is True:
                return True
            elif response.status_code == 200 and response.json()["leapyear"] is False:
                return False
            else:
                return response.json()
        except RequestException as e:
            print(f"Error fetching data: {e}")
            return False


if __name__ == "__main__":
    leap_year = LeapYear("https://digidates.de/api/v1/leapyear")
    print(leap_year.check_connection())
    print(leap_year.check_leap_year(year="2024"))
