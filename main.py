from fastapi import FastAPI


from src.utils.healthchecker import router as healthchecker_router
from src.routes.contacts import router as contacts_router

app = FastAPI()
routes = [healthchecker_router, contacts_router]
for router in routes:
    app.include_router(router=router, prefix="/api")
