"""
AgentOS
-------

The main entry point for AgentOS.

Run:
    python -m app.main
"""

from pathlib import Path

from agno.os import AgentOS
from agents.mcp_agent import mcp_agent
from fastapi import FastAPI
from db import get_postgres_db

# Create custom FastAPI app
app: FastAPI = FastAPI(
    title="Custom FastAPI App",
    version="1.0.0",
)


# Add your own routes
@app.post("/customers")
async def get_customers():
    return [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "email": "jane.doe@example.com",
        },
    ]


# ---------------------------------------------------------------------------
# Create AgentOS
# ---------------------------------------------------------------------------
agent_os = AgentOS(
    name="AgentOS",
    tracing=True,
    scheduler=True,
    db=get_postgres_db(),
    agents=[mcp_agent],
    config=str(Path(__file__).parent / "config.yaml"),
    base_app=app,
)

app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(
        app="main:app",
        reload=True,
    )
