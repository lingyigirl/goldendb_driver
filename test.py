# -*- coding: utf-8 -*-
from pymysql import loadbalance



user = 'dbproxy'
passwd = 'db10$ZTE'
#db = 'test'
charset = 'utf8'

# conn = pymysql.connect(host = '10.229.32.235', port = 6606, user = user, passwd = passwd, charset = charset)
# print("ip:{} port:{}连接成功".format('10.229.32.235',6606))
# cursor = conn.cursor()

# conn.close()



#loadbalance_group = "10.229.31.134:8880,10.229.31.134:8881"
loadbalance_group = "10.229.31.202:8880,10.229.31.202:8881"
# loadbalance = "10.229.32.235:6606"
for i in range(0,1):
    # print("测试deloadbalance")
    # ip_port_list = loadbalance.deloadbalance(loadbalance_group,ip_port_blacklist)
    # print("不在黑名单中的ip,port:"+str(ip_port_list))
    
    print("测试randomcon")
    conn,ip_port_blacklist = loadbalance.randomcon(loadbalance_group , user, passwd, charset)
    print("连接是否成功:{} 黑名单的ip,port:{}".format(conn,ip_port_blacklist))
    
    
    # print("测试blacklistcon")
    # e = loadbalance.blacklistcon(ip_port_blacklist, user, passwd, charset)
    # print("黑名单中连接失败的ip:{} port:{}"+str(e))
