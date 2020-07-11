#!/bin/zsh

# installing the requirements
pip install -r requirements.txt

# resetting the screen
# clear

echo "\n\n\nWelcome the the Falpi Birb Game!"
echo "Main Menu: "
echo "\t1. Play Yourself"
echo "\t2. See NEAT in action"
echo "\t0. Exit"

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

