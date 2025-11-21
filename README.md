Proyecto: Portal informativo - Escuela Joaquín García Monge (React + Django)
============================================================================

Contenido del ZIP:
- backend/: Django project y app 'schoolapi' (models, serializers, views, urls)
- frontend/: React + Vite app (JSX components, CSS)
- EVALUATION.md : rúbrica
- backend/fixture.json : datos de ejemplo extraídos de las imágenes

Instrucciones resumidas:
1) Backend
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py loaddata fixture.json
   python manage.py createsuperuser
   python manage.py runserver

2) Frontend
   cd frontend
   npm install
   npm run dev

3) Abrir http://localhost:5173 (frontend) y http://127.0.0.1:8000/admin (backend admin)

Notas:
- Cambia SECRET_KEY en backend/backend/settings.py antes de producción.
- Para JWT instalar paquetes y configurar (se incluye endpoints en urls).
