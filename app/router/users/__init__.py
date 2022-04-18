from fastapi import APIRouter, Response, status
from .service import read_users, add_user

router = APIRouter(
    prefix="/users",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", status_code=status.HTTP_200_OK)
async def get_users(response: Response):

    try:
        users = read_users()
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"message": "Server has some error~~!!!"}

    if users is None:
        response.status_code = status.HTTP_404_NOT_FOUND

    return {"users": users}
