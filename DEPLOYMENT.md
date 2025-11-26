# Deployment Guide - Amazon Scraper to Render

## Prerequisites
- GitHub account (free)
- Render account (free tier available)

## Step 1: Create a GitHub Repository

1. Go to https://github.com and sign in
2. Click the "+" icon in the top right → "New repository"
3. Name it: `amazon-scraper-app`
4. Set to **Public** (required for Render free tier)
5. Click "Create repository"

## Step 2: Push Your Code to GitHub

Open Terminal and run these commands in your project folder:

```bash
cd /Users/leibykoplowitz/.gemini/antigravity/playground/fiery-plasma

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Amazon scraper web app"

# Connect to your GitHub repo (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/amazon-scraper-app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Create a Render Account

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with your GitHub account (easiest option)
4. Verify your email

## Step 4: Deploy to Render

1. In Render dashboard, click "New +" → "Web Service"
2. Click "Connect account" to link your GitHub
3. Find and select your `amazon-scraper-app` repository
4. Configure the service:
   - **Name**: `amazon-scraper` (or any name you prefer)
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Runtime**: `Docker`
   - **Instance Type**: Select **Free** (or paid if you need faster performance)
5. Click "Create Web Service"

## Step 5: Wait for Deployment

- Render will automatically:
  - Detect your Dockerfile
  - Build the Docker image (installs Chrome, Python, dependencies)
  - Deploy the application
- This takes 5-10 minutes for the first deployment
- You'll see build logs in real-time

## Step 6: Access Your App

Once deployed, Render gives you a URL like:
```
https://amazon-scraper-XXXXX.onrender.com
```

You can now access your scraper from anywhere!

## Important Notes

### Free Tier Limitations
- **Spins down after 15 minutes of inactivity**
  - First request after inactivity takes ~30 seconds to wake up
  - Subsequent requests are fast
- **750 hours/month free** (enough for personal use)

### Upgrade to Paid ($7/month) for:
- Always-on service (no spin-down)
- Faster performance
- More memory

### Data Persistence
⚠️ **Important**: The free tier uses ephemeral storage, meaning:
- Uploaded files are lost when the service restarts
- For production use, consider adding cloud storage (S3, etc.)

## Troubleshooting

### Build Fails
- Check the build logs in Render dashboard
- Common issue: Missing dependencies in `requirements.txt`

### App Crashes
- Check the logs in Render dashboard
- Verify ChromeDriver installation in Dockerfile

### Slow Scraping
- Free tier has limited CPU/memory
- Consider upgrading to paid tier for better performance

## Next Steps

After deployment:
1. Test by uploading a small Excel file
2. Verify scraping works correctly
3. Share the URL with your team!

## Need Help?
- Render docs: https://render.com/docs
- GitHub issues: Create an issue in your repo
