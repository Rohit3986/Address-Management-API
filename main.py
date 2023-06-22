
#-------------------------importing necessary libraries----------------------
import database
import models
from fastapi import FastAPI
import uvicorn
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
app=FastAPI() #creating instance of fastapi

models.database.Base.metadata.create_all(bind=database.engine)

#-------------------------- this endpoint is for adding/creating address entries-------------------
@app.post("/add_address/")
async def create(country:str,state:str,district:str,area:str,house_number:str):
    try:
        session=Session(bind=database.engine,expire_on_commit=False)
        db_user = models.Address(house_number=house_number, area=area,district=district,state=state,country=country)
        session.add(db_user)
        session.commit()
        return {"message":"1 entry added","value":db_user}
    except Exception as e:
        return {"error":str(e),'message':'record not inserted'}



#-------------------------- this block is for updating address entries-------------------
@app.patch("/update_address")
async def update(id: int, country:str,state:str,district:str,area:str,house_number:str):
    try:
        session=Session(bind=database.engine,expire_on_commit=False)
        db_user = session.query(models.Address).get(id)
        if db_user==None:
            return {"message":"no records found"}
        db_user.house_number=house_number
        db_user.area=area
        db_user.district=district
        db_user.country=country
        session.commit()
        db_user_new = session.query(models.Address).get(id)
        return {"message":"updated successfully","old_entry":db_user,"new_entry":db_user_new}
    except Exception as e:
        return {"error":str(e),"message":"record not updated"}


#----------- this endpoint is for reading/retriveing a particular address from database-------------------
@app.get("/get_address_by_address_id/")
def get_address_by_house_id(id:int):
    try:
        session=Session(bind=database.engine,expire_on_commit=False)
        db_user = session.query(models.Address).get(id)

        if db_user==None: #this condition will check that given id is existed or not in our database
            return {"message":"no records found"}
        return {"message":"sucess","value":db_user}
    except Exception as e:
        return {"error":str(e),"message":"something went wrong"}



#----------- this endpoint is for reading/retriveing all address from database-------------------
@app.get("/get_all_entries/")
async def get_address_by_house_id():
    try:
        session=Session(bind=database.engine,expire_on_commit=False)
        db_user = session.query(models.Address).all()
        if db_user==None:
            return {"message":"no records found"}
        return {"message":"all records fecthed successfully","value":db_user}
    except Exception as e:
        return {"error":str(e),"message":"something went wrong"}



#-------------------------- this endpoint is for reading/retriveing all address from database-------------------
@app.get("/get_address_by_state/")
async def get_address_by_house_id(state:str = None):
    try:
        session=Session(bind=database.engine,expire_on_commit=False)
        db_user=session.query(models.Address).filter(models.Address.state==state).all()
        if db_user==None:
            return {"message":"no records found"}
        return {"message":"all records fecthed successfully","value":db_user}
    except Exception as e:
        return {"error":str(e),"message":"something went wrong"}

#-------------------------- this endpoint is for deleting address entries-------------------
@app.post("/delete_address")
async def delete(id:int):
    try:
        session=Session(bind=database.engine,expire_on_commit=False)
        db_user = session.query(models.Address).get(id)
        if db_user==None:
            return {"message":"no records found"}
        id=db_user.address_id
        session.delete(db_user)
        session.commit()
        return {"message":"entry of address id "+id+"deleted sucessfully"}
    except Exception as e:
        return {"error":str(e),'message':'record not deleted'}


# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema
#     openapi_schema = get_openapi(
#         title="Your API Title",
#         version="1.0.0",
#         description="Your API Description",
#         routes=app.routes,
#     )
#     # Modify the schema here if needed
#     app.openapi_schema = openapi_schema
#     return app.openapi_schema

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)
