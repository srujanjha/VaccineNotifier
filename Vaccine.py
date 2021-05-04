import requests
import datetime
import time
token="telagram_bot_token"
chat_id="telegram_chat_id"
# https://api.telegram.org/bottelagram_bot_token/getUpdates
for i in range(100):
    dts = datetime.datetime.now()
    district_keys=[] # Add the district_ids, you are interested in
    log=[]
    message=""
    url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='
    if i % 5==0:
        print("COWIN")
        url='https://cowin.gov.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='
    else:
        print("CDN")
    for dt in [dts.strftime("%d-%m-%Y"),(dts+datetime.timedelta(days=7)).strftime("%d-%m-%Y"),(dts+datetime.timedelta(days=14)).strftime("%d-%m-%Y")]:
        for dis in district_keys:
            try:
                x = requests.get(url+str(dis)+'&date='+dt)
                if x.status_code == 200:
                    res=x.json()
                    for center in res['centers']:
                        for slot in center['sessions']:
                            if slot['available_capacity']>0 and slot['min_age_limit']<45:
                                print(slot['available_capacity'],slot['date'],center['name'],center['district_name'],center['pincode'])
                                message+="("+str(slot['available_capacity'])+") "+slot['date']+","+slot['vaccine']+","+center['name']+","+center['district_name']+","+str(center['pincode'])+"\n"
                                log.append(center)
            except:
                print("connectionReset")
    # Uncomment below lines for Telegram Bot
    # if message!='':
    #     requests.post("https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="+message)
    print(i)
    time.sleep(60*5) # 5 minutes sleep
