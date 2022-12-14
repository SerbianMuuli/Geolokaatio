@ECHO OFF

pushd %~dp0

Set "VIRTUAL_ENV=proj_venv"

IF NOT EXIST "%VIRTUAL_ENV%\Scripts\activate.bat" (
	pip.exe install virtualenv
    	python -m venv %VIRTUAL_ENV%
)

CALL proj_venv\Scripts\activate.bat
ECHO ON
CALL python -m pip install --upgrade pip
CALL pip install -r requirements.txt
CALL python manage.py migrate
CALL python manage.py runserver
