import urllib3
import xmltodict

#creates pool manager
http = urllib3.PoolManager()

#requests to GET data
xml = http.request("GET", "http://talks.cam.ac.uk/show/xml/39636")
#dept of earth sci seminars     http://talks.cam.ac.uk/show/xml/15125

#parses xml to python dictionary
#takes the "talk" subset, which is now a list of dictionaries (one dict per talk)
talks = xmltodict.parse(xml.data)["list"]["talk"]

#number of talks scheduled
num_talks = len(talks)

foo = []

for i in talks:
    foo.append(i["start_time"])

print(foo)
