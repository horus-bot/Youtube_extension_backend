from fastapi import FastAPI
from fastapi.responses import JSONResponse
from groq_summary import groq_summary

app = FastAPI()

@app.get("/summarize")
async def summarize(url:str):
    try:
        result = groq_summary(url)
        return JSONResponse(content={"summary": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
