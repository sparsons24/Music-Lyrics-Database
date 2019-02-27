import urllib.request
import json
import datetime
import mysql.connector
from mysql.connector import errorcode

# f = urllib.request.urlopen('http://api.wunderground.com/api/Your_Key/geolookup/conditions/q/GA/Atlanta.json')
# json_string = f.read()
# parsed_json = json.loads(json_string)
# location = parsed_json['location']['city']
# temp_f = parsed_json['current_observation']['temp_f']
# print("Current temperature in %s is: %s" % (location, temp_f))
# print("Current temperature is: %s" % parsed_json)
# f.close()
'''
stock = input("""Please specify a stock symbol: """)
f = urllib.request.urlopen('https://api.iextrading.com/1.0/stock/' + stock + '/chart')
json_string = f.read()
parsed_json = json.loads(json_string)
length = len(parsed_json)
i=0
now = datetime.datetime.now()

while i<length:
#message['date']<=now.strftime("%Y-%m-%d"):
    message=parsed_json[i]
    date = message['date']
    close = message['close']
    print(str(length) + """ The date of the stock price of %s""" % stock + """ is %s""" % date + """ and the closing price was $%s""" % close + """.""")
    i=i+1
'''


def doQuery(connection):

    word = input("""Please specify a word: """)

    cursor = connection.cursor(buffered = True)

# query = """insert into stockdata(symbol,date,closing) values('%s','%s','%s')""" % (stock,date,close)
    cursor.execute("select Title, Artist from Recordings natural join Words natural join Word_Count where Words.Word = '%s'" % (word))
    #connection.commit()
    count = cursor.rowcount
    if count == 0:
        print("There are no songs with the word, """ + word + """, in the database.""")
    else:
        print("""The following, """ + str(count) + """ songs have at least one instance of the word, """ + word + """, in the lyrics:""")
        print("{0:100} {1:50}".format("Title", "Artist"))
        print("-" * 150)
        i = 0
        for(Title, Artist) in cursor:
            print("{0:100} {1:50}".format(Title, Artist))
            i = i+1

    
    cursor.close()


try:
    connection = mysql.connector.connect(host='45.36.146.185', user='Spa', password='lyrics', database='Music')
    doQuery(connection)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: probably in user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    connection.close()