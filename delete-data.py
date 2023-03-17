
from utils import db_conn

sql1 = "delete i.* from mb_member_info i inner join mb_member m on i.member_id = m.id where m.phone in ('13124523341','13124523342','13124523344','13124523345','13124523346','13124523347');"
db_conn.delete_sql(db_name='czbk_member', sql=sql1)
sql2 = "delete l.* from mb_member_login_log l inner join mb_member m on l.member_id = m.id where m.phone in ('13124523341','13124523342','13124523344','13124523345','13124523346','13124523347');"
db_conn.delete_sql(db_name='czbk_member', sql=sql2)
sql3 = "delete from mb_member_register_log where phone in ('13124523341','13124523342','13124523344','13124523345','13124523346','13124523347');"
db_conn.delete_sql(db_name='czbk_member', sql=sql3)
sql4 = "delete from mb_member where phone in ('13124523341','13124523342','13124523344','13124523345','13124523346','13124523347');"
db_conn.delete_sql(db_name='czbk_member', sql=sql4)

