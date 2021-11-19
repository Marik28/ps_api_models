import typer
from sqlalchemy.exc import IntegrityError

import models
import tables
from database import Session


def insert_platforms():
    platforms_to_create = [
        tables.Platform(name=value) for value in models.Platform
    ]
    with Session() as session:
        with typer.progressbar(platforms_to_create) as progress:
            for platform in progress:
                session.add(platform)

                try:
                    session.commit()
                except IntegrityError:
                    session.rollback()


if __name__ == '__main__':
    insert_platforms()
