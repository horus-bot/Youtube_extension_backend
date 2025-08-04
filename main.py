from fastapi import FastAPI
from fastapi.responses import JSONResponse
from groq_summary import groq_summary
from tamil import tamil
from hindi import hindi 

app = FastAPI()

@app.get("/summarize")
async def summarize(url:str):
    try:
        result = groq_summary(url)
        return JSONResponse(content={"summary": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/tamil")
async def tamil_translation(url:str):
    try:
        result=tamil(url)
        return JSONResponse(conten={"summary": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500) 
    
@app.get("/hindi")
async def hindi_translation(url:str):
    try:
        result=hindi(url)
        return JSONResponse(conten={"summary": result})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)     