# Django Multilingual FAQ API

## 🚀 Overview

This project is a Django-based REST API for managing Frequently Asked Questions (FAQs) with multilingual support. It includes a WYSIWYG editor for rich text formatting, automated translation using Google Translate, caching with Redis, and a user-friendly Django admin panel.

## 📌 Features

- **FAQ Model** with multilingual support
- **WYSIWYG Editor** using `django-ckeditor`
- **REST API** with language-based retrieval
- **Caching** using Redis for improved performance
- **Automated Translations** using `googletrans`
- **Admin Panel** for easy management
- **Unit Tests** with `pytest`
- **PEP8 Compliance** with `flake8`

---

## 🛠 Installation

### Prerequisites

Before proceeding, ensure you have the following installed on your system:

- **Python**: Version 3.8 or higher. [Download Python](https://www.python.org/downloads/)
- **Redis**: For caching translations. [Install Redis](https://redis.io/download)
- **Git**: To clone the repository. [Install Git](https://git-scm.com/downloads)

### Step 1: Clone the Repository

```sh
git clone https://github.com/SambhavDeev/FAQ_backend.git
cd FAQ_backend
```

### Step 2: Create a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```sh
pip install -r requirements.txt
```

### Step 4: Set Up the Database

```sh
python manage.py migrate
python manage.py createsuperuser
```

### Step 5: Start Redis

```sh
redis-server
```

### Step 6: Run the Development Server

```sh
python manage.py runserver
```

---

## 🔥 API Usage

### Fetch FAQs in English (default)

```sh
curl http://localhost:8000/api/faqs/
```

### Fetch FAQs in Hindi

```sh
curl http://localhost:8000/api/faqs/?lang=hi
```

### Fetch FAQs in Bengali

```sh
curl http://localhost:8000/api/faqs/?lang=bn
```

---

## ⚙️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default), can be switched to PostgreSQL
- **Caching:** Redis
- **Translation:** Google Translate API / googletrans
- **WYSIWYG Editor:** django-ckeditor

---

## ✅ Testing & Linting

### Run Unit Tests

```sh
pytest
```

### Run Linting (PEP8 Compliance)

```sh
flake8 .
```

---

## 📜 Git Commit Guidelines

Use conventional commit messages:

- `feat: Add multilingual FAQ model`
- `fix: Improve translation caching`
- `docs: Update README with API examples`
- `chore: Add Dockerfile and docker-compose.yml`
- `test: Add unit tests for FAQ model`

---

## 📦 Deployment (Bonus)

### Run with Docker

```sh
docker-compose up --build
```

### Deploy to Heroku

```sh
git push heroku main
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'feat: Add feature-name'`)
4. Push to branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 📧 Contact

For any queries, reach out to: `devsambhav5@gmail.com`


