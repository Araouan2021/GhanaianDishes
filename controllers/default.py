def search():
    query = db.recipes.title.contains(request.vars.search)
    recipes = db(query).select(orderby=db.recipes.title)
    return dict(recipes=recipes)