from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import logging
import sys
from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, crud
from .database import engine, get_db

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Simple API",
    description="A simple API that returns 200 OK and provides GET endpoints for data visualization",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Verificação do Railway (Serviço de Deploy que estou usando para hospedar o backend)
@app.get("/health", summary="Healthcheck endpoint")
async def health_check():
    return {"status": "healthy"}

@app.get("/", status_code=status.HTTP_200_OK, summary="Root endpoint")
def root():
    logger.info("Root endpoint called")
    return {"status": "success", "message": "API is running"}

@app.get("/clientes", response_model=List[schemas.Cliente], summary="Obter todos os clientes")
def read_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clientes = crud.get_clientes(db, skip=skip, limit=limit)
    return clientes

@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente, summary="Obter um cliente específico")
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, cliente_id=cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.get("/enderecos", response_model=List[schemas.Endereco], summary="Obter todos os endereços")
def read_enderecos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enderecos = crud.get_enderecos(db, skip=skip, limit=limit)
    return enderecos

@app.get("/enderecos/{endereco_id}", response_model=schemas.Endereco, summary="Obter um endereço específico")
def read_endereco(endereco_id: int, db: Session = Depends(get_db)):
    endereco = crud.get_endereco(db, endereco_id=endereco_id)
    if not endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return endereco

@app.get("/departamentos", response_model=List[schemas.Departamento], summary="Obter todos os departamentos")
def read_departamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departamentos = crud.get_departamentos(db, skip=skip, limit=limit)
    return departamentos

@app.get("/departamentos/{departamento_id}", response_model=schemas.Departamento, summary="Obter um departamento específico")
def read_departamento(departamento_id: int, db: Session = Depends(get_db)):
    departamento = crud.get_departamento(db, departamento_id=departamento_id)
    if not departamento:
        raise HTTPException(status_code=404, detail="Departamento não encontrado")
    return departamento

@app.get("/funcionarios", response_model=List[schemas.Funcionario], summary="Obter todos os funcionarios")
def read_funcionarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    funcionarios = crud.get_funcionarios(db, skip=skip, limit=limit)
    return funcionarios

@app.get("/funcionarios/{funcionario_id}", response_model=schemas.Funcionario, summary="Obter um funcionario específico")
def read_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    funcionario = crud.get_funcionario(db, funcionario_id=funcionario_id)
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionario não encontrado")
    return funcionario

@app.get("/categorias", response_model=List[schemas.Categoria], summary="Obter todas as categorias")
def read_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db, skip=skip, limit=limit)
    return categorias

@app.get("/categorias/{categoria_id}", response_model=schemas.Categoria, summary="Obter uma categoria específica")
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = crud.get_categoria(db, categoria_id=categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@app.get("/fornecedores", response_model=List[schemas.Fornecedor], summary="Obter todos os fornecedores")
def read_fornecedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    fornecedores = crud.get_fornecedores(db, skip=skip, limit=limit)
    return fornecedores

@app.get("/fornecedores/{fornecedor_id}", response_model=schemas.Fornecedor, summary="Obter um fornecedor específico")
def read_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor = crud.get_fornecedor(db, fornecedor_id=fornecedor_id)
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@app.get("/produtos", response_model=List[schemas.Produto], summary="Obter todos os produtos")
def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produtos = crud.get_produtos(db, skip=skip, limit=limit)
    return produtos

@app.get("/produtos/{produto_id}", response_model=schemas.Produto, summary="Obter um produto específico")
def read_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = crud.get_produto(db, produto_id=produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@app.get("/pedidos", response_model=List[schemas.Pedido], summary="Obter todos os pedidos")
def read_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pedidos = crud.get_pedidos(db, skip=skip, limit=limit)
    return pedidos

@app.get("/pedidos/{pedido_id}", response_model=schemas.Pedido, summary="Obter um pedido específico")
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = crud.get_pedido(db, pedido_id=pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@app.get("/itenspedido", response_model=List[schemas.ItensPedido], summary="Obter todos os itens de pedido")
def read_itenspedido(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    itenspedido = crud.get_itenspedido(db, skip=skip, limit=limit)
    return itenspedido

@app.get("/itenspedido/{itempedido_id}", response_model=schemas.ItensPedido, summary="Obter um item de pedido específico")
def read_itempedido(itempedido_id: int, db: Session = Depends(get_db)):
    itempedido = crud.get_itempedido(db, itempedido_id=itempedido_id)
    if not itempedido:
        raise HTTPException(status_code=404, detail="Item de pedido não encontrado")
    return itempedido

@app.get("/estoque", response_model=List[schemas.Estoque], summary="Obter todos os registros de estoque")
def read_estoque(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estoque = crud.get_estoque(db, skip=skip, limit=limit)
    return estoque

@app.get("/estoque/{estoque_id}", response_model=schemas.Estoque, summary="Obter um registro de estoque específico")
def read_estoque_item(estoque_id: int, db: Session = Depends(get_db)):
    estoque_item = crud.get_estoque_item(db, estoque_id=estoque_id)
    if not estoque_item:
        raise HTTPException(status_code=404, detail="Registro de estoque não encontrado")
    return estoque_item