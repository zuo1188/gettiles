import psycopg2
conn = psycopg2.connect(database="basemap",user='postgres',password='Abc$1234',host='t0.map.design')
cur_r = conn.cursor()
cur_r_write = conn.cursor()
cur_r_name = conn.cursor()
cur_r.execute("SELECT rheilongjiang.id,r_lname.route_id FROM rheilongjiang INNER JOIN r_lname ON r_lname.id=rheilongjiang.id;")
print(cur_r.rowcount)
for rec_r in cur_r:
    #print(rec_r)
    cur_r_name.execute("SELECT r_name.pathname , r_name.route_kind FROM r_name WHERE r_name.route_id=%s and r_name.language='1'and r_name.route_kind='0';",[rec_r[1],])
    for rec_r_name in cur_r_name:
        print(rec_r_name[0])
        #cur_r_write.execute("UPDATE rheilongjiang SET name_zh=%s where rheilongjiang.id=%s;",[rec_r_name[0],rec_r[0]])
conn.commit()
cur_r_name.close()
cur_r_write.close()
cur_r.close()

conn.close()