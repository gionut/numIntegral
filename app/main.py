from fastapi import FastAPI, HTTPException
import math

app = FastAPI()


@app.get("/integral/{lower}/{upper}")
async def root(lower: float, upper: float):
    if lower > upper:
        raise HTTPException(status_code=500, detail="The values of lower and upper path parameters should be increasing.")
    
    result = {}
    loops = 7
    N = 1
    for _ in range(loops):
        N = N*10 
        dx = (upper - lower) / N
        integral = 0.0
        for i in range(N):
            x = lower + i * dx
            integral += math.fabs(math.sin(x)) * dx
        result[N] = integral

    return result