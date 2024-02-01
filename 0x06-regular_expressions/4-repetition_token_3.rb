#!/usr/bin/env bash
echo "$1" | grep -o 'hbt*n' | tr -d '\n'
