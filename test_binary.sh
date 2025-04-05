#!/bin/bash

# Simple script to test the glade binary

echo "=== TESTING GLADE BINARY ==="

# Check if file exists
if [ ! -f ./glade ]; then
    echo "ERROR: glade binary not found!"
    exit 1
fi

# Make it executable
chmod +x ./glade

# Check file type
echo -e "\nFile type:"
file ./glade

# Check architecture
echo -e "\nSystem architecture:"
uname -a

# Try running directly with simple input
echo -e "\nTrying to run with simple input..."
echo "w" | ./glade

# Try running with solution
echo -e "\nTrying solution..."
echo "ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw" | ./glade

# Try copying to /tmp
echo -e "\nTrying from /tmp directory..."
cp glade /tmp/
chmod +x /tmp/glade
cd /tmp
echo "wasd" | ./glade
cd - > /dev/null

# Try with gdb if available
if command -v gdb &> /dev/null; then
    echo -e "\nTrying with gdb..."
    echo "r" | gdb -q ./glade
else
    echo -e "\ngdb not available"
fi

echo -e "\nTest complete. If you didn't see any output from the binary,"
echo "it may not work in this environment. Consider trying Docker or a VM." 