Param(
    [switch]$OpenBrowser
)

$cwd = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
Set-Location $cwd

# locate python in venv if present
if (Test-Path "$cwd\\.venv\\Scripts\\python.exe") {
    $pythonExe = Join-Path $cwd '.venv\\Scripts\\python.exe'
} elseif (Test-Path "$cwd\\venv\\Scripts\\python.exe") {
    $pythonExe = Join-Path $cwd 'venv\\Scripts\\python.exe'
} else {
    $pythonExe = 'python'
}

Write-Output "Using Python executable: $pythonExe"

# Start backend
try {
    $backendProc = Start-Process -FilePath $pythonExe -ArgumentList 'backend\\app.py' -WorkingDirectory $cwd -WindowStyle Minimized -PassThru
    Write-Output "Started backend (PID $($backendProc.Id))."
} catch {
    Write-Output "Failed to start backend: $($_.Exception.Message)"
    exit 1
}

# Start frontend dev server
$frontendDir = Join-Path $cwd 'frontend_interface'
if (-not (Test-Path $frontendDir)) { Write-Output "frontend_interface not found at $frontendDir"; exit 1 }

# Prefer the npm Windows wrapper if present (npm.cmd) so Start-Process can run it directly
$npmExe = 'npm'
$possible = @('C:\Program Files\nodejs\npm.cmd', 'C:\Program Files\nodejs\npm.exe')
try {
    $cmd = Get-Command npm -ErrorAction SilentlyContinue
    if ($cmd -and $cmd.Source) { $possible += $cmd.Source }
} catch { }
foreach ($p in $possible) { if ($p -and (Test-Path $p)) { $npmExe = $p; break } }

try {
    $npmProc = Start-Process -FilePath $npmExe -ArgumentList 'start' -WorkingDirectory $frontendDir -PassThru
    Write-Output "Started frontend dev server (PID $($npmProc.Id)) using $npmExe."
} catch {
    Write-Output "Failed to start frontend dev server: $($_.Exception.Message)"
    exit 1
}

# Wait for the dev server to listen (3000 or 3001)
$timeout = 40
$listeningPort = $null
for ($i=0; $i -lt $timeout; $i++) {
    if ((Test-NetConnection -ComputerName 127.0.0.1 -Port 3000).TcpTestSucceeded) { $listeningPort = 3000; break }
    if ((Test-NetConnection -ComputerName 127.0.0.1 -Port 3001).TcpTestSucceeded) { $listeningPort = 3001; break }
    Start-Sleep -Seconds 1
}

if (-not $listeningPort) {
    Write-Output "Timed out waiting for frontend dev server to start. Check the terminal for npm output."
    exit 1
}

Write-Output "Frontend dev server listening on port $listeningPort"

if ($OpenBrowser) {
    Start-Process "http://127.0.0.1:$listeningPort"
    Write-Output "Opened browser at http://127.0.0.1:$listeningPort"
} else {
    Write-Output "Run: Start-Process 'http://127.0.0.1:$listeningPort' to open the site in your browser."
}

Write-Output 'start_dev.ps1 finished.'
