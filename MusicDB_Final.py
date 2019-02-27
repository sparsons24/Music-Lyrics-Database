#import MySQLdb
import csv
import mysql.connector
#import pandas as pd
#from mysql.connector import errorcode


def main():
    conn = mysql.connector.connect(host='45.36.146.185', user='Spa', passwd='lyrics', db='Music')
    c = conn.cursor()

    with open('Word_Count_Practice.csv', encoding = 'utf-8-sig') as csvfile:
        dict = csv.DictReader(csvfile)
        for row in dict:
            track_id = row['Track_ID']
            track_word_count_list = row['Track_Word_Count'].split(',')
            for pair in track_word_count_list:
                split = pair.split(':')
                word_id = split[0];
                word_count = split[1];
               # print("Track ID: {}  Word ID: {}  Count: {}".format(track_ID, word_id, word_count))

                try:
                    c.execute(
                        'CREATE TABLE IF NOT EXISTS Word_Count(Track_ID varchar(25), Word_ID numeric(10), Word_Count numeric(65), primary key(Track_ID, Word_ID))')
                except mysql.connector.IntegrityError:
                    pass

                try:
                    c.execute("INSERT INTO Word_Count(Track_ID, Word_ID, Word_Count) VALUES(%s, %s, %s)",
                              [track_id, word_id, word_count])
                except mysql.connector.IntegrityError:
                    pass

        conn.commit()
        conn.close()

'''    with open('Recordings_2.csv', encoding='utf-8-sig') as csvfile:
        dict = csv.DictReader(csvfile)
        for row in dict:
                track_id = row["Track_ID"]
                artist = row["Artist"]
                title = row["Title"]

                try:
                    c.execute('CREATE TABLE IF NOT EXISTS Recordings(Track_ID varchar(25) primary key, Artist varchar(250) character set utf8mb4, Title varchar(800) character set utf8mb4)')
                except mysql.connector.IntegrityError:
                    pass

                try:
                    c.execute("INSERT INTO Recordings(Track_ID, Artist, Title) VALUES(%s, %s, %s)",
                              [row["Track_ID"], row["Artist"], row["Title"]])
                except mysql.connector.IntegrityError:
                    pass
    conn.commit()
    conn.close() 
'''

'''   with open('Words.csv', encoding='utf-8-sig') as csvfile:
        dict = csv.DictReader(csvfile)
        for row in dict:

            # print(row)

            word_id = row["Word_ID"]
            word = row["Word"]
            total_word_count = row["Total_Word_Count"]

            try:
                c.execute('CREATE TABLE IF NOT EXISTS Words(Word_ID numeric(7) primary key, Word varchar(50), Total_Word_Count numeric(10)) character set = utf8')
            except mysql.connector.IntegrityError:
                pass
            try:
                c.execute('ALTER TABLE Words modify Word varchar(50), character set = utf8mb4')
            except mysql.connector.IntegrityError:
                pass
            try:
                c.execute("INSERT INTO Words(Word_ID, Word, Total_Word_Count) VALUES( '%s', '%s', '%s')" %
                          (word_id, word, total_word_count))
            except mysql.connector.IntegrityError:
                pass

    conn.commit()
    conn.close()
'''

'''
#------------------------Patrick's old code------------------------
            try:
                c.execute('INSERT INTO Review (review_id, score_phrase, title, url, score, editors_choice, platform) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                          [row['review_id'], row['score_phrase'], row['title'], row['url'], score, editors_choice, row['platform']])
            except MySQLdb.IntegrityError:
                pass
            try:
                c.execute('INSERT INTO ReleaseDate (title, platform, release_year, release_month, release_day) VALUES (%s, %s, %s, %s, %s)',
                          [row['title'], row['platform'], int(row['release_year']), int(row['release_month']), int(row['release_day'])])
            except MySQLdb.IntegrityError:
                pass 

genre_list = row['genre'].split(', ')
            title = row['title']
            score = row['score']
            if len(score) == 1 or len(score) == 2:
                score += '.0'
            if row['editors_choice'] == 'Y':
                editors_choice = True
            else:
                editors_choice = False 
'''


if __name__ == '__main__':
    main()
