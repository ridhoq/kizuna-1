import config
from kizuna.models.ReactionImage import ReactionImage

import sqlalchemy as sa
import sqlalchemy.orm as orm

make_session = orm.sessionmaker(bind=sa.create_engine(config.DATABASE_URL, echo=True))

session = make_session()

images = session.query(ReactionImage).all()

for image in images:
    old = 'https://s3-us-west-2.amazonaws.com/kizuna.guap.io'
    new = 'https://img.kizuna.guap.io'
    image.url = image.url.replace(old, new)

session.commit()
