#!/bin/zsh

# resetting the screen
clear

echo "                          .   .       "
echo "                          | \/|       "
echo "  (\   _                  ) )|/|      "
echo "      (/            _----. /.'.'      "
echo ".-._________..      .' @ _\  .'              Welcome to..."
echo "'.._______.   '.   /    (_| .')       the one and only,"
echo "  '._____.  /   '-/      | _.'                the legendary,"
echo "   '.______ (         ) ) \           "
echo "     '..____ '._       )  )           "
echo "        .' __.--\  , ,  // ((         "
echo "        '.'     |  \/   (_.'(         Flapi Birb Game!"
echo "                '   \ .'              "
echo "                 \   (                "
echo "                  \   '.              "
echo "  Author: Tanishq  \ \ '.)            "
echo "     Chaudhary      '-'-'             "


echo "\n\nMain Menu: "
echo "\t001. Play Yourself"
echo "\t002. See NEAT in action"
echo "\tany. Exit"

while [ true ]
do
    echo -n "\n\nEnter Your Choice: "
    read input

    if [[ $input == '1' ]]
    then
        python Game/play.py
    elif [[ $input == '2' ]]
    then
        python Game/NEATplay.py
    else
        break
    fi
done

