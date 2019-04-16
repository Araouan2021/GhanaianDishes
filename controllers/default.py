
def show():
    recipes = db.recipes(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(recipes=recipes)

def download():
    return response.download(request, db)

def index():
    recipes = db().select(db.recipes.ALL, orderby=db.recipes.title)
    return dict(recipes=recipes)

@auth.requires_login()
def delete():
    parameters = request.args
    submitted_id = parameters[0]

    if db(db.recipes.id == submitted_id).select():
        db(db.recipes.id == submitted_id).delete()
        return 'Recipe Deleted Successfully'

    else:
        return 'No Recipe With the ID found'


def getRecipe():
    ingredients = request.vars.ingredient
    currentIndex = 0
    recipes = ""

    for ingredient in ingredients:
        if currentIndex==0:
            print(currentIndex)
            query = db.recipes.ingredients.contains(ingredient)
            recipes = db(query).select()
            currentIndex = 9;
        else:
            if len(recipes)>0:
                recipes = filter(lambda recipe: ingredient in recipe.ingredients, recipes)
            else:
                break

    if type(ingredients) is list:
        ingredientString = ", ".join(ingredients)
    else:
        ingredientString = ingredients
    
            
    return dict(recipes=recipes, ingredients=ingredientString)
        


        

