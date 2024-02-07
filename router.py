from db import add_item, show_items


def parse_to_add(message):
    name, description, price = message.text.split('/')
    name = name.strip()
    description = description.strip()
    price = float(price.strip())
    add_item(name, description, price)


def show_all():
    return show_items()
