#!/bin/sh

FIRST="Today, $(date | cut -f 1,2,3 -d ' '), is your birthday!"
SECOND="As your birthday gift please accept this heartfelt automated message to you, $1"

osascript -e " tell application \"Messages\" to send \" Today is the birthday of $1 \" to buddy \"Jack Fox\" "

sleep 20

SENT=" tell application \"Messages\" to send \" $FIRST \" to buddy \"$1\" "
osascript -e "$SENT"
SENT=" tell application \"Messages\" to send \" $SECOND \" to buddy \"$1\" "
osascript -e "$SENT"

exit 0