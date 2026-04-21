from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from agent import run_agent
   

app = FastAPI(title="FastMCP + OpenRouter Weather Agent")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>FastMCP + OpenRouter AI Agent</title>
            <style>
                body {
                    margin: 0;
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #1e3c72, #2a5298);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .card {
                    background: white;
                    padding: 40px;
                    border-radius: 15px;
                    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
                    text-align: center;
                    width: 450px;
                }
                input {
                    width: 100%;
                    padding: 12px;
                    margin-bottom: 20px;
                    border-radius: 8px;
                    border: 1px solid #ccc;
                }
                button {
                    width: 100%;
                    padding: 12px;
                    border: none;
                    border-radius: 8px;
                    background: #1e3c72;
                    color: white;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background: #16305c;
                }
                .result {
                    margin-top: 20px;
                    padding: 15px;
                    background: #f4f4f4;
                    border-radius: 8px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🌍 FastMCP + OpenRouter Weather Agent</h2>
                <form method="post">
                    <input type="text" name="message" placeholder="Ask about weather..." required>
                    <button type="submit">Ask</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/", response_class=HTMLResponse)
async def ask(message: str = Form(...)):
    result = run_agent(message)

    return f"""
    <html>
        <body style="margin:0;font-family:'Segoe UI';background:linear-gradient(135deg,#1e3c72,#2a5298);display:flex;justify-content:center;align-items:center;height:100vh;">
            <div style="background:white;padding:40px;border-radius:15px;box-shadow:0 15px 40px rgba(0,0,0,0.3);text-align:center;width:450px;">
                <h2>🌍 Weather Result</h2>
                <div style="margin:20px 0;padding:15px;background:#f4f4f4;border-radius:8px;">
                    {result}
                </div>
                <a href="/" style="text-decoration:none;padding:10px 20px;background:#1e3c72;color:white;border-radius:8px;">Ask Again</a>
            </div>
        </body>
    </html>
    """