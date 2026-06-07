from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Movies for You</title>

<style>
body{
    margin:0;
    background:#000;
    font-family:Arial, sans-serif;
    color:white;
}

.container{
    width:80%;
    margin:40px auto;
}

h1{
    color:#ff4d4d;
    font-size:36px;
    margin-bottom:10px;
}

.visitor{
    color:#bdbdbd;
    margin-bottom:20px;
    font-size:18px;
}

.movies{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:15px;
}

.card{
    background:#1a1a1a;
    border-radius:8px;
    padding:15px;
}

.title{
    color:#d4a017;
    font-size:24px;
    font-weight:bold;
    margin-bottom:10px;
}

.genre{
    color:#d0d0d0;
    font-size:14px;
    margin-bottom:8px;
}

.rating{
    color:#00ff66;
    font-weight:bold;
    margin-bottom:8px;
}

.duration{
    color:#bdbdbd;
    font-size:14px;
}

.language{
    color:#bdbdbd;
    font-size:14px;
}
</style>
</head>

<body>

<div class="container">

<h1>🎬 Movies for You</h1>

<div class="visitor">
You are visitor #1
</div>

<div class="movies">

<div class="card">
<div class="title">Interstellar</div>
<div class="genre">Sci-Fi, Adventure</div>
<div class="rating">★ 4.8</div>
<div class="duration">2h 49m</div>
<div class="language">English</div>
</div>

<div class="card">
<div class="title">Leo</div>
<div class="genre">Action, Drama</div>
<div class="rating">★ 4.4</div>
<div class="duration">2h 44m</div>
<div class="language">Tamil</div>
</div>

<div class="card">
<div class="title">Jawan</div>
<div class="genre">Action, Thriller</div>
<div class="rating">★ 4.5</div>
<div class="duration">2h 49m</div>
<div class="language">Hindi</div>
</div>

<div class="card">
<div class="title">Avengers: Endgame</div>
<div class="genre">Superhero, Action</div>
<div class="rating">★ 4.9</div>
<div class="duration">3h 2m</div>
<div class="language">English</div>
</div>

<div class="card">
<div class="title">Vikram</div>
<div class="genre">Action, Crime</div>
<div class="rating">★ 4.7</div>
<div class="duration">2h 54m</div>
<div class="language">Tamil</div>
</div>

<div class="card">
<div class="title">Your Name</div>
<div class="genre">Anime, Romance</div>
<div class="rating">★ 4.6</div>
<div class="duration">1h 46m</div>
<div class="language">Japanese</div>
</div>

</div>

</div>

</body>
</html>
"""

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    print("=" * 50)
    print("Server running at: http://localhost:8000")
    print("Press CTRL + C to stop the server")
    print("=" * 50)

    server = HTTPServer(("0.0.0.0", 8000), Handler)
    server.serve_forever()