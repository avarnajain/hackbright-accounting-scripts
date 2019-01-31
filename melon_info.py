"""Print out all the melons in our inventory."""


from melons import melon_attributes_dict


def print_melon(melon_name):
    """Print each melon with corresponding attribute information."""

    for melon in melon_attributes_dict:
        if melon == melon_name:
            print(melon)
            for attribute, value in melon_attributes_dict[melon].items():
                print(attribute, ':', value)

print_melon('Cantaloupe')
