﻿import time

from sqlalchemy import insert, select
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache
from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"],
)

@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Many date many date"

@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query) 
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, details={
            "status": "error",
            "data": None,
            "details": None
        })

# ORM - Object relational model
# SQl Injection

@router.post("/")
async def add_specific_operations(new_operation: OperationCreate,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}