import datetime
import uuid
from typing import TYPE_CHECKING, Optional, List
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

if TYPE_CHECKING:
    from models.texto_ocr import TextoOcr
    from models.texto_correcao_manual import TextoCorrecaoManual
    from models.exemplar import Exemplar

class Pagina(SQLModel, table=True):
    id: Optional[int] = Field(default_factory=None, primary_key=True)

    pagina_index: int
    image_path: str
    exemplar_id: int = Field(default=None, foreign_key="exemplar.id")

    # exemplares: "Exemplar" = Relationship(back_populates="paginas")
    # textos_ocr: list["TextoOcr"] = Relationship(back_populates="paginas")
    # textos_correcao_manual: list["TextoCorrecaoManual"] = Relationship(back_populates="paginas")

    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)