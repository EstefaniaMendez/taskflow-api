
from fastapi import FastAPI, HTTPException 

app = FastAPI()
from pydantic import BaseModel
class TareaNueva(BaseModel):
    nombre: str
    estado: str = "pendiente"

tareas = [
    {
        "id": 1,
        "nombre": "Estudiar FastAPI",
        "estado": "pendiente"
    },
    {
        "id": 2,
        "nombre": "Crear mi primer proyecto",
        "estado": "pendiente"
    },
    {
        "id": 3,
        "nombre": "Aprender Python",
        "estado": "pendiente"
    }
]

@app.get("/")
def inicio():
    return {"mensaje": "TaskFlow API funcionando"}

@app.get("/tareas")
def obtener_tareas():
    return tareas

@app.get("/tareas/{id}")
def obtener_tarea(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return tarea
    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


@app.post("/tareas", status_code=201)
def crear_tarea(datos: TareaNueva):
    nueva_tarea = {
        "id":max(tarea["id"] for tarea in tareas) + 1,
        "nombre": datos.nombre,
        "estado": datos.estado
    }
    tareas.append(nueva_tarea)
    return nueva_tarea 

@app.put("/tareas/{id}")
def actualizar_tarea(id:int, datos: TareaNueva):
    for tarea in tareas:
        if tarea["id"]==id:
            tarea["nombre"]= datos.nombre
            tarea["estado"]= datos.estado
            return tarea

    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@app.delete("/tareas/{id}")
def eliminar_tarea(id:int):
    for tarea in tareas:
        if tarea["id"]== id:
            tareas.remove(tarea)
            return {"mensaje":"Tarea eliminada correctamente"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")