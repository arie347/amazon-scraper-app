# Local Setup Guide - Amazon Scraper

This guide will help you run the Amazon Product Scraper on your computer.

## Prerequisites

You need to have installed:
- **Python 3.9+** - [Download here](https://www.python.org/downloads/)
- **Google Chrome** - [Download here](https://www.google.com/chrome/)
- **Git** - [Download here](https://git-scm.com/downloads)

## Installation Steps

### 1. Download the Code

Open Terminal (Mac) or Command Prompt (Windows) and run:

```bash
git clone https://github.com/arie347/amazon-scraper-app.git
cd amazon-scraper-app
```

### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

**Note for Windows users:** Use `pip` instead of `pip3`

### 3. Install ChromeDriver

#### Mac:
```bash
brew install chromedriver
```

#### Windows:
1. Download ChromeDriver from: https://googlechromelabs.github.io/chrome-for-testing/
2. Extract the file
3. Add the folder to your PATH environment variable

#### Linux:
```bash
sudo apt-get install chromium-chromedriver
```

## Running the Application

### Start the Server

```bash
python3 -m uvicorn web_app:app --reload --port 8000
```

**Note for Windows users:** Use `python` instead of `python3`

### Access the Dashboard

Open your web browser and go to:
```
http://localhost:8000
```

You should see the Amazon Scraper dashboard!

## How to Use

1. **Upload Excel File**
   - Click "Choose File" and select your maintenance Excel file
   - The file should have ASINs in Column B and expected prices in Column C
   - Click "Upload"

2. **Start Scraping**
   - Click the "Rescrape" button next to your uploaded file
   - Watch the progress bar as it processes each product
   - This will take about 2-3 minutes per product

3. **Download Results**
   - When status shows "Completed", click the "Download" button
   - You'll get an updated Excel file with all the scraped data

## Troubleshooting

### "Command not found: python3"
- Try using `python` instead of `python3`
- Or install Python from python.org

### "ChromeDriver not found"
- Make sure Chrome is installed
- Follow the ChromeDriver installation steps above
- Restart your terminal after installation

### "Port 8000 already in use"
- Change the port number: `python3 -m uvicorn web_app:app --port 8001`
- Then access at `http://localhost:8001`

### Scraper is slow
- This is normal! Each product takes 2-3 seconds
- For 165 products, expect 8-10 minutes total
- You can reduce the delay in `web_app.py` if needed

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## Need Help?

Contact the person who shared this with you, or check the GitHub repository for updates.
