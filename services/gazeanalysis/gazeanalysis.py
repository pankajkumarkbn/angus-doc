# -*- coding: utf-8 -*-
import angus
from pprint import pprint

conn = angus.connect()
service = conn.services.get_service('gaze_analysis', version=1)
job = service.process({'image': open('./macgyver.jpg', 'rb')})

pprint(job.result)
