from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/mult")
def multiply(op1: float = Query(...), op2: float = Query(...)):
    resultado = op1 * op2
    return {"op1": op1, "op2": op2, "resultado": resultado}
