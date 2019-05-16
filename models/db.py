db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False)

db.define_table('recipes',
                Field('title',),
                Field('ingredients', 'text'),
                Field('method', 'text'),
                Field('size'),
                Field('time'),
                Field('file', 'upload'),
                #auth.signature              
                )
                
db.define_table('reviews',
                Field('recipe_id', 'reference recipes'),
                Field('author'),
	        Field('body', 'text'),
                #auth.signature
	        ) 
