import pymongo
import time
from config import mongo


class Mongo(object):
    @classmethod
    def new(cls, form):
        name = cls.__name__.lower()
        query = {k: v for k, v in form.items()}
        query.update(created_time=time.time(), deleted=False)
        mongo[name].insert(query)

    # 逻辑数据
    @classmethod
    def find(cls, flag=pymongo.ASCENDING):
        name = cls.__name__.lower()
        ms = mongo[name].find(dict(deleted=False)).sort('_id', flag)
        return ms

    # 全部数据
    @classmethod
    def _find(cls, flag=pymongo.ASCENDING):
        name = cls.__name__.lower()
        ms = mongo[name].find().sort('_id', flag)
        return ms

    @classmethod
    def all_limit(cls, num, flag=pymongo.ASCENDING):
        ms = cls.find().sort('_id', flag).limit(num)
        return ms

    @classmethod
    def find_one(cls, **kwargs):
        name = cls.__name__.lower()
        kwargs.update(deleted=False)
        m = mongo[name].find_one(kwargs)
        return m

    # 逻辑删除
    @classmethod
    def delete(cls, **kwargs):
        m = cls.find_one(**kwargs)
        m['deleted'] = True
        name = cls.__name__.lower()
        mongo[name].save(m)

    # 更新
    @classmethod
    def update(cls, form, **kwargs):
        m = cls.find_one(**kwargs)
        for k, v in form.items():
            m[k] = v
        name = cls.__name__.lower()
        mongo[name].save(m)











