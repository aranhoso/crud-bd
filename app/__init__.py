from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, schemas

__version__ = "1.0.0"
__author__ = "Guilherme Fernandes Medeiros"
__created__ = "2025-02-13"


def create_app() -> FastAPI:
    app = FastAPI(
        title="Trabalho Final - Banco de Dados",
        description="Implementação simples de um CRUD para o trabalho final da UC de Banco de Dados",
        version=__version__,
        contact={
            "name": __author__,
            "email": "medeiros.guilherme@unifesp.br"
        }
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = create_app()