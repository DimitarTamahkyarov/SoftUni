def shopping_cart(*args):
    meals = {"Soup": [], "Pizza": [], "Dessert": []}
    meal_limits = {"Soup":  3, "Pizza": 4, "Dessert": 2}
    added_products = False

    for arg in args:
        if arg == "Stop":
            break

        meal = arg[0]
        product = arg[1]

        if product not in meals[meal] and len(meals[meal]) < meal_limits[meal]:
            meals[meal].append(product)
            added_products = True

    if not added_products:
        return "No products in the cart!"

    meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ""

    for meal in meals:
        sorted_products = sorted(meal[1])
        result += f"{meal[0]}:\n"

        for product in sorted_products:
            result += f" - {product}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
