import datetime as dt
import uuid
from uuid import UUID
from enum import Enum, auto

from sqlalchemy import bindparam
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from sqlalchemy import text
from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import Mapped as M
from sqlalchemy.orm import mapped_column as column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import false
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.associationproxy import AssociationProxy

from app.db.base import Base

sql_utcnow = text('(now() at time zone \'utc\')')


class BaseMixin:
    @declared_attr.directive
    def __tablename__(cls):
        letters = ['_' + i.lower() if i.isupper() else i for i in cls.__name__]
        return ''.join(letters).lstrip('_') + 's'

    id: M[UUID] = column(server_default=text("gen_random_uuid()"), primary_key=True, index=True)
    created_at: M[dt.datetime] = column(server_default=sql_utcnow)
    updated_at: M[dt.datetime | None] = column(nullable=True, onupdate=sql_utcnow)


class API(BaseMixin, Base):
    documentation_url: M[str]
    adminpanel_url: M[str]
    description: M[str]
    price_per_month: M[int]


class ApplicationAPI(BaseMixin, Base):
    api_id: M[UUID] = column(ForeignKey("apis.id", ondelete="CASCADE"))
    application_id: M[UUID] = column(ForeignKey("applications", ondelete="CASCADE"))
    api_token: M[str | None]


class Application(BaseMixin, Base):
    number: M[str]

