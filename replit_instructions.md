# Running the Linux Binary Using Replit

Replit.com offers a free Linux environment in your browser without needing to install anything. Here's how to use it to run the `glade` binary:

## Step 1: Create a Replit Account

1. Go to [replit.com](https://replit.com/) and sign up for a free account
2. Verify your email if required

## Step 2: Create a New Repl

1. Click on the "+ Create Repl" button
2. Select "Bash" as the language
3. Give your Repl a name (e.g., "quagmire-challenge")
4. Click "Create Repl"

## Step 3: Upload the Binary

1. In your new Repl, locate the "Files" panel on the left side
2. Click on the three dots (...) and select "Upload file"
3. Upload the `glade` file from your computer

## Step 4: Run the Binary

1. In the Replit terminal (shell), make the binary executable:
   ```
   chmod +x glade
   ```

2. Run the binary:
   ```
   ./glade
   ```

3. When prompted, enter one of these movement sequences:
   ```
   ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw
   ```
   or
   ```
   dwawdwawdwawdwawdwawdwawdwawdwaw
   ```
   or
   ```
   ddssaawwddssaawwddssaaww
   ```

4. If the sequence is correct, you should see: "You're out, here's your flag: [THE_ACTUAL_FLAG]"

5. Copy the complete flag (including the flag{...} format) and submit it to the challenge platform

## Alternative: Try Our Automated Sequence Testing

You can also upload and run our automated solution tester script:

1. Upload the `run_all_solutions.py` file to Replit
2. Make it executable:
   ```
   chmod +x run_all_solutions.py
   ```
3. Run it:
   ```
   python3 run_all_solutions.py
   ```
   
This script will automatically try all the potential solutions and tell you if it finds the flag.

## Troubleshooting

- If you get a "Permission denied" error, make sure you ran the `chmod +x glade` command
- If you get a "Command not found" error, make sure you're using `./glade` to run the file
- If the binary doesn't work, try copying `glade` to the `/tmp` directory and running it from there:
  ```
  cp glade /tmp
  cd /tmp
  chmod +x glade
  ./glade
  ``` 