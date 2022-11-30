from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryTecnicos():
   
    def __init__(self, session: Session):
        self.session = session

    def criar(self, tecnico: schemas.Tecnicos):
        session_tecnico = models.Tecnicos(
           nome = tecnico.nome,
           email = tecnico.email 
        )

        self.session.add(session_tecnico)
        self.session.commit()
        self.session.refresh(session_tecnico)
        return session_tecnico
        
    def listar(self): 
        tecnicos = self.session.query(models.Tecnicos).all()
        return tecnicos

    def obter(self, tecnico_id: int):
        stmt = select(models.Tecnicos).filter_by(id = tecnico_id)
        tecnico_id = self.session.execute(stmt).one()
        return tecnico_id

    def remover(self, tecnico_id: int):
        stmt = delete(models.Tecnicos).where(models.Tecnicos.id == tecnico_id)
        self.session.execute(stmt)
        self.session.commit()
        