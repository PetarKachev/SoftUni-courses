def accommodate_new_pets(capacity: int, max_weight: float, *pets_info):
    allowed_pets = 0
    skipped_pets = 0
    remaining_capacity = capacity
    result = ''
    pets_dict = {}

    for pet_type, pet_weight in pets_info:
        if remaining_capacity > 0:
            if pet_weight > max_weight:
                skipped_pets += 1
                continue

            if pet_type not in pets_dict:
                pets_dict[pet_type] = 0
            pets_dict[pet_type] += 1
            remaining_capacity -= 1
            allowed_pets += 1
        else:
            break

    if remaining_capacity == 0 and len(pets_info) > (allowed_pets + skipped_pets):
        result += "You did not manage to accommodate all pets!\n"
    else:
        result += f"All pets are accommodated! Available capacity: {remaining_capacity}.\n"

    result += "Accommodated pets:\n"
    for pet, quantity in sorted(pets_dict.items(), key=lambda x: x[0]):
        result += f"{pet}: {quantity}\n"

    return result