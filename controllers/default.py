
def show():
    recipe = db.recipes(request.args(0, cast=int)) or redirect(URL('index'))
    return dict(recipe=recipe)

def postReview():
    recipe = db.recipes(request.args(0, cast=int)) or redirect(URL('index'))
    body = request.vars.body
    author = request.vars.author
    
    results = db.reviews.insert(
    recipe_id = request.args(0, cast=int),
    body = body,
    author = author,
            )
    redirect(URL('show', args = recipe.id))
    return dict(review=review)

    redirect(URL('show', args = review.recipe_id))
    return dict(review=review)


def download():
    return response.download(request, db)

def index():
    recipes = db().select(db.recipes.ALL, orderby=db.recipes.title)
    return dict(recipes=recipes)

# #@auth.requires_login()
# def delete():
#     parameters = request.args
#     submitted_id = parameters[0]

#     if db(db.recipes.id == submitted_id).select():
#         db(db.recipes.id == submitted_id).delete()
#         return 'Recipe Deleted Successfully'

#     else:
#         return 'No Recipe With the ID found'


def getRecipe():
    ingredients = request.vars.ingredient
    currentIndex = 0
    recipes = ""
    if type(ingredients) is list:
        for ingredient in ingredients:
            if currentIndex==0:
                query = db.recipes.ingredients.contains(ingredient)
                recipes = db(query).select()
                currentIndex = 9;
            else:
                if len(recipes)>0:
                    recipes = filter(lambda recipe: ingredient in recipe.ingredients, recipes)
                else:
                    break
        ingredientString = ", ".join(ingredients)
    else:
        query = db.recipes.ingredients.contains(ingredients)
        recipes = db(query).select()
        ingredientString = ingredients
    
            
    return dict(recipes=recipes, ingredients=ingredientString)

def postRecipe():
    form = SQLFORM(db.recipes).process(next=URL('index'))
    return dict(form=form)

def login():
    return dict()

def authenticate():
    email = request.vars.email
    password = request.vars.password

    if auth.login_bare(email,password):
        redirect(URL('index'))
    else:
        return "Login failed"

@auth.requires_login()
@auth.requires_membership('manager')
def manage():
    grid = SQLFORM.smartgrid(db.reviews)
    return dict(grid=grid)
    


    
        


        

