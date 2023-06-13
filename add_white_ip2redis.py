import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
target_key = 'ip_whitelist'

with open("acl-ips") as f:
    lines = f.readlines()
    for line in lines:
        ip = line.strip() 
        r.sadd(target_key, ip)
