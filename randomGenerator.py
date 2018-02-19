class FetchBadWord():

    #init
    def __init__(self, cur):
        self.cur = cur

    def english(self):
        #get a random entry english table
        self.cur.execute("select * from english offset random() * (select count(*) from english) limit 1 ;")
        rows = self.cur.fetchone()
        return (rows[0])

    def hindi(self):
        #get a random entry from hindi table
        self.cur.execute("select * from hindi offset random() * (select count(*) from hindi) limit 1 ;")
        rows = self.cur.fetchone()
        #since an list will be returned, although of length 1, parse it to return only data
        return (rows[0])