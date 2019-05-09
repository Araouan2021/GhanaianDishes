db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False)

db.define_table('recipes',
                Field('title', unique=True),
                Field('ingredients', 'text'),
                Field('method', 'text'),
                Field('size'),
                Field('time'),
                Field('file', 'upload'),
                format = '%(title)s')
                
db.define_table('review',
                Field('recipes_id', 'reference recipes'),
                Field('author'),
                Field('email'),
                Field('body', 'text'))
                


