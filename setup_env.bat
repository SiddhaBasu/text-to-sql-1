@echo off
REM setup_env.bat - Sets up Python environment and installs requirements
python -m venv ..\venv
call ..\venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r ..\requirements.txt

echo Setup complete. Activate your environment with "..\venv\Scripts\activate".
