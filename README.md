# Fullstack Quiz

Technical quiz with a FastAPI backend challenge and a React frontend challenge.

## FastAPI (test-fastapi)

Complete the TODOs in `main.py` to build a simple CRUD API for users.

### Setup

```bash
cd test-fastapi
python3 -m venv venv
venv\Scripts\activate              # On Mac: source venv/bin/activate
pip install -r requirements.txt
```

### Run tests

```bash
venv\Scripts\pytest test_solution.py -v   # On Mac: make test
```

### Run the server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. Docs at `http://localhost:8000/docs`.

---

## React (test-react)

Complete the `DataFetcher.jsx` component to fetch and display data from an API.

### Setup

```bash
cd test-react
npm install
```

### Run tests

```bash
npx jest --verbose                # On Mac: make run-test
```

### Run the dev server

```bash
npm run dev
```

Open http://localhost:5173/ to see the component in the browser.
