import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the web server
app = FastAPI()

# 2. Define what a request looks like (two numbers: a and b)
class ComputeRequest(BaseModel):
    a: int
    b: int

# 3. The Health Check (just to see if the site is "alive")
@app.get("/health")
async def health():
    return {"status": "ok"}

# 4. The Math Logic
@app.post("/compute")
async def compute(req: ComputeRequest):
    s = req.a + req.b        # Sum: 14 + 10 = 24
    p = req.a * req.b        # Product: 14 * 10 = 140
    
    # Create the verification hash (The Secret Fingerprint)
    hash_input = f"sum:{s}:product:{p}"
    v = hashlib.sha256(hash_input.encode()).hexdigest()[:10]
    
    return {"sum": s, "product": p, "verify": v}
