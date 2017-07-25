
class Utils():

    @classmethod
    def todict(self,result):
        ls = []
        dictresult = {}
        for emp in result:
            d = {}
            for column in emp.__table__.columns:
                d[column.name] = str(getattr(emp, column.name))
            ls.append(d)
            dictresult = {"result" : ls}
        return dictresult