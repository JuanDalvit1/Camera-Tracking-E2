Camera Tracking

Este projeto segue a arquitetura MVC para garantir modularidade e escalabilidade. O backend é responsável por coletar e processar dados da câmera em tempo real, armazenar informações e permitir o treinamento de modelos. O frontend fornece uma interface para visualizar a câmera, realizar treinamentos e acessar os resultados das análises.]

## Estrutura de Diretórios

📂 /
│── 📂 backend/
│ │── 📂 models/
│ │── 📂 controllers/
│ │── 📂 services/
│ │── 📂 database/
│ │── main.py
│── 📂 frontend/
│ │── 📂 components/
│ │── 📂 pages/
│ │── 📂 assets/
│ │── app.py
│── 📂 config/
│── 📂 docs/
│── 📂 tests/
│── requirements.txt
│── README.md

## Funcionalidades

- **Visualização em Tempo Real**: Captura e processamento de imagem da câmera com insights visuais.
- **Treinamento de Modelos**: Coleta e classificação de dados para aprendizado de máquina.
- **Dashboard**: Exibição de estatísticas e resultados das análises.

## Tecnologias

- **Backend**: Python (FastAPI/Flask/Django) + OpenCV/TensorFlow/PyTorch
- **Banco de Dados**: PostgreSQL/SQLite/MongoDB
- **Frontend**: React/Vue.js/Streamlit
- **Infraestrutura**: Docker para containerização

A arquitetura permite adicionar ou remover funcionalidades sem comprometer o restante do sistema.

Checklist para Criar o Projeto do Zero
1️⃣ Configuração Inicial
✅ Criar um repositório Git e configurar o ambiente de desenvolvimento.
✅ Criar um ambiente virtual Python e definir o requirements.txt com bibliotecas essenciais.
✅ Configurar o banco de dados (PostgreSQL, SQLite ou MongoDB) e criar a estrutura básica.

2️⃣ Estruturação do Backend
✅ Criar a pasta backend/ e organizar subpastas (models/, controllers/, services/, database/).
✅ Implementar a conexão com o banco de dados e definir os modelos de dados.
✅ Criar um serviço para capturar imagens da câmera e processar os dados com OpenCV.
✅ Criar APIs para:

Fornecer o streaming da câmera em tempo real.
Receber e armazenar dados do treinamento.
Disponibilizar as análises para o frontend.
✅ Testar endpoints com Postman/Insomnia.
3️⃣ Desenvolvimento do Frontend
✅ Criar a pasta frontend/ e organizar subpastas (components/, pages/, assets/).
✅ Criar a interface de visualização em tempo real, exibindo a câmera com as análises.
✅ Criar a interface do módulo de treinamento, permitindo interações e coleta de dados.
✅ Criar a interface do dashboard, exibindo estatísticas e informações analisadas.
✅ Configurar a comunicação com o backend via API.

4️⃣ Integração e Testes
✅ Testar a comunicação entre frontend e backend.
✅ Validar a captura e processamento de imagens.
✅ Testar o armazenamento de dados do treinamento e recuperação no dashboard.

5️⃣ Otimização e Deploy
✅ Revisar a arquitetura para garantir escalabilidade e modularidade.
✅ Criar um Dockerfile para containerizar a aplicação.
✅ Configurar o deploy (Heroku, AWS, ou outra solução).
✅ Criar a documentação (README.md) explicando como rodar e contribuir com o projeto.

## Como Iniciar o Projeto

### Backend

1. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:

   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Inicie o servidor FastAPI:
   ```bash
   uvicorn backend.main:app --reload
   ```

### Frontend

1. Navegue até o diretório `frontend`:

   ```bash
   cd frontend
   ```

2. Inicie a aplicação Streamlit:
   ```bash
   streamlit run app.py
   ```

Agora você pode acessar a interface do frontend em `http://localhost:8501` e a API do backend em `http://localhost:8000`.
