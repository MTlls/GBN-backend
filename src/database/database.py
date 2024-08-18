import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from src.models.jornal import Jornal
from src.models.exemplar import Exemplar
from src.models.pagina import Pagina
from src.models.texto_ocr import TextoOcr
from src.models.texto_correcao_manual import TextoCorrecaoManual

load_dotenv()

sqlite_url = os.getenv("DB_STRING")

engine = create_engine(sqlite_url, echo=True)

def get_engine():
    return engine

def create_db_and_tables() -> None:
    Jornal.metadata.create_all(engine)
    Exemplar.metadata.create_all(engine)
    Pagina.metadata.create_all(engine)
    TextoOcr.metadata.create_all(engine)
    TextoCorrecaoManual.metadata.create_all(engine)
    # SQLModel.metadata.create_trable(engine)