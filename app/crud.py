from sqlalchemy.orm import Session
from . import models, schemas

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.cliente_id == cliente_id).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def get_endereco(db: Session, endereco_id: int):
    return db.query(models.Endereco).filter(models.Endereco.endereco_id == endereco_id).first()

def get_enderecos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Endereco).offset(skip).limit(limit).all()

def get_departamento(db: Session, departamento_id: int):
    return db.query(models.Departamento).filter(models.Departamento.departamento_id == departamento_id).first()

def get_departamentos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Departamento).offset(skip).limit(limit).all()

def get_funcionario(db: Session, funcionario_id: int):
    return db.query(models.Funcionario).filter(models.Funcionario.funcionario_id == funcionario_id).first()

def get_funcionarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Funcionario).offset(skip).limit(limit).all()

def get_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.categoria_id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categoria).offset(skip).limit(limit).all()

def get_fornecedor(db: Session, fornecedor_id: int):
    return db.query(models.Fornecedor).filter(models.Fornecedor.fornecedor_id == fornecedor_id).first()

def get_fornecedores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fornecedor).offset(skip).limit(limit).all()

def get_produto(db: Session, produto_id: int):
    return db.query(models.Produto).filter(models.Produto.produto_id == produto_id).first()

def get_produtos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Produto).offset(skip).limit(limit).all()

def get_pedido(db: Session, pedido_id: int):
    return db.query(models.Pedido).filter(models.Pedido.pedido_id == pedido_id).first()

def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pedido).offset(skip).limit(limit).all()

def get_itempedido(db: Session, itempedido_id: int):
    return db.query(models.ItensPedido).filter(models.ItensPedido.itempedido_id == itempedido_id).first()

def get_itenspedido(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ItensPedido).offset(skip).limit(limit).all()

def get_estoque_item(db: Session, estoque_id: int):
    return db.query(models.Estoque).filter(models.Estoque.estoque_id == estoque_id).first()

def get_estoque(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Estoque).offset(skip).limit(limit).all()