# Inclusão 360

Plataforma para projeto de inclusão digital. Para mais informações, visite nossa [página do projeto](https://sites.google.com/cesar.school/inclusao-360/).

## Estrutura do Projeto

Este é um monorepo contendo dois projetos principais:

```
.
.
├── frontend/          # Aplicação frontend em React
│   └── docker/       # Configuração Docker do frontend
└── backend/          # Aplicação backend em Python Flask
    └── docker/       # Configuração Docker do backend
```

## Configuração Docker

Cada projeto possui sua própria configuração Docker independente.

### Frontend Docker

Para executar apenas o frontend:
```bash
cd frontend
docker build -t inclusao360-frontend .
docker run -p 3000:3000 inclusao360-frontend
```

### Backend Docker

Para executar apenas o backend:
```bash
cd backend
docker build -t inclusao360-backend .
docker run -p 5000:5000 inclusao360-backend
```

### Executando Ambos os Projetos

Você pode executar ambos os projetos simultaneamente em terminais separados seguindo as instruções acima para cada um.

Para desenvolvimento local sem Docker, siga as instruções na seção "Desenvolvimento".

## Tecnologias

### Frontend
- React
- TypeScript
- Node.js

### Backend
- Python 3.12
- Flask

## Pré-requisitos

- Docker
- Docker Compose
- Node.js (para desenvolvimento frontend local)
- Python 3.x (para desenvolvimento backend local)

## Começando

1. Clone o repositório:
```bash
git clone https://github.com/yourusername/plataforma-360.git
cd plataforma-360
```

2. Execute com Docker:
```bash
docker-compose up
```

A aplicação estará disponível em:
- Frontend: http://localhost:3000
- Backend: http://localhost:5000

## Desenvolvimento

### Desenvolvimento Frontend
```bash
cd frontend
npm install
npm start
```

### Desenvolvimento Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```

## Configuração Docker

O projeto utiliza Docker para containerização. Cada componente (frontend e backend) possui seu próprio Dockerfile, e são orquestrados usando docker-compose.

Para construir e executar os containers:
```bash
docker-compose up --build
```

## Como Contribuir

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/RecursoIncrivel`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona um Recurso Incrível'`)
4. Faça push para a branch (`git push origin feature/RecursoIncrivel`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença GNU GPL v2 - veja o arquivo [LICENSE](LICENSE) para detalhes.
