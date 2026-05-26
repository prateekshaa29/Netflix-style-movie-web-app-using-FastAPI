from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

hit_count = 0

MOVIES = [
    {
        "title": "Interstellar",
        "genre": ["Sci-Fi", "Adventure"],
        "rating": 4.8,
        "duration": "2h 49m",
        "language": "English",
    },
    {
        "title": "Leo",
        "genre": ["Action", "Drama"],
        "rating": 4.4,
        "duration": "2h 44m",
        "language": "Tamil",
    },
    {
        "title": "Jawan",
        "genre": ["Action", "Thriller"],
        "rating": 4.5,
        "duration": "2h 49m",
        "language": "Hindi",
    },
    {
        "title": "Avengers: Endgame",
        "genre": ["Superhero", "Action"],
        "rating": 4.9,
        "duration": "3h 2m",
        "language": "English",
    },
    {
        "title": "Vikram",
        "genre": ["Action", "Crime"],
        "rating": 4.7,
        "duration": "2h 54m",
        "language": "Tamil",
    },
    {
        "title": "Your Name",
        "genre": ["Anime", "Romance"],
        "rating": 4.6,
        "duration": "1h 46m",
        "language": "Japanese",
    },
]

HTML_PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Movies for You</title>

<style>
  body {
    font-family: Arial, sans-serif;
    background: #111;
    color: white;
    max-width: 1000px;
    margin: auto;
    padding: 20px;
  }

  h1 {
    color: #ff3c3c;
  }

  .visitor {
    color: #bbb;
    margin-bottom: 20px;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
  }

  .card {
    background: #1e1e1e;
    padding: 16px;
    border-radius: 10px;
    border: 1px solid #333;
  }

  .card h2 {
    margin-top: 0;
    color: #ffcc00;
  }

  .meta {
    color: #ddd;
    line-height: 1.6;
  }

  .rating {
    color: #00ff88;
    font-weight: bold;
  }
</style>

</head>

<body>

<h1>🎬 Movies for You</h1>

<div class="visitor">
  You are visitor #__COUNT__
</div>

<div id="grid" class="grid"></div>

<script>

fetch('/movies')
  .then(response => response.json())
  .then(data => {

    const grid = document.getElementById('grid');

    for (const movie of data.movies) {

      const card = document.createElement('div');

      card.className = 'card';

      card.innerHTML = `
        <h2>${movie.title}</h2>

        <div class="meta">
          <div>${movie.genre.join(', ')}</div>

          <div>
            <span class="rating">★ ${movie.rating}</span>
          </div>

          <div>${movie.duration}</div>

          <div>${movie.language}</div>
        </div>
      `;

      grid.appendChild(card);
    }
  });

</script>

</body>
</html>
"""


@app.get("/movies")
async def get_movies(request: Request):

    client_ip = request.client.host if request.client else "unknown"

    print(f"[{hit_count}] {client_ip} -> /movies", flush=True)

    return {"movies": MOVIES}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    global hit_count

    hit_count += 1

    client_ip = request.client.host if request.client else "unknown"

    print(f"[{hit_count}] {client_ip} -> /", flush=True)

    return HTMLResponse(
        HTML_PAGE.replace("__COUNT__", str(hit_count))
    )