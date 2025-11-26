from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List

# ----------- Load Artifacts -----------
movies = pd.read_pickle("movies.pkl")
neighbors = joblib.load("neighbors.pkl")

app = FastAPI(title="Movie Recommender API", version="2.0")

class RecommendResponse(BaseModel):
    query: str
    recommendations: List[str]

@app.get("/recommend", response_model=RecommendResponse)
def recommend(title: str = Query(..., description="Exact movie title"), top_n: int = 5):
    if title not in neighbors:
        suggestions = movies[movies['title'].str.contains(title, case=False, na=False)]['title'].head(5).tolist()
        raise HTTPException(status_code=404, detail={
            "error": f"Title '{title}' not found.",
            "suggestions": suggestions
        })

    recs = neighbors[title][:top_n]
    return {"query": title, "recommendations": recs}

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
