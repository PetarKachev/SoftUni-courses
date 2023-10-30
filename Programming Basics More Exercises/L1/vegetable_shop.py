veggie_kg_price = float(input())
fruit_kg_price = float(input())
all_kg_veggie = int(input())
all_kg_fruit = int(input())

all_veggie_price = veggie_kg_price * all_kg_veggie
all_fruit_price = fruit_kg_price * all_kg_fruit

euro_price = (all_veggie_price + all_fruit_price) / 1.94

print(f"{euro_price:.2f}")