import requests
from typing import Dict, Tuple, List
from enum import Enum


class ChildenType(str, Enum):
    DIRECT = "direct-children"
    ULTIMATE = "ultimate-children"


class GleifClient:
    BASE_URL = "https://api.gleif.org"
    API_V1_URL = BASE_URL + "/api/v1"

    def __init__(self) -> None:
        self.session = requests.Session()

    def make_api_request(self, url: str) -> Dict:
        response = self.session.get(url, headers={"Accept": "application/vnd.api+json"})
        return response.json()

    def get_data_from_response(self, response) -> Dict:
        if "data" in response:
            return response["data"]
        raise KeyError("'data' key not present in response.")

    def __has_pagination(self, response):
        return "next" in response["links"]

    def __get_next_link(self, response):
        return response["links"]["next"]

    def __is_last_page(self, response):
        return (
            response["meta"]["pagination"]["currentPage"]
            == response["meta"]["pagination"]["lastPage"]
        )

    def __parse_response(self, response):
        result = []
        for item in self.get_data_from_response(response):
            id_item = item["id"]
            legal_name = item["attributes"]["entity"]["legalName"]["name"]
            legal_country = item["attributes"]["entity"]["legalAddress"]["country"]
            result.append((id_item, legal_name, legal_country))
        return result

    def get_leis(self, parent: str, level: ChildenType) -> List[Tuple[str, str]]:
        url = self.API_V1_URL + "/lei-records/" + parent + "/" + level.value
        response = self.make_api_request(url)
        result = self.__parse_response(response=response)

        while self.__has_pagination(response):
            next_url = self.__get_next_link(response)
            response = self.make_api_request(next_url)
            next_result = self.__parse_response(response=response)
            result.extend(next_result)

            if self.__is_last_page(response=response):
                break
        return result

    def get_children(self, companies: List[str]) -> List[Tuple[str, str]]:
        list_tuples = []
        for company in companies:
            leis = self.get_leis(company, ChildenType.DIRECT) + self.get_leis(
                company, ChildenType.ULTIMATE
            )
            list_tuples.extend(leis)
        return list_tuples
