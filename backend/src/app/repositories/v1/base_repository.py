from uuid import UUID

from pydantic import BaseModel


class BaseRepository:
    def __init__(self, dao):
        self.dao = dao

    def find_by_id(self, obj_id: str, *args, **kwargs):
        return self.dao.find_by_id(obj_id, *args, **kwargs)

    #
    # def find_all(self, created_by: str, *args, **kwargs):
    #     return self.dao.find_all(created_by, *args, **kwargs)
    #
    # def find_by_ids(self, object_ids: list[UUID | int], created_by: str, *args, **kwargs):
    #     return self.dao.find_by_ids(object_ids, created_by, *args, **kwargs)
    #
    # def create_one(self, dto: BaseModel, created_by: str, *args, **kwargs):
    #     return self.dao.create_one(dto, created_by, *args, **kwargs)
    #
    # def update_one(self, dto: BaseModel, object_id: UUID | int,  updated_by: str, *args, **kwargs):
    #     return self.dao.update_one(dto, object_id, updated_by, *args, **kwargs)
    #
    # def delete_one(self, object_id: UUID | int, deleted_by: str, *args, **kwargs):
    #     return self.dao.delete_one(object_id, deleted_by, *args, **kwargs)
