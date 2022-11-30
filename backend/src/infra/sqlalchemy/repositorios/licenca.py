from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositoryLicenca():
    def __init__(self, session: Session):
        self.session = session

    def criar(self, licenca: schemas.Licenca):
        session_licenca = models.Licenca(
            produto=licenca.produto,
            chave=licenca.chave,
            nota=licenca.nota,
            solcompra=licenca.solcompra,
            pedcompra=licenca.pedcompra
        )

        self.session.add(session_licenca)
        self.session.commit()
        self.session.refresh(session_licenca)
        return session_licenca

    def listar(self):
        licenca = self.session.query(models.Licenca).all()
        return licenca

    def obter(self, licenca_id: int):
        stmt = select(models.Licenca).filter_by(id = licenca_id)
        licenca = self.session.execute(stmt).one()
        return licenca

    def remover(self, licenca_id: int):
        stmt = delete(models.Licenca).where(models.Licenca.id == licenca_id)

        self.session.execute(stmt)
        self.session.commit()
