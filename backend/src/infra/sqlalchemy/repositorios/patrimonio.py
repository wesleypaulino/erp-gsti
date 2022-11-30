from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryPatrimonio():
   
    def __init__(self, session: Session):
        self.session = session

    def criar(self, patrimonio: schemas.Patrimonio):
        session_patrimonio = models.Patrimonio(
           patrimonio = patrimonio.patrimonio,
           depto = patrimonio.depto,
           serivcetag = patrimonio.serivcetag, 
           garantia = patrimonio.garantia,
           status = patrimonio.status 
        )

        self.session.add(session_patrimonio)
        self.session.commit()
        self.session.refresh(session_patrimonio)
        return session_patrimonio
        
    def listar(self): 
        patrimonios = self.session.query(models.Patrimonio).all()
        return patrimonios

    def obter(self, patrimonio_id: int):
        stmt = select(models.Patrimonio).filter_by(id = patrimonio_id)
        patrimonio = self.session.execute(stmt).one()
        return patrimonio

    def remover(self, patrimonio_id: int):
        stmt = delete(models.Patrimonio).where(models.Patrimonio.id == patrimonio_id)
        self.session.execute(stmt)
        self.session.commit()
        
        