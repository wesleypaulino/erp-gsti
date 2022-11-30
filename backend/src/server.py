from typing import List
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import criar_db, get_db
from src.schemas.schemas import Tecnicos
from src.schemas.schemas import Patrimonio
from src.schemas.schemas import Licenca

from src.infra.sqlalchemy.repositorios.tecnicos import RepositoryTecnicos
from src.infra.sqlalchemy.repositorios.patrimonio import RepositoryPatrimonio
from src.infra.sqlalchemy.repositorios.licenca import RepositoryLicenca

# criar_db()

app = FastAPI()

##Cors
origins = origins = [
    "http://localhost:4200",
    "http://localhost:8000",
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],) 

@app.get('/')
def listar():
    return {'menssage': 'Hello World!'}

###TECNICOS
@app.post('/tecnicos',
          status_code=status.HTTP_201_CREATED,
          response_model=Tecnicos)
def criar_tecnico(tecnico: Tecnicos, session: Session = Depends(get_db)):
    tecnico_criado = RepositoryTecnicos(session).criar(tecnico)
    return tecnico_criado

@app.get('/tecnicos', status_code=status.HTTP_200_OK, response_model=List[Tecnicos])
def tecnicos(db: Session = Depends(get_db)):
    try:
        tecnicos = RepositoryTecnicos(db).listar()
        return tecnicos
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não há dados para exibir')

@app.get('/tecnicos/{tecnico_id}')
def obter_tecnico(tecnico_id: int, session: Session = Depends(get_db)):
    tecnico_id = RepositoryTecnicos(session).obter(tecnico_id)
    return tecnico_id

@app.delete('/tecnicos/{tecnico_id}')
def remover_tecnico(tecnico_id: int, session: Session = Depends(get_db)):
    RepositoryTecnicos(session).remover(tecnico_id)
    return {'mensagem':'Tecnico removido com sucesso'} 

###PATRIMONIOS
@app.post('/patrimonios')
def criar_patrimonio(patrimonio: Patrimonio, session: Session = Depends(get_db)):
    patrimonio_criado = RepositoryPatrimonio(session).criar(patrimonio)
    return patrimonio_criado

@app.get('/patrimonios')
def patrimonios(db: Session = Depends(get_db)):
    try:
        patrimonios = RepositoryPatrimonio(db).listar()
        return patrimonios
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não há dados para exibir')

@app.get('/patrimonios/{patrimonio_id}')
def obter_patrimonio(patrimonio_id: int, session: Session = Depends(get_db)):
    patrimonio_id  = RepositoryPatrimonio(session).obter(patrimonio_id)
    return patrimonio_id

@app.delete('/patrimonios/{patrimonio_id}')
def remover_patrimonio(patrimonio_id: int, session: Session = Depends(get_db)):
    RepositoryPatrimonio(session).remover(patrimonio_id)
    return {'mensagem': 'Patromino removido com sucesso'}

###LICENCAS
@app.post('/licencas')
def criar_licencas(licenca: Licenca, session: Session = Depends(get_db)):
    licenca_criado = RepositoryLicenca(session).criar(licenca)
    return licenca_criado

@app.get('/licencas')
def licencas(db: Session = Depends(get_db)):
    try:
        licencas = RepositoryLicenca(db).listar()
        return licencas
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não há dados para exibir')

@app.get('/licencas/{licenca_id}')
def obter_licenca(licenca_id: int, session: Session = Depends(get_db)):
    licenca_id = RepositoryLicenca(session).obter(licenca_id)
    return licenca_id

@app.delete('/licencas/{licenca_id}')
def remover_licenca(licenca_id: int, session: Session = Depends(get_db)):
    RepositoryLicenca(session).remover(licenca_id)
    return {'mensagem':'Removido com sucesso'}


