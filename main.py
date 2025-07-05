from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from gemini_utils import get_representatives_info
from database import init_db, get_db, RepresentativeDB
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# Load environment variables at startup
load_dotenv(verbose=True)
print(f"GEMINI_API_KEY in main.py: {'GEMINI_API_KEY' in os.environ}")

app = FastAPI(
    title="Indian Public Representatives API",
    description="API to get information about local public representatives in Indian cities",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class Representative(BaseModel):
    name: str
    designation: str
    phone: Optional[str] = None
    email: Optional[str] = None
    verified: Optional[bool] = False

class RepresentativeUpdate(BaseModel):
    name: str
    designation: str
    phone: Optional[str] = None
    email: Optional[str] = None

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/representatives/{city}", response_model=List[Representative])
async def get_representatives(city: str, db: AsyncSession = Depends(get_db)):
    # First check database for verified representatives
    query = select(RepresentativeDB).where(RepresentativeDB.city == city.lower())
    result = await db.execute(query)
    db_reps = result.scalars().all()
    
    if db_reps:
        return [
            Representative(
                name=rep.name,
                designation=rep.designation,
                phone=rep.phone,
                email=rep.email,
                verified=rep.verified == 1
            ) for rep in db_reps
        ]
    
    # If no data in database, get from Gemini AI
    try:
        ai_reps = await get_representatives_info(city)
        
        # Store AI-generated data in database
        for rep in ai_reps:
            db_rep = RepresentativeDB(
                name=rep["name"],
                designation=rep["designation"],
                phone=rep.get("phone"),
                email=rep.get("email"),
                city=city.lower(),
                verified=0
            )
            db.add(db_rep)
        
        await db.commit()
        
        return [Representative(**rep, verified=False) for rep in ai_reps]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update_representative", response_model=Representative)
async def update_representative(
    rep: RepresentativeUpdate,
    db: AsyncSession = Depends(get_db)
):
    query = select(RepresentativeDB).where(
        RepresentativeDB.name == rep.name,
        RepresentativeDB.designation == rep.designation
    )
    result = await db.execute(query)
    db_rep = result.scalar_one_or_none()
    
    if not db_rep:
        raise HTTPException(status_code=404, detail="Representative not found")
    
    if rep.phone is not None:
        db_rep.phone = rep.phone
    if rep.email is not None:
        db_rep.email = rep.email
    db_rep.verified = 1
    
    await db.commit()
    
    return Representative(
        name=db_rep.name,
        designation=db_rep.designation,
        phone=db_rep.phone,
        email=db_rep.email,
        verified=True
    )
port = int(os.environ.get("PORT", 8000))
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
