# 🌐 Flask Web Framework

Flask is a lightweight and flexible web framework written in Python. It's designed to be easy to use and extend, making it perfect for beginners and professionals building web applications, APIs, or microservices.

## 🚀 Key Features

- 🔧 **Minimal and Flexible**: Micro-framework with no default database or form validation tools.
- 🌍 **Routing**: Clean and easy URL routing.
- 🧠 **Jinja2 Templating**: Powerful templating engine for dynamic content rendering.
- 🔒 **Secure Sessions**: Built-in support for sessions and cookies.
- 📦 **Extensible**: Add only the libraries you need.

## 📦 Commonly Used Flask Extensions

| Extension        | Description                                |
|------------------|--------------------------------------------|
| Flask-WTF        | Form rendering and validation               |
| Flask-Session    | Server-side session management              |
| Flask-SQLAlchemy | ORM for working with databases              |
| Flask-Migrate    | Database migrations using Alembic           |
| Flask-Login      | User authentication and session management  |
| Flask-Mail       | Send emails from your Flask app             |
| Flask-CORS       | Handle Cross-Origin Resource Sharing (CORS) |
| Flask-Bcrypt     | Password hashing                            |
| Flask-RESTful    | Create RESTful APIs easily                  |
| python-dotenv    | Manage environment variables in .env files  |


## 🛠️ Quick Start

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

> Made with ❤️ using Python & Flask