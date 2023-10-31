import requests
key = 'the_key_that_i_used'

def get_value(input_data):
    url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=ik20POF2g0ah76aJc0xhzMaxNE5z6o1J"

    try:
        response = requests.get(url)
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        return "Error", e

current_asset = input()
current_rate = get_value(current_asset.upper())
print(current_rate)