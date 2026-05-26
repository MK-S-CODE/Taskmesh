from fastapi import FastAPI
from api.Router import api_router 
from shared.config.settings import APP_NAME

app = FastAPI()

print(APP_NAME)
app.include_router(api_router)

