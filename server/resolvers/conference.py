from server.sql_base.models import Conference
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/since.db')

def create(_conference: Conference) -> int:
    new_id = dbmanager.execute(
        query="insert into Conference(name, place, presonalId) values(?, ?, ?)",
        args=(_conference.name, _conference.place, _conference.presonalId)
    )
    return new_id

def get(conference_id: int) -> Conference | None:
    res = dbmanager.execute(
        query='select * from Conference where id=(?)',
        args=(conference_id,)
    )

    return None if not res else Conference(
        id=res[0],
        name=res[1],
        place=res[2],
        presonalId=res[3]
    )
def get_all() -> list[Conference]:
    Conference_list = dbmanager.execute(query="select * from Conference", many=True)
    res = []

    if Conference_list:
        for conference in Conference_list:
            res.append(Conference(
                id=conference[0],
                name=conference[1],
                place=conference[2],
                presonalId=conference[3]
            ))

    return res

def remove(сonference_id: int) -> None:
    return dbmanager.execute('delete from Conference where id=(?)', args=(сonference_id,))

def update(сonference_id: int, new_data: Conference) -> None:
    return dbmanager.execute(
        query='update Conference set (name, place, presonalId) = (?, ?, ?) where id=(?)',
        args=(new_data.name, new_data.place, new_data.presonalId))
