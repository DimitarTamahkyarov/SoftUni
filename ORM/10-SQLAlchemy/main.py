from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import session_decorator 
from models import Recipe, User


engine = create_engine('postgresql+psycopg2://postgres:112344567@localhost/sql_alchemy_database')
Session = sessionmaker(bind=engine) 
session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)

    session.add(new_recipe)


# recipe1 = create_recipe('Spaghetti Carbonara', 'Pasta, Eggs, Pancetta, Cheese', 'Cook the pasta, mix it with eggs, pancetta, and cheese')
# recipe2 = create_recipe('Chicken Stir-Fry', 'Chicken, Bell Peppers, Soy Sauce, Vegetables', 'Stir-fry chicken and vegetables with soy sauce')

@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str,  new_ingredients: str, new_instructions: str) -> None:

    session.query(Recipe).filter_by(name=name).update({
        Recipe.name: new_name,
        Recipe.ingredients: new_ingredients,
        Recipe.instructions: new_instructions
    })


# update_recipe_by_name(
#     name="Spaghetti Carbonara",
#     new_name="Carbonara Pasta",
#     new_ingredients="Pasta, Eggs, Guanciale, Cheese",
#     new_instructions="Cook the pasta, mix with eggs, guanciale, and cheese"
# )


@session_decorator(session)
def delete_recipe_by_name(name: str):

    deleted_records = session.query(Recipe).filter_by(name=name).delete()

    return f'Deleted records: {deleted_records}'


print(delete_recipe_by_name("Carbonara Pasta"))
