# Django + Streamlit Study Project

Este repositório apresenta um **projeto de estudo** que combina o poder do **Django**, um framework de desenvolvimento web robusto, com o **Streamlit**, um framework para criação de aplicativos interativos voltado para ciência de dados. O objetivo deste projeto é explorar como integrar essas ferramentas para construir soluções ágeis e interativas.

## 💡 **Sobre o Projeto**

Este projeto foi desenvolvido para demonstrar como o Django pode ser utilizado em conjunto com o Streamlit para:

- Construir interfaces web interativas para análise de dados.
- Integrar funcionalidades de backend robustas com visualizações interativas.
- Servir como ponto de partida para o aprendizado de **Streamlit** em um contexto de aplicações Django.

Trata-se de um projeto **acadêmico e experimental**, ideal para desenvolvedores que estão se aventurando na criação de dashboards dinâmicos com **Streamlit** e **Django**.

## 🚀 **Principais Funcionalidades**

- Integração de um backend Django com uma interface Streamlit.
- Visualizações interativas de dados com gráficos e tabelas.
- Rápida prototipação de ferramentas de análise de dados.

## 🛠️ **Tecnologias Utilizadas**

- [Python](https://www.python.org/) 3.9+
- [Django](https://www.djangoproject.com/) 4.x
- [Streamlit](https://streamlit.io/) 1.x
- Banco de dados SQLite (padrão para estudos)

## 🗂️ **Estrutura do Projeto**

```plaintext
streamlit-django-project/
│
├── app/                   # App principal do projeto Django
│   ├── models.py          # Modelos para manipulação de dados
│   ├── views.py           # Lógica de backend para o Django
│   ├── templates/         # Templates HTML (quando necessário)
│   └── static/            # Arquivos estáticos (CSS/JS)
│
├── streamlit/             # Aplicação Streamlit
│   ├── app.py             # Arquivo principal do Streamlit
│   └── utils/             # Funções auxiliares e de suporte
│
├── manage.py              # Comando principal do Django
├── db.sqlite3             # Banco de dados SQLite
└── settings.py            # Configurações do projeto Django
```

## ⚙️ **Configuração e Execução**

### **1. Configurar o ambiente virtual**

Clone o repositório e crie um ambiente virtual:

```bash
git clone https://github.com/carlosalbertoprojetos/streamlit.git
cd streamlit
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

### **2. Configurar o Django**

Realize as migrações do banco de dados e crie um superusuário:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### **3. Executar o Django e o Streamlit**

Inicie o servidor Django:

```bash
python manage.py runserver
```

Inicie o Streamlit em uma nova aba do terminal:

```bash
streamlit run streamlit/app.py
```

### **4. Acessar as Aplicações**

- Painel Django Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- Interface Streamlit: [http://localhost:8501](http://localhost:8501)

## 📚 **Propósito Educacional**

Este projeto é **exclusivamente para fins de aprendizado**. Ele demonstra a integração entre Django e Streamlit como forma de facilitar o desenvolvimento de aplicativos de ciência de dados interativos.

## 🌟 **Próximos Passos**

- Implementar visualizações mais complexas e interativas no Streamlit.
- Explorar a integração de APIs para alimentar a aplicação com dados externos.
- Criar testes automatizados para validação de funcionalidades.

## 📄 **Licença**

Este projeto está licenciado sob a [Licença MIT](LICENSE). Sinta-se à vontade para utilizá-lo, modificá-lo e melhorá-lo para seus próprios estudos e experimentos.

---

💻 Desenvolvido por [Carlos Alberto Medeiros](https://www.linkedin.com/in/carlos-alberto-medeiros-29aa6258/)  
🌟 Experimente o potencial de **Django + Streamlit** para projetos interativos de ciência de dados!
