<font face="courier">
    <?
        $myfilename = "instructions2.txt";
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
            $totalsteps = 1;
            foreach ( $instructions as $i ) {
                $dir = $i[0];
                $steps = (int)substr($i, 1);
                for ( $i = 0 ; $i < $steps ; $i++, $totalsteps++ ) {
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
                    $key = "$x" . "-" . "$y";
                    if ( ! array_key_exists($key, $wire) ) {
                        $wire["$x" . "-" . "$y"] = $totalsteps;
                    }
                }
            }
            if ( sizeof($wire1) == 0 ) {
                $wire1 = $wire;
            } else {
                $wire2 = $wire;
            }
        }

        $shortest = FALSE;

        foreach ( $wire1 as $coord => $v1 ) {
            if ( array_key_exists($coord, $wire2) ) {
                $steps = $wire1[$coord] + $wire2[$coord];
                if ( !$shortest ) {
                    $shortest = $steps;
                } elseif ( $steps < $shortest ) {
                    $shortest = $steps;
                }
            }
        }

        echo $shortest;
    ?>
</font>