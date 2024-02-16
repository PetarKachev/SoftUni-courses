def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs[key] = [char for char in kwargs[key] if char % 2 == 0]
        else:
            kwargs[key] = [char for char in kwargs[key] if char % 2 != 0]
    sorted_dict = dict(sorted(kwargs.items(), key=lambda kvp: kvp[1], reverse=True))
    return sorted_dict