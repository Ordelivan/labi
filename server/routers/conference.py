from fastapi import APIRouter
from server.sql_base.models import Conference
from server.resolvers import conference


router = APIRouter(prefix='/Conference', tags=['Conference'])

@router.post('/create')
def create(_Conference: Conference) -> int:
    new_id = conference.create(_Conference)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{conference_id}')
def get(conference_id: int) -> Conference | None:
    return conference.get(conference_id)

@router.get('/')
def get_all() -> list[Conference] | None:
    return conference.get_all()

@router.get('/remove/{conference_id}')
def remove(conference_id: int) -> None:
    return conference.remove(conference_id)


@router.put("/update/{conference_id}")
def update(conference_id: int, new_data: Conference):
    return conference.update(conference_id=conference_id, new_data=new_data)

