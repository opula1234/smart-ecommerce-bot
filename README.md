# 🤖 Smart E-Commerce Sales Bot

An AI-powered sales assistant built with **FastAPI**, **Google Gemini 2.5 Flash**, and **SQLModel**.

The chatbot helps customers discover products from an electronics inventory using natural language queries. It supports intelligent product recommendations, budget-based filtering, brand-specific searches, and multi-turn conversation memory.

---

## 🚀 Features

### AI-Powered Product Recommendations

* Uses Google Gemini 2.5 Flash
* Context-aware responses
* Natural language understanding
* Conversational product discovery

### Product Search

Customers can ask questions like:

```text
Suggest a laptop under 50k
```

```text
I need an Apple laptop
```

```text
Show me Samsung mobiles under 40k
```

```text
Recommend a smartwatch
```

The bot automatically extracts:

* Product category
* Budget
* Brand

and recommends matching products.

---

### Conversation Memory

The chatbot remembers previous messages within the same session.

Example:

```text
User:
Suggest a laptop under 50k

Bot:
Lenovo IdeaPad Slim 3 ...

User:
What about Dell?
```

The bot understands the context of the ongoing conversation.

---

### Inventory-Based Responses

The AI is restricted to the products available in the database.

Benefits:

* No hallucinated products
* Accurate pricing
* Inventory-aware recommendations

---

### Lifespan-Based Startup Management

The application uses FastAPI's modern lifespan API.

Startup tasks:

* Database initialization
* Product seeding
* Gemini client initialization
* Conversation memory initialization

Shutdown tasks:

* Resource cleanup

---

## 🏗️ Tech Stack

### Backend

* FastAPI
* Python 3.12+

### Database

* SQLite
* SQLModel

### AI Model

* Google Gemini 2.5 Flash
* LangChain Google GenAI

### API Server

* Uvicorn

### Configuration

* Python Dotenv

---

## 📁 Project Structure

```text
smart_ecommerce_bot/

├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── dependencies.py
│   ├── seed_data.py
│   │
│   └── routers/
│       └── sales_bot.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/opula1234/smart-ecommerce-bot.git

cd smart-ecommerce-bot
```

---

### Create Virtual Environment

Using uv:

```bash
uv venv
```

Activate:

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

### Install Dependencies

Using uv:

```bash
uv sync
```

or

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your API key from Google AI Studio.

---

## ▶️ Run Application

From the project root:

```bash
uv run uvicorn app.main:app --reload
```

or

```bash
python -m uvicorn app.main:app --reload
```

Application URL:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

## 📚 API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
  "message": "Sales Bot Running"
}
```

---

### Chat with Sales Bot

```http
POST /api/v1/sales-bot
```

Request:

```json
{
  "session_id": "123",
  "user_query": "Suggest a laptop under 50000"
}
```

Response:

```json
{
  "reply": "Lenovo IdeaPad Slim 3..."
}
```

---

### Clear Conversation

```http
DELETE /api/v1/sales-bot/clear
```

Request:

```json
{
  "session_id": "123"
}
```

Response:

```json
{
  "message": "Conversation cleared"
}
```

---

### List Products

```http
GET /api/v1/products
```

Optional Query Parameters:

| Parameter | Description           |
| --------- | --------------------- |
| category  | laptop/mobile/tablet  |
| max_price | Maximum product price |

Example:

```http
GET /api/v1/products?category=laptop&max_price=50000
```

---

## 🗄️ Database

Current database:

```text
SQLite
```

Database file:

```text
machi_electronic_store.db
```

Tables:

### Product

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| name     | String  |
| category | String  |
| brand    | String  |
| price    | Float   |
| specs    | String  |
| stock    | Integer |

---

## 🧠 AI Workflow

```text
User Query
      │
      ▼
Query Parsing
(Category / Budget / Brand)
      │
      ▼
Database Search
      │
      ▼
Inventory Context Creation
      │
      ▼
Conversation History
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Response Generation
```

---

## 🔮 Future Enhancements

### Database

* PostgreSQL Support
* Database Migrations with Alembic

### AI

* RAG using Vector Database
* Product Embeddings
* Semantic Search

### Backend

* JWT Authentication
* Role-Based Access Control
* Redis Caching
* Async Database Support

### Deployment

* Docker
* Docker Compose
* GitHub Actions CI/CD
* AWS EC2 Deployment
* Azure App Service Deployment

---

## 🧪 Example Queries

```text
Suggest a laptop under 60k
```

```text
Recommend an Apple product
```

```text
Which Samsung phone is best?
```

```text
Show me tablets below 30k
```

```text
I need headphones for office calls
```

---

## 👨‍💻 Author

Built using:

* FastAPI
* SQLModel
* LangChain
* Google Gemini
* Python

---

## 📄 License

This project is available under the MIT License.
