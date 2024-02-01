#!/usr/bin/env ruby
echo "$1" | grep -o 'hbt*n' | tr -d '\n'
