# Real-Time Multiplayer Strategy Game with Deterministic Lockstep Netcode

Age-of-Empires style RTS built from scratch with deterministic simulation — all clients stay in sync from inputs alone (no state sync). Determinism across platforms, plus A* pathfinding, fog of war, unit AI is famously tricky.

## Architecture
- **Backend:** Python (deterministic sim) + Django, PostgreSQL (sqlite fallback)
- **Frontend:** React 18 + Vite + Canvas (game) + WebSockets (mock lockstep)
- **15 Apps:** simulation, networking, pathfinding, units, buildings, fog_of_war, determinism, commands, world, ai, economy, combat, frontend, api, analytics

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
```

## Build
```bash
make build
docker build -t rts-game .
npm run build
```

## Run
```bash
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
npm run dev
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
```

## Features
- **Deterministic lockstep:** fixed-point `16.16`, tick `16ms (60Hz)`, input sync only, hash `FNV-1a` per tick, replay from inputs
- **Cross-platform determinism:** no `Math.random()`, no `Date.now()` in sim, sorted `dict` iteration
- **Pathfinding:** A* deterministic (`heapq` with tie-breaker `counter`), flow fields for groups
- **Fog of war:** vision `5 tiles`, shroud, exploration
- **Units:** infantry/archers/cavalry with formation, attack, patrol AI

## License
Proprietary — All rights reserved.
