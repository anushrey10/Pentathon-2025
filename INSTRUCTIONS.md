# QUAGMIRE CHALLENGE - HOW TO GET THE FLAG

## THE ISSUE
The flag is NOT the movement sequence itself. This is why submitting "flag{ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw}" was rejected.

Instead, the binary outputs "You're out, here's your flag:" followed by the actual flag when you successfully navigate the maze.

## SOLUTION USING REPLIT (Easiest Method)

[Replit](https://replit.com/) provides a free Linux environment in your browser.

### Step 1: Create a Replit Account
1. Go to [replit.com](https://replit.com/) and sign up for a free account
2. Verify your email if required

### Step 2: Create a New Repl
1. Click on the "+ Create Repl" button
2. Select "Bash" as the language
3. Give your Repl a name (e.g., "quagmire-challenge")
4. Click "Create Repl"

### Step 3: Upload Files
1. Upload the `glade` binary file from your computer
2. Upload the `replit_solver.py` script (we've created this to automatically test solutions)

### Step 4: Run the Solver Script
1. In the Replit terminal, make both files executable:
   ```
   chmod +x glade replit_solver.py
   ```
2. Run the solver script:
   ```
   python3 replit_solver.py
   ```
3. The script will automatically try all our solution candidates and display the flag if found

### Step 5: Submit the Flag
- Copy the complete flag (including the flag{...} format)
- Submit it to the challenge platform

## ALTERNATIVE: MANUAL TESTING

If you prefer to manually test the solutions:

1. Make the binary executable in Replit:
   ```
   chmod +x glade
   ```
2. Run the binary:
   ```
   ./glade
   ```
3. When prompted, enter one of these movement sequences:
   - `ddwdwwawwddssdwawwssaawwddssdwawwssaawwddssdwaw`
   - `dwawdwawdwawdwawdwawdwawdwawdwaw`
   - `ddssaawwddssaawwddssaaww`

## OTHER LINUX OPTIONS

If you prefer not to use Replit, here are other ways to run the Linux binary:

### 1. Using Docker (if installed)
```bash
docker run -it --rm -v $(pwd):/work ubuntu:latest bash
cd /work
chmod +x glade
./glade
```
Then enter the movement sequence.

### 2. Using a Virtual Machine
- Install VirtualBox or UTM
- Set up a Linux VM (Ubuntu recommended)
- Transfer the glade file and run it inside the VM

### 3. Using WSL (Windows Subsystem for Linux)
If you're on Windows:
1. Enable WSL and install Ubuntu
2. Transfer the glade file to your Ubuntu environment
3. Run it there

## TROUBLESHOOTING

- **Binary doesn't run?** Make sure you've made it executable with `chmod +x glade`
- **No flag appears?** Try different movement sequences from our list
- **Replit has issues?** Try copying the file to the /tmp directory and running it from there:
  ```
  cp glade /tmp
  cd /tmp
  chmod +x glade
  ./glade
  ```

Remember: The flag is revealed by the program when you successfully complete the maze - not derived from the sequence itself. 