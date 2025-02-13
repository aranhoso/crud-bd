from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from .database import Base


class Cliente(Base):
    __tablename__ = "Clientes"
    cliente_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100))
    telefone = Column(String(20))
    
    enderecos = relationship("Endereco", back_populates="cliente")
    pedidos = relationship("Pedido", back_populates="cliente")

class Endereco(Base):
    __tablename__ = "Enderecos"
    endereco_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("Clientes.cliente_id"))
    rua = Column(String(150))
    numero = Column(String(20))
    bairro = Column(String(100))
    cidade = Column(String(100))
    estado = Column(String(50))
    
    cliente = relationship("Cliente", back_populates="enderecos")

class Departamento(Base):
    __tablename__ = "Departamentos"
    departamento_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    
    funcionarios = relationship("Funcionario", back_populates="departamento")

class Funcionario(Base):
    __tablename__ = "Funcionarios"
    funcionario_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100))
    departamento_id = Column(Integer, ForeignKey("Departamentos.departamento_id"))
    
    departamento = relationship("Departamento", back_populates="funcionarios")
    pedidos = relationship("Pedido", back_populates="funcionario")

class Categoria(Base):
    __tablename__ = "Categorias"
    categoria_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    descricao = Column(String(255))
    
    produtos = relationship("Produto", back_populates="categoria")

class Fornecedor(Base):
    __tablename__ = "Fornecedores"
    fornecedor_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    contato = Column(String(100))
    
    produtos = relationship("Produto", back_populates="fornecedor")

class Produto(Base):
    __tablename__ = "Produtos"
    produto_id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    descricao = Column(String(255))
    categoria_id = Column(Integer, ForeignKey("Categorias.categoria_id"))
    fornecedor_id = Column(Integer, ForeignKey("Fornecedores.fornecedor_id"))
    preco = Column(DECIMAL(10,2))
    
    categoria = relationship("Categoria", back_populates="produtos")
    fornecedor = relationship("Fornecedor", back_populates="produtos")
    itens_pedido = relationship("ItensPedido", back_populates="produto")
    estoque = relationship("Estoque", back_populates="produto", uselist=False)

class Pedido(Base):
    __tablename__ = "Pedidos"
    pedido_id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("Clientes.cliente_id"))
    funcionario_id = Column(Integer, ForeignKey("Funcionarios.funcionario_id"))
    data = Column(Date)
    status = Column(String(50))
    
    cliente = relationship("Cliente", back_populates="pedidos")
    funcionario = relationship("Funcionario", back_populates="pedidos")
    itens = relationship("ItensPedido", back_populates="pedido")

class ItensPedido(Base):
    __tablename__ = "ItensPedido"
    itempedido_id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("Pedidos.pedido_id"))
    produto_id = Column(Integer, ForeignKey("Produtos.produto_id"))
    quantidade = Column(Integer)
    preco_unitario = Column(DECIMAL(10,2))
    
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto", back_populates="itens_pedido")

class Estoque(Base):
    __tablename__ = "Estoque"
    estoque_id = Column(Integer, primary_key=True, index=True)
    produto_id = Column(Integer, ForeignKey("Produtos.produto_id"), unique=True)
    quantidade_disponivel = Column(Integer)
    
    produto = relationship("Produto", back_populates="estoque")