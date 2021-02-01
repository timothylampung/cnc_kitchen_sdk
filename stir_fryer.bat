echo preparing env on %cd%
%cd%\venv\Scripts\activate && set FLASK_APP=stir_fry_app.py && python -m flask run --host 192.168.1.13 --port 5000
PAUSE