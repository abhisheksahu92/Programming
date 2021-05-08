# Here is a line from a web server access log:
#
# 127.0.0.1 - [10/Oct/2000:13:30:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# 127.0.0.1 - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# 127.0.0.1 - [10/Oct/2000:14:05:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# 127.0.0.1 - [10/Oct/2000:15:05:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# Assume you are given a access log file with many such lines. You need to analyze two things:
# 1 - What is the percentage distribution of the various Status Codes (200 in the above line) in the whole file?
# For example "200 - 80%, 400 - 15%, 403 - 5%"
# 2 - Analyze the "Number of requests in an hour" metric. Print the max requests seen in any hour, min requests seen in any hour,
# and the average requests seen per hour. For example "Max : 9348 requests in an hour, Min: 20 requests in an hour, Avg: 453 requests per hour"
#
# Write the python code for these 2 data analysis problems

log_file = 'response.log'
# 127.0.0.1 - [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326
# GET /apache_pb.gif HTTP/1.0" 200 2326
# GET /apache_pb.gif HTTP/1.0" 400 2326
# GET /apache_pb.gif HTTP/1.0" 403 2326

start_time = None
with open(log_file,'r') as f:
    for line in f.readline():
        extracted_date = re.findall(r'[0-9]{1,2}/[a-zA-Z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}',line)
        if start_time is None:
            start_time = pd.todatetime(extracted_date)
        start_time\
            .minute = '00'
        end_time = start_time + pd.timedelta(hrs=1)
        if extracted_date.between(start_time,end_time):
            count += 1
        else:
            start_time = end_time
            end_time = start_time + pd.timedelta(hrs=1)

# import re
# import pandas as pd
# list_of_request_for_hr = []
# list_of_times = []
# with open(log_file,'r') as f:
#     for line in f.readline():
#         list_of_times.append(re.findall(r'[0-9]{1,2}/[a-zA-Z]{3}/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}',line))
#     times = list(map(lambda x: pd.todatetime(x),list_of_times))
# mini_time = min(times)
# mini_time.minute = '00'
# mext_time = mini_time + pd.timedelta(hrs=1)
# max_time = max(times)
# while mext_time < max_time:
#     list_of_request_for_hr.append(len(list(map(lambda x: x.between(mini_time,mext_time)))))
#     mext_time = mext_time + pd.timedelta(hrs=1)
# min(list_of_request_for_hr) # mini
# max(list_of_request_for_hr) # maxi




#
# status = {}
# total_response = 0
# with open(log_file,'r') as f:
#     for x in f.readlines():
#         statuscode = x.split(' ')[-2]
#         status[statuscode] = status.get(statuscode,0) + 1
#         total_response += 1
#
# for x in status:
#     print(f'Percentage distribution for {x} is status[x] // total_response')



