# Music-Lyrics-Database

  For my CSC 621 final project, my partner and I worked to create a database application for analysis of music lyrics. We have included data for all genres of music, including artist, song title, and lyric information from the musiXmatch dataset. In addition, we have included data for the count of a word in all songs, as well as in each individual song. The purpose of this database application is to provide information to musicians and music gurus, alike, and encourage the analysis of music lyrics based on the frequency and inclusion of the top 5,000 words determined by the musiXmatch team. See here for more information on our datasets from musiXmatch and the Million Song Dataset.
  Given the large volume of data (almost 1 million tracks, approximately 80,000 words, and 5,000 tracks with word counts for lyrics in the top 5000 words), it is imperative that a database be created to store information for each primary key – track, word, and track-word count. We expect music gurus, music analysts, and the “average Joe” to enjoy exploring our database to observe trends and outliers within our set of lyrics. Users can access our database by visiting our webpage, where they can enter an artist, track, or word to find more information about the lyrics of a song. 
  As a disclaimer, we would like to emphasize that there are inaccuracies in the original dataset and that there may exist duplicate track and artist pairs in the original dataset. We did not alter the data but would like to acknowledge these discrepancies. It is also important to note that the lyrics provided by musiXmatch are in bag-of-word format due to copyright restrictions on the original lyrics. Additionally, stemming of the words (combining words that have the same root) was used to improve the accuracy of statistical analysis performed on the dataset. 
  One example of an interesting figure that an analyst could research with the data that we provide is the term frequency-inverse document frequency (tf-idf) value of a word. The tf-idf provides a more accurate depiction of the topic of the song by weighting the significance of each word by its relevance rather than frequency in the dataset. For instance, the word “I” is the most popular word in our dataset; consequently, its significance is trivial given that it is so popular amongst all songs. A word that is not very popular in the dataset, such as “meadow” (#4824), would be significant if it appears multiple times in a song. Calculating this value for each song in our database is a future goal that we plan to implement. Moreover, we would also like to improve our database by incorporating data regarding the genre and time of a track’s release, and update the table with more recent tracks. 
  To create our database,  we designed three entity relations with primary/foreign keys from the datasets provided by musiXmatch. We have also identified the functional dependencies of each relation and verified that our relation schemas are in Boyce-Codd normal form. As illustrated below, we constructed an E-R diagram with these three relation schemas and used this diagram as a basis for creating our tables in our Music database in MySQL Workbench. 


Datasets:

1.	Recordings by Title and Artist
2.	List of 5000 Most Common Words
3.	Count of Words per Song

Relation Schemas:

1.	recordings(trackID, title, artist)
2.	word_count(trackID, wordID, wordcount)
3.	words(wordID, totalwordcount)

Functional Dependencies:

•	trackID -> title, artist
•	trackID, wordID -> wordcount
•	wordID -> totalwordcount

  Furthermore, we loaded our Words table into MySQL with a similar query. For our Word_Count table, due to the way in which the “word: count” ratio was stored in the original dataset, we extracted the word and count of the “word: count” ratio in Python and assigned these entities to variables to use in our SQL query. See below for a screenshot of our code. Our database contains 5,000 Tracks with Word: Word_Count ratios; 711,443 unique Tracks with Artists; and 79,874 Words with Total_Word_Counts. 
 Sample Python and SQL to extract the word and word-count, and to create the Word_Count table in our Music database
	Finally, for our user interface, we chose to build a web page using PHP, HTML, and SQL queries by storing an artist, track, and word.php file on a web server. After connecting to our Music database using PHP, we formatted our website with HTML code and embedded SQL queries in PHP code to retrieve data from our database (see below for sample code). Our web page consists of a home page with three text boxes in which a user can type an Artist, Track, or Word to search for lyric information. Upon submitting one of these three items, a second page will load displaying a table of song titles with the artist, each word included in its lyrics (of the top 5000 words), and each word’s respective word count in the song. One important safeguard that we took to protect our database was to use prepared statements in our SQL queries to prevent SQL injections. See below for a sample of our HTML and our prepared statements used in the artist.php file. Additionally, we chose to include a gif and a logo on our web page, for decorative purposes. 
  All in all, we successfully designed, constructed, and queried our very own database of music lyrics, and created a web-based interface for public consumption. Despite the challenges posed by the volume of data, special characters composing the lyrics, and the complexities of learning PHP, the project was a valuable experience – one that allowed us to expand our coding skills and gain real-world experience building databases and web pages. We aim to expand our web page and to design additional queries to allow for more advanced analysis on our music database.
 
Works Cited
“Bag of Words & TF-IDF.” Skymind, Skymind Inc., skymind.ai/wiki/bagofwords-tf-idf.
Bertin-Mahieux, Thierry, et al. “The MusiXmatch Dataset.” Million Song Dataset | Scaling MIR Research, 2011, labrosa.ee.columbia.edu/millionsong/musixmatch.
Unknown. “Music Beat GIF - Music Beat Beats - Discover & Share GIFs.” Tenor, Tenor, 23 Dec. 2016, tenor.com/view/music-beat-beats-gif-7412752.

