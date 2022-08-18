import asyncio
from random import randint
from time import perf_counter

import requests

MAX_POKEMON = 898
COUNT = 20


def http_get(url: str):
    return requests.get(url).json()


async def http_get_async(url: str):
    return await asyncio.to_thread(http_get, url)


def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = http_get(pokemon_url)
    return str(pokemon.get("name"))


async def get_random_pokemon_name_async() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get_async(pokemon_url)
    return str(pokemon.get("name"))


def main():
    # synchronous call
    time_before = perf_counter()
    result = [get_random_pokemon_name() for _ in range(1, COUNT)]
    print(result)
    print(f"Total time (synchronous): {perf_counter() - time_before}")


async def main_async():
    # asynchronous call
    time_before = perf_counter()
    result_async = await asyncio.gather(*[get_random_pokemon_name_async() for _ in range(1, COUNT)])
    print(result_async)
    print(f"Total time (asynchronous): {perf_counter() - time_before}")


main()
asyncio.run(main_async())
