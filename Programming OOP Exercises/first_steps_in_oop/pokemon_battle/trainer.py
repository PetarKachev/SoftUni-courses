from ex8_pokemon_battle.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: [Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return "Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"
        return result