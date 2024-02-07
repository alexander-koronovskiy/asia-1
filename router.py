from db import add_item


def parse_to_add(message):
    name, description, price = message.text.split('/')
    name = name.strip()
    description = description.strip()
    price = float(price.strip())
    add_item(name, description, price)
