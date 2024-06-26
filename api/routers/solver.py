from fastapi import APIRouter, UploadFile, Form, File
from typing import Annotated
import importlib

router = APIRouter()


@router.post("/solver")
async def solve(day: Annotated[int, Form()],year: Annotated[int, Form()], part: Annotated[int, Form()],text: Annotated[UploadFile, File()]):
    module = importlib.import_module(f"api.solvers.{year}.day{day}.solver")
    importlib.reload(module)
    solver = getattr(module, f'part{part}')
    content = await text.read()
    return solver(content.decode('utf-8').split('\n')[:-1])
