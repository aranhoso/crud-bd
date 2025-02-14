from typing import Optional
from pydantic import BaseModel
from datetime import date

class DepartamentoBase(BaseModel):
    nome: str

class DepartamentoCreate(DepartamentoBase):
    pass

class Departamento(DepartamentoBase):
    departamento_id: int

    class Config:
        orm_mode: True

class FuncionarioBase(BaseModel):
    nome: str
    email: Optional[str] = None
    departamento_id: int

class FuncionarioCreate(FuncionarioBase):
    pass

class Funcionario(FuncionarioBase):
    funcionario_id: int
    departamento: Departamento

    class Config:
        orm_mode: True

class ClienteBase(BaseModel):
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    cliente_id: int

    class Config:
        orm_mode: True

class EnderecoBase(BaseModel):
    rua: str
    numero: str
    bairro: str
    cidade: str
    estado: str
    cliente_id: int

class EnderecoCreate(EnderecoBase):
    pass

class Endereco(EnderecoBase):
    endereco_id: int

    class Config:
        orm_mode: True

class CategoriaBase(BaseModel):
    nome: str
    descricao: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    categoria_id: int

    class Config:
        orm_mode: True

class FornecedorBase(BaseModel):
    nome: str
    contato: Optional[str] = None

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    fornecedor_id: int

    class Config:
        orm_mode: True

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    categoria_id: int
    fornecedor_id: int
    preco: float

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    produto_id: int
    categoria: Categoria
    fornecedor: Fornecedor

    class Config:
        orm_mode: True

class PedidoBase(BaseModel):
    cliente_id: int
    funcionario_id: int
    data: Optional[date] = None
    status: Optional[str] = None

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    pedido_id: int
    cliente: Cliente
    funcionario: Funcionario

    class Config:
        orm_mode: True

class ItensPedidoBase(BaseModel):
    pedido_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

class ItensPedidoCreate(ItensPedidoBase):
    pass

class ItensPedido(ItensPedidoBase):
    itempedido_id: int
    produto: Produto

    class Config:
        orm_mode: True

class EstoqueBase(BaseModel):
    produto_id: int
    quantidade_disponivel: int

class EstoqueCreate(EstoqueBase):
    pass

class Estoque(EstoqueBase):
    estoque_id: int
    produto: Produto

    class Config:
        orm_mode: True