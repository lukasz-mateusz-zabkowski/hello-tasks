@echo off
REM Run FastAPI dev server (Windows)
REM Assumes you run from project root and venv is available in .venv


if exist .venv\Scripts\activate.bat (
call .venv\Scripts\activate.bat
) else (
echo [ERROR] .venv not found. Create it first: py -m venv .venv
exit /b 1
)


python -m uvicorn app.main:app --reload