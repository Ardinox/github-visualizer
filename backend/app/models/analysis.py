from enum import Enum
from sqlalchemy import DateTime, ForeignKey, Enum as SQLEnum, func
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from app.database.base import Base


class AnalysisProfile(str, Enum):
    OPEN_SOURCE = "open_source"
    PERSONAL = "personal"
    TEAM = "team"
    COMPLETED = "completed"


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    repository_id: Mapped[int] = mapped_column(
        ForeignKey("repositories.id"), nullable=False
    )

    profile: Mapped[AnalysisProfile] = mapped_column(
        SQLEnum(AnalysisProfile), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
