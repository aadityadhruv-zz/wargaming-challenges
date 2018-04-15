#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Any even integer with a digit sum = 16
# Must be run with the environment variable `LOL`
echo 970 | env LOL=1 $DIR/crackme0x07
