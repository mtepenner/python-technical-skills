# Python Technical Skills Showcase

!
A curated collection of Python implementations demonstrating core engineering competencies. This repository serves as a technical reference for best practices in backend development, system design, and algorithmic problem-solving.

## 📋 Table of Contents
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Core Modules](#-core-modules)
- [License](#-license)

## 🚀 Features
* **RESTful API Design**: Drone Mesh Network implementation using FastAPI with Pydantic validation.
* **Concurrency**: Asynchronous I/O operations using `asyncio` and `gather` for non-blocking tasks.
* **Database Integration**: ORM implementation for Telemetry Data using SQLAlchemy and SQLite.
* **Problem Solving**: Optimized implementations of Two Pointers, Sliding Window, and Breadth-First Search (BFS) patterns.
* **Pythonic Features**: Advanced usage of decorators, generators, list/dict comprehensions, and context managers.
* **Robust Testing**: Unit testing suite using the `unittest` module for edge-case validation.

## 🛠️ Technologies Used
* **Language**: Python 3.x
* **Web Framework**: FastAPI
* **Database/ORM**: SQLAlchemy, SQLite
* **Validation**: Pydantic
* **Testing**: Unittest

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/python-technical-skills.git
    cd python-technical-skills
    ```

2.  **Install dependencies:**
    ```bash
    pip install fastapi sqlalchemy pydantic uvicorn
    ```

## 💻 Usage

### Running the API
To launch the Drone Mesh Network API:
```bash
uvicorn api-design:app --reload
```

### Running Unit Tests
To execute the test suite:
```bash
python -m unittest testing-fundamentals.py
```

### Database Interaction
To run the telemetry database demonstration:
```bash
python database-basics.py
```

## 📂 Core Modules

| File | Focus | Key Concept |
| :--- | :--- | :--- |
| `api-design.py` | Web Services | POST/GET endpoints, HTTP status codes |
| `concurrency.py` | Performance | Async/Await, concurrent task execution |
| `core-data-structures.py` | Efficiency | Time complexity of Lists, Sets, and Dicts |
| `oop.py` | Architecture | Inheritance, dunder methods, and encapsulation |
| `problem-solving-patterns.py` | Algorithms | Memory-efficient traversal and search |
| `pythonic-features.py` | Idiomatic Code | Generators for memory efficiency |

## ⚖️ License
This project is licensed under the MIT License.
