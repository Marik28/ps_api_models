from typing import Optional

import sqlalchemy.orm

import models
import tables


def get_platform_by_name(session: sqlalchemy.orm.Session, name: str) -> Optional[tables.Platform]:
    return session.query(tables.Platform).filter(tables.Platform.name == name).first()


def insert_platforms(session: sqlalchemy.orm.Session):
    platforms = [tables.Platform(name=platform.value) for platform in models.Platform]
    session.add_all(platforms)
    session.commit()
