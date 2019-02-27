<?php
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
 	<title>Exploring Stock Price Database</title>
        <style>
            table  {border: 1px solid powderblue;}
            th, td {padding: 15px;}
            th     {color: red; font: 20px arial, sans-serif;}
            h1     {color: blue;}
            select {padding: 5px;}
        </style>
 </head>
<body>

<!-- Word:  <?php echo $_POST["Artist"]; ?><br> -->
<?php
    echo "<a class='click-me' href='http://45.36.146.185/~willpar/PHPdemo.php'>Go Back</a>";
    if ($query = $connection->prepare("SELECT Artist, Title, Word, Word_Count FROM Recordings natural join Word_Count natural join Words where Artist = ? ORDER BY ARTIST ASC")) {
        $query->bind_param("s", $_POST['Artist']);
                $query->execute();
                $result = $query->get_result();
                $query->close();
    }

            // Start HTML table and header row.
        echo "<table border=1> <tr>";
        
        // Make first row of HTML table using column names
            while( $field = $result->fetch_field() ){
            
        // Get field name and echo within header tags.
            echo "<th>". $field->name . "</th>";
            }
            
        // Fetch results row by row and create table entries
        while ( $row = mysqli_fetch_array($result) ){
                echo "<tr>";
            echo "<td>".$row['Artist']."</td>";
            echo "<td>".$row['Title']."</td>";
            echo "<td>".$row['Word']."</td>";
            echo "<td>".$row['Word_Count']."</td>";
                echo "</tr>";	
        }
            echo "</table>";

            // add a Back button
        // $_POST['page2'] = 'false';  // reset variable so Back button works right
        //     echo "<br><br>";
        //     echo "<form method = 'post'>";
        //     echo "   <button type = 'submit' >Go Back</button>";
        // echo "</body>";
        echo "<a class='click-me' href='http://45.36.146.185/~willpar/PHPdemo.php'>Go Back</a>";
?>
</body>
</html>