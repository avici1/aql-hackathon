import requests
from datetime import datetime as dt


class Challenge_10:
    """
    Module representing the challenge number 10.
    This challenge is about accessing multiple API.
    """

    def __init__(self):
        """
        Base constructor
        """
        self.GOV_URL = "http://environment.data.gov.uk/flood-monitoring"
        self.CORE_URL = "https://api.core.aql.com/v1/"
        self.TOKEN = "12391|5wbWXrwLCxx5EatPBpxkLFksCTodQ1CxD3YZX8qp8ad8c808"
        self.LOCATION_ID = "w80fP5N2B3"
        self.DECODER_ID = "ojAWt7NyR5K"
        self.TEAM = 10
        self.STATION_IDS = [
            "F1902",
            "L1515",
            "F1903",
            "L1907",
            "L2009",
            "L1931",
            "L2208",
            "F2206",
            "L2205",
            "L2402",
            "L2806",
            "L2803",
            "L2411",
            "L2403",
        ]

    def process_station(self, station_id):
        """
        Processing the station
        """
        url = f"{self.GOV_URL}/id/stations/{station_id}/measures"
        response = requests.get(url)


if __name__ == "__main__":
    ch_10 = Challenge_10()
    for station_id in ch_10.STATION_IDS:
        print(station_id)
