from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getSquadre():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.teamCode, t.name
                from lahmansbaseballdb.teams t 
                order by t.name  """

        cursor.execute(query, )

        for row in cursor:
            result.append((row["teamCode"], row["name"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAnni(squadra):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.year
                    from lahmansbaseballdb.teams t 
                    where t.teamCode = %s"""

        cursor.execute(query, (squadra, ))

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(squadra):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.year, a2.year as year2, count(a2.playerID) as num
                from lahmansbaseballdb.appearances a, lahmansbaseballdb.appearances a2 
                where a2.year > a.year and a2.teamCode = %s and a2.teamCode = a.teamCode
                and a2.playerID = a.playerID
                group by a2.year, a.year"""

        cursor.execute(query, (squadra, ))

        for row in cursor:
            result.append((row["year"], row["year2"], row["num"]))

        cursor.close()
        conn.close()
        return result