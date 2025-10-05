# Quick Setup Script for Planopticon

Write-Host "🌌 Planopticon - Quick Setup Script" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

$projectRoot = "c:\Users\prath\OneDrive\Documents\NasaSpace\organized-project"

# Check if organized-project exists
if (!(Test-Path $projectRoot)) {
    Write-Host "❌ Error: organized-project folder not found!" -ForegroundColor Red
    Write-Host "Please make sure you're running this from the correct location." -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Project folder found" -ForegroundColor Green
Write-Host ""

# Setup Backend
Write-Host "🔧 Setting up Backend..." -ForegroundColor Yellow
Set-Location "$projectRoot\backend"

# Check if virtual environment exists
if (!(Test-Path "venv")) {
    Write-Host "Creating Python virtual environment..." -ForegroundColor Cyan
    python -m venv venv
    Write-Host "✅ Virtual environment created" -ForegroundColor Green
} else {
    Write-Host "✅ Virtual environment already exists" -ForegroundColor Green
}

Write-Host ""
Write-Host "Installing Python dependencies..." -ForegroundColor Cyan
& "$projectRoot\backend\venv\Scripts\python.exe" -m pip install --upgrade pip
& "$projectRoot\backend\venv\Scripts\pip.exe" install -r requirements.txt

Write-Host "✅ Backend setup complete!" -ForegroundColor Green
Write-Host ""

# Setup Frontend
Write-Host "🔧 Setting up Frontend..." -ForegroundColor Yellow
Set-Location "$projectRoot\frontend"

# Check if node_modules exists
if (!(Test-Path "node_modules")) {
    Write-Host "Installing npm dependencies (this may take a few minutes)..." -ForegroundColor Cyan
    npm install
    Write-Host "✅ npm dependencies installed" -ForegroundColor Green
} else {
    Write-Host "✅ node_modules already exists" -ForegroundColor Green
}

# Create .env.local if not exists
if (!(Test-Path ".env.local")) {
    Write-Host "Creating .env.local file..." -ForegroundColor Cyan
    Copy-Item ".env.example" ".env.local"
    Write-Host "✅ .env.local created (using default: http://localhost:5000)" -ForegroundColor Green
} else {
    Write-Host "✅ .env.local already exists" -ForegroundColor Green
}

Write-Host "✅ Frontend setup complete!" -ForegroundColor Green
Write-Host ""

# Final Instructions
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "🎉 Setup Complete!" -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "To start the application:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1️⃣  Start Backend (Terminal 1):" -ForegroundColor Cyan
Write-Host "   cd $projectRoot\backend" -ForegroundColor White
Write-Host "   .\venv\Scripts\activate" -ForegroundColor White
Write-Host "   python app.py" -ForegroundColor White
Write-Host ""
Write-Host "2️⃣  Start Frontend (Terminal 2):" -ForegroundColor Cyan
Write-Host "   cd $projectRoot\frontend" -ForegroundColor White
Write-Host "   npm run dev" -ForegroundColor White
Write-Host ""
Write-Host "3️⃣  Open browser:" -ForegroundColor Cyan
Write-Host "   http://localhost:5173" -ForegroundColor White
Write-Host ""
Write-Host "📚 Documentation:" -ForegroundColor Yellow
Write-Host "   - Main README: $projectRoot\README.md" -ForegroundColor White
Write-Host "   - Migration Guide: $projectRoot\MIGRATION_GUIDE.md" -ForegroundColor White
Write-Host ""
Write-Host "Happy exploring! 🚀" -ForegroundColor Green

Set-Location $projectRoot
