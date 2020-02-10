<font face="courier">
<?
    $myfilename = "instructions1.txt";
    if(file_exists($myfilename)){
      echo nl2br(file_get_contents($myfilename));
    }
    echo "<p>";

    $file = fopen("input.txt", 'r') or exit("Unable to open file!");

    $wire1 = [];
    $wire2 = [];

    while ( !feof($file) ) {
        $line = fgets($file);
        $instructions = explode(",", $line);
        $x = 0;
        $y = 0;
        $wire = [];
        foreach ( $instructions as $i ) {
            $dir = $i[0];
            $steps = (int)substr($i, 1);
            for ( $i = 0 ; $i < $steps ; $i++ ) {
                switch ($dir) {
                    case "R":
                        $x++;
                        break;
                    case "L":
                        $x--;
                        break;
                    case "U":
                        $y++;
                        break;
                    case "D":
                        $y--;
                        break;
                }
                $wire["$x" . "-" . "$y"] = TRUE;
            }
        }
        if ( sizeof($wire1) == 0 ) {
            $wire1 = $wire;
        } else {
            $wire2 = $wire;
        }
    }

    $shortest = FALSE;

    foreach ( $wire1 as $coord1 => $v1 ) {
        if ( array_key_exists($coord1, $wire2) ) {
            list( $x, $y ) = explode("-", $coord1);
            $distance = (int)$x + (int)$y;
            if ( !$shortest ) {
                $shortest = $distance;
            } elseif ( $distance < $shortest ) {
                $shortest = $distance;
            }
        }
    }

    echo $shortest;
?>
</font>