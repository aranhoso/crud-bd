from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

class ClienteBase(BaseModel):
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None

class Cliente(ClienteBase):
    cliente_id: int

    class Config:
        orm_mode = True

class EnderecoBase(BaseModel):
    rua: Optional[str] = None
    numero: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None

class Endereco(EnderecoBase):
    endereco_id: int
    cliente_id: int

    class Config:
        orm_mode = True

class DepartamentoBase(BaseModel):
    nome: str

class Departamento(DepartamentoBase):
    departamento_id: int

    class Config:
        orm_mode = True

# Funcionarios
class FuncionarioBase(BaseModel):
    nome: str
    email: Optional[str] = None

class Funcionario(FuncionarioBase):
    funcionario_id: int
    departamento_id: int

    class Config:
        orm_mode = True

class CategoriaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class Categoria(CategoriaBase):
    categoria_id: int

    class Config:
        orm_mode = True

class FornecedorBase(BaseModel):
    nome: str
    contato: Optional[str] = None

class Fornecedor(FornecedorBase):
    fornecedor_id: int

    class Config:
        orm_mode = True

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: Decimal

class Produto(ProdutoBase):
    produto_id: int
    categoria_id: int
    fornecedor_id: int

    class Config:
        orm_mode = True

class PedidoBase(BaseModel):
    data: Optional[date] = None
    status: Optional[str] = None

class Pedido(PedidoBase):
    pedido_id: int
    cliente_id: int
    funcionario_id: int

    class Config:
        orm_mode = True

class ItensPedidoBase(BaseModel):
    quantidade: int
    preco_unitario: Decimal

class ItensPedido(ItensPedidoBase):
    itempedido_id: int
    pedido_id: int
    produto_id: int

    class Config:
        orm_mode = True

class EstoqueBase(BaseModel):
    quantidade_disponivel: int

class Estoque(EstoqueBase):
    estoque_id: int
    produto_id: int

    class Config:
        orm_mode = True