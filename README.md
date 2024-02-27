# unimai_workshop

This repository contains the exercises of UnimAI workshop "Data Analytics in Central Banking Industry".

## Description

In the field of data analytics, it is crucial to be able to retrieve, organise and analyse data, as well as carefully manage metadata. The provided explanations and exercises offer an overview of some daily tasks in the production and analysis of dataset.
[GLEIF API](https://documenter.getpostman.com/view/7679680/SVYrrxuU?version=latest#40ef2ec4-b8bd-46de-8ad5-5359ed828242) was used to retrieve real entities data.
<u>NOTE</u>: The datasets present in the repo contain artificial data: data entries were randomly generated, and casually assigned to elements extracted via GLEIF API.

## Installation


## Usage

```python
from gleif_api_companies import GleifClient

gleif_client = GleifClient()

# returns the direct and ultimate children of the provided parent company
gleif_client.get_children(parent_company)

```


## License

[BSB 3-Clause](https://choosealicense.com/licenses/bsd-3-clause/#:~:text=A%20permissive%20license%20similar%20to,derived%20products%20without%20written%20consent.)