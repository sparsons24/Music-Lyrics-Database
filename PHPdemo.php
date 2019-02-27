<?php
   // A very simple example to demonstrate how to connect to a database and
   // retrieve information to integrate into a web page.  

   // There are two different web pages generated from this file, the first
   // populates a selection list of all the stock symbols in stockdata. 
   // The second retrieves data from the table selected and creates a table
   // from the metadata that is returned.

   session_start();

   // Set connection variables - should not be visible like this example
   $host     = 'localhost';
   $user     = 'Spa';
   $dbname   = 'Music';
   $password = 'lyrics';
   
   error_reporting(E_ALL);
   ini_set("display_errors", 1);
   ini_set("log_errors", 1);

   //********* Connect to the database or die **************//
   $connection = new mysqli($host, $user, $password, $dbname)
 		    or die ("Error: could not connect to host ". $host. " " .mysql_error());
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
 	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
 	<title>Exploring Music Lyrics Database</title>
        <style>
            table  {border: 5px solid powderblue;}
            th, td {padding: 15px;}
            th     {color: red; font: 20px arial, sans-serif;}
            h1     {color: black;}
            select {padding: 5px;}
            label{
        display:inline-block;
        width:75px;
        margin-right:30px;
        text-align:left;
        }

        input{

        }

        form{
        border:none;
        width:500px;
        margin:0px auto;
        }
}

        </style>
 </head>

 <body>
 <center>

 <?php	
   // determine if this is the first page or the refresh page				
        //*********Query  database******************//
        // Send query to MySQL and get the result
        $query = "SELECT DISTINCT Word FROM Word_Count natural join Words";
        $result = $connection->query( $query );

        // produce some HTML code
        echo "<h1 style='background-color:DodgerBlue; color:white;'>MUSIC LYRICS DATABASE</h1>";
  echo "<h2>Enter a word, artist, or track and click Submit to retrieve music data.</h2>";
  echo "<img src='Headphonepulse.gif' alt='Headphones' style='width:200px;height:200px;'>";
  echo " <br>";
  echo " <br>";
        // echo "    <fieldset>";
	echo "    <form action='word.php' method = 'post' >";
        echo "    <label for='Word'>Word: </label><input type = 'text' name = 'Word' size='20'>";
        echo "    <input type='submit' value='Submit'>";
        echo "    </form>";

        echo "    <form action='artist.php' method = 'post' >";
        echo "    <label for='Artist'>Artist: </label><input type = 'text' name = 'Artist' size='20'>";
        echo "    <input type='submit' value='Submit'>";
        echo "    </form>";

        echo "    <form action='track.php' method = 'post' >";
        echo "    <label for='Track'>Track Title: </label><input type = 'text' name = 'Track' size='20'>";
        echo "    <input type='submit' value='Submit'>";
        echo "    </form>";
        echo "    <br><br><br>Data provided by:<br>";
        echo " <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Musixmatch_horizontal_logo_on_white.svg/1280px-Musixmatch_horizontal_logo_on_white.svg.png' style='width:20%;height:20%;'";
        echo "<br><br>Developed by: Patrick Williams and Sarah Parsons";

?>
        
</center>
</BODY>
</HTML>

