# Projekt Stand - task_api

Stand: 20.04.2026

## Kurzbeschreibung

Dieses Projekt ist ein Backend fuer eine Todo-App auf Basis von FastAPI, SQLAlchemy und PostgreSQL.
Die aktuelle Basis ist vorhanden, aber das Projekt ist noch nicht vollstaendig ausgebaut.

## Was dieses Projekt gerade macht

- Stellt den Startpunkt fuer eine Todo-API bereit.
- Verbindet sich mit einer PostgreSQL-Datenbank ueber Umgebungsvariablen.
- Definiert Datenmodelle fuer Benutzer und Tasks.
- Definiert Pydantic-Schemas fuer die API-Antworten und Eingaben.
- Bietet aktuell einen ersten Lese-Endpunkt fuer Tasks an.

## Projektstruktur

```text
task_api/
├─ docker-compose.yml
├─ pyproject.toml
├─ README.md
├─ requirements.txt
├─ app/
│  ├─ __init__.py
│  ├─ database.py
│  ├─ main.py
│  ├─ models/
│  │  ├─ __init__.py
│  │  └─ models.py
│  ├─ routers/
│  │  ├─ __init__.py
│  │  └─ routers.py
│  └─ schemas/
│     ├─ __init__.py
│     └─ schema.py
└─ tests/
   └─ __init__.py
```

## Datei fuer Datei

### README.md

Kurzer Projekttext mit dem Hinweis, dass es sich um eine API fuer eine Todo-App handelt.

### pyproject.toml

Definiert das Projekt als Python-Paket `task-api` und listet die verwendeten Abhaengigkeiten:

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- python-dotenv
- python-jose
- passlib
- psycopg2-binary

Fuer Entwicklung sind ausserdem `pytest` und `httpx` eingetragen.

### app/database.py

Hier wird die Datenbankverbindung aufgebaut.

- `load_dotenv()` laedt Umgebungsvariablen aus einer `.env`-Datei.
- Die DB-URL wird aus `POSTGRES_USER`, `POSTGRES_PASSWORD`, `DB_HOST`, `DB_PORT` und `POSTGRES_DB` zusammengesetzt.
- `engine`, `SessionLocal` und `Base` werden fuer SQLAlchemy bereitgestellt.
- `get_db()` liefert eine Session als Dependency fuer FastAPI.
- `test()` prueft die Verbindung mit einem simplen `Select 1`.

Wichtig: In der Datei steht bereits ein Hinweis, dass die DB-URL nicht hart im Repo landen soll und `.env` ignoriert wird.

### app/main.py

Das ist der Einstiegspunkt der API.

- Erzeugt die FastAPI-App mit dem Titel `Todo API`.
- Definiert aktuell den Endpunkt `GET /tasks/`.
- Dieser Endpunkt liest alle Task-Eintraege aus der Datenbank und gibt sie als `TaskResponse` zurueck.

Aktuell ist das der einzige aktive Endpunkt.

### app/models/models.py

Hier sind die SQLAlchemy-Modelle definiert.

- `User` mit `id`, `name`, `email` und `password`.
- `Task` mit `id`, `title`, `completed` und `user_id`.
- Zwischen `User` und `Task` gibt es eine Beziehung ueber `tasks` und `owner`.

Das zeigt, dass das Projekt nicht nur einzelne Tasks, sondern auch Benutzerzuordnung vorsieht.

### app/schemas/schema.py

Hier sind die Pydantic-Modelle fuer die API definiert.

- `TaskBase` beschreibt die Basisfelder eines Tasks.
- `TaskCreate` ist derzeit ein direkter Ableger ohne Zusatzfelder.
- `TaskUpdate` erlaubt optionale Teilupdates.
- `TaskResponse` ergaenzt das Task-Modell um die `id`.

### app/routers/routers.py

Die Datei ist derzeit leer.

Das bedeutet: Die Struktur fuer getrennte Router ist schon vorgesehen, aber die eigentliche Auslagerung von Endpunkten wurde noch nicht begonnen.

### tests/

Der Test-Ordner ist vorhanden, aber es gibt aktuell noch keine Testfaelle.

## Aktueller Entwicklungsstand

Das Projekt ist im fruehen Backend-Aufbau.

Bereits vorhanden:

- FastAPI-Grundgeruest
- Datenbankanbindung
- SQLAlchemy-Modelle
- Pydantic-Schemas
- Erster GET-Endpunkt fuer Tasks
- Docker-Compose-Datei fuer PostgreSQL

Noch nicht fertig:

- CRUD-Endpunkte fuer Tasks
- Endpunkte fuer User
- Authentifizierung und Autorisierung
- Migrationen mit Alembic
- Tests
- Router-Struktur ist noch ungenutzt

## Was hier gerade passiert

Der Code zeigt, dass die Basis fuer eine Todo-API aufgebaut wurde.
Im Fokus stehen aktuell die Verbindung zur Datenbank, das Datenmodell und die erste Auslieferung von Task-Daten ueber FastAPI.

Die naechste logische Entwicklungsphase ist:

1. Endpunkte in Router-Dateien sauber strukturieren.
2. CRUD fuer Tasks und User vervollstaendigen.
3. Datenbankmigrationen einfuehren.
4. Tests aufbauen.
5. Sicherheits- und Konfigurationsdetails sauber auslagern.

## Auffaelligkeiten und Risiken

- Die DB-Verbindungsdaten werden aus Umgebungsvariablen zusammengesetzt, was gut ist, aber die Konfiguration muss sauber gepflegt werden.
- `docker-compose.yml` enthaelt einen Kommentar, dass das Postgres-Image beim Start nicht gefunden wurde. Das sollte bei der naechsten Umgebung nochmal geprueft werden.
- `routers.py` ist leer, obwohl die Projektstruktur Router vorsieht.
- Es gibt noch keine Tests, daher ist der Ist-Zustand nicht abgesichert.

## Praktische Lesart fuer eine KI

Wenn ein anderes KI-System dieses Projekt liest, sollte es so verstehen:

- Das ist ein FastAPI-Backend fuer eine Todo-App.
- Die Datenbank ist PostgreSQL.
- Es gibt schon Modelle und Schemas, aber noch wenig API-Logik.
- Der wichtigste funktionierende API-Teil ist aktuell `GET /tasks/`.
- Das Projekt ist noch in der Aufbauphase und braucht mehr Endpunkte, Tests und Trennung der Verantwortlichkeiten.

## Kurzfazit

Das Projekt ist ein sauberes, aber noch sehr fruehes Grundgeruest fuer eine Todo-API.
Die Architekturidee ist vorhanden, die Implementation ist aber erst teilweise umgesetzt.