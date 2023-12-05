import frappe
import redis
import random

frappe.utils.logger.set_log_level("DEBUG")
logger = frappe.logger("api11111", allow_site=True, file_count=50)

@frappe.whitelist()
def ping():
    STREAM_KEY = "jobs"

    JOB_TYPES = [
      "cleaning",
      "room_service",
      "taxi",
      "extra_towels",
      "extra_pillows"
    ]

    job = {
        "room": random.randint(100, 500),
        "job": random.choice(JOB_TYPES)
    }

    r = redis.Redis(decode_responses=True)
    job_id = r.xadd(STREAM_KEY, job)
    
    print(f"Created job {job_id}:")
    return 'pong from vendor'

@frappe.whitelist()
def create_om(**kwargs):
    del kwargs['cmd']
    print(kwargs['mobile_number'])
    print(kwargs['pack_name'])
    print(kwargs['channel'])
    print(kwargs)
    logger.info("Log from api................")
    job=frappe._dict(kwargs)
    r = redis.Redis(decode_responses=True)
    job_id = r.xadd("OM", job)
    print(f"Created OM job {job_id}:")
    json_data = {
        "message": "success",
         
           "data": {"a":6, "b":8}  
         
        }
    return json_data