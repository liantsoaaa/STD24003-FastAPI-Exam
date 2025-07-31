from fastapi  import FastAPI, Request, Response, status #type: ignore
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# Q1 
@app.get("/ping", response_class=PlainTextResponse)
async def ping():
    return Response(content="pong", media_type="text/plain", status_code=200)

# Q2
@app.get("/home", response_class=HTMLResponse)
async def home():
    
    html_content = "<html><body><h1>Welcome home!</h1></body></html>"
    return HTMLResponse(content=html_content, status_code=200)

# Q3
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc):
    return HTMLResponse(
        content="<html><body><h1>404 NOT FOUND</h1></body></html>",
        status_code=404
    )
    
# Q4
total_posts = []

class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime 
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(new_posts: List[Post]):
    for post in new_posts:
        total_posts.append(post)
    return total_posts

# Q5
@app.post("/posts")
async def get_posts():
    return total_posts

# Q6
@app.put("/posts")
async def modify_or_add_posts(modified_posts: List[Post]):
    titles= {post.title: i for i, post in enumerate(total_posts)}
    for new_post in modified_posts:
        if new_post.title in titles:
            new_modification = titles[new_post.title]
            if total_posts[new_modification] != new_post:                          
                total_posts[new_modification] = new_post
        else:
            total_posts.append(new_post)                                                                                                                                           
            
        

