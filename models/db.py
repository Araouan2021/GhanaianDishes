db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False)

db.define_table('recipes',
                Field('title'),
                Field('ingredients'),
                Field('time'),
                Field('size'),
                Field('file', 'upload'),
                auth.signature
                )
auth.settings.login_url = URL('login')