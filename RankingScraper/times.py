import urllib, json

timesTableUrl = "https://www.timeshighereducation.com/sites//default//files//the_data_rankings//united_states_rankings_2017_limit0_068d27a033ada75528617769a8a4c4c2.json"
response = urllib.urlopen(timesTableUrl)
jsonData = json.loads(response.read())
with open("times.json", "w") as timesJson:
    timesJson.write("[\n")
    for n in range(0, 200):
        collegeInfo = jsonData["data"]
        uniName = collegeInfo[n]["name"]
        uniRank = collegeInfo[n]["rank"]
        json.dump({"name": uniName, "rank": uniRank}, timesJson)
        timesJson.write("\n")
    timesJson.write("]")