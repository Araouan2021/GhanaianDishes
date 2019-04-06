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

def search():
    query = db.recipes.title.contains(request.vars.search)
    recipes = db(query).select(orderby=db.recipes.title)
    return dict(recipes=recipes)

