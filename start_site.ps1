Param(
    [switch]$OpenBrowser
)

$cwd = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
Set-Location $cwd

# Prefer virtualenv python if present
if (Test-Path "$cwd\\.venv\\Scripts\\python.exe") {
    $pythonExe = Join-Path $cwd '.venv\\Scripts\\python.exe'
} elseif (Test-Path "$cwd\\venv\\Scripts\\python.exe") {
    $pythonExe = Join-Path $cwd 'venv\\Scripts\\python.exe'
} else {
    $pythonExe = 'python'
}

Write-Output "Using Python executable: $pythonExe"

# Start backend in background
try {
    $proc = Start-Process -FilePath $pythonExe -ArgumentList 'backend\\app.py' -WorkingDirectory $cwd -WindowStyle Hidden -PassThru
    Write-Output "Started backend (PID $($proc.Id))."
} catch {
    Write-Output "Failed to start backend: $($_.Exception.Message)"
    exit 1
}

# Wait for the server to listen on port 5000 (timeout after 30s)
$timeout = 30
$listening = $false
for ($i = 0; $i -lt $timeout; $i++) {
    $res = Test-NetConnection -ComputerName 127.0.0.1 -Port 5000
    if ($res.TcpTestSucceeded) { $listening = $true; break }
    Start-Sleep -Seconds 1
}

if (-not $listening) {
    Write-Output "Timed out waiting for backend to listen on port 5000. Check logs or run 'python backend\\app.py' manually.";
    exit 1
}

Write-Output "Backend is listening on http://127.0.0.1:5000"

if ($OpenBrowser) {
    Start-Process 'http://127.0.0.1:5000'
    Write-Output 'Opened default browser to http://127.0.0.1:5000'
} else {
    Write-Output "Run: Start-Process 'http://127.0.0.1:5000' to open the site in your browser."
}

Write-Output 'start_site.ps1 finished.'
