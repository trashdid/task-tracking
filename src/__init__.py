from fastapi import FastAPI

api_config = {
    "title": "Task Tracking API",
    "summary": "Basic Task Tracking API",
    "description": "This is a simple CRUD API to demonstrate task tracking",
    "docs_url": None,
    "redoc_url": None,
    "contact": {
        "name": "Siddharth Karunakaran",
        "url": "https://www.linkedin.com/in/siddharthkarunakaran/"
    }
}

app = FastAPI(**api_config)