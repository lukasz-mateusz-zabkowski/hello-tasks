# \# Hello Tasks API

# 

# Proste API edukacyjne do zarządzania zadaniami.  

# Projekt realizowany krok po kroku w ramach nauki \*\*backendu (Python, FastAPI)\*\* z naciskiem na \*\*dobre praktyki, HTTP, Git i bezpieczeństwo\*\*.

# 

# ---

# 

# \## 🎯 Cel projektu

# 

# Celem projektu jest:

# \- zbudowanie \*\*realnego backendowego API\*\* od zera,

# \- nauka pracy z \*\*Git/GitHub\*\*,

# \- zrozumienie \*\*HTTP, walidacji danych i logowania\*\*,

# \- przygotowanie fundamentu pod \*\*bazę danych i bezpieczeństwo\*\*.

# 

# Projekt rozwijany iteracyjnie (tydzień po tygodniu).

# 

# ---

# 

# \## 🧱 Stack technologiczny

# 

# \- \*\*Python 3.11+\*\*

# \- \*\*FastAPI\*\*

# \- \*\*Uvicorn\*\*

# \- \*\*PostgreSQL\*\* (Docker)

# \- \*\*Git / GitHub\*\*

# \- \*\*Docker / Docker Compose\*\*

# 

# ---

# 

# \## 📂 Struktura projektu

# hello-tasks/

# ├── app/

# │ ├── init.py

# │ ├── main.py # FastAPI app

# │ ├── logger.py # Logging z rotacją

# │ ├── log\_demo.py # Demo loggera

# │ ├── json\_parser.py # Walidacja danych (Day 2)

# │ └── api/

# │ ├── init.py

# │ └── routes.py # Endpointy API

# │

# ├── notes/

# │ └── http.md # Notatki HTTP

# │

# ├── scripts/

# │ └── run\_dev.bat # Uruchamianie API (Windows)

# │

# ├── docker-compose.yml # PostgreSQL (Docker)

# ├── requirements.txt

# ├── README.md

└── .gitignore


===

# ---

# 

# \## 📅 Zakres zrealizowany – Tydzień 1

# 

# \### ✅ Dzień 1 – Fundamenty

# \- Git: init, commit, branch, push

# \- Struktura projektu

# \- README + plan MVP

# 

# \### ✅ Dzień 2 – Python Core

# \- typy, funkcje, wyjątki

# \- `dataclasses`

# \- walidacja danych JSON → obiekt

# 

# \### ✅ Dzień 3 – OOP + HTTP

# \- klasy, dziedziczenie, kompozycja

# \- notatki HTTP (metody, statusy, nagłówki)

# \- cookies vs tokeny

# 

# \### ✅ Dzień 4 – Git + Logging

# \- merge vs rebase

# \- tagi i release

# \- logging produkcyjny (rotacja plików)

# 

# \### ✅ Dzień 5 – SQL + PostgreSQL

# \- tabele, PK, FK, indeksy

# \- PostgreSQL w Dockerze

# \- pierwsza tabela `tasks`

# 

# \### ✅ Dzień 6 – FastAPI

# \- FastAPI + Uvicorn

# \- endpointy:

# &nbsp; - `GET /health`

# &nbsp; - `GET /tasks`

# \- struktura API

# 

# \### ✅ Dzień 7 – DX + Dokumentacja

# \- Swagger / OpenAPI (`/docs`)

# \- modele odpowiedzi (Pydantic)

# \- skrypty uruchomieniowe

# \- kompletne README

# 

# ---

# 

# \## 🚀 Endpointy API

# 

# \### Health check





