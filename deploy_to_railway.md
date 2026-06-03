# 🚀 QUICK DEPLOY TO RAILWAY (FREE)

## ⚡ 3 Simple Steps:

### **STEP 1: Push to GitHub** (2 mins)

Open Command Prompt in `C:\vaunportfolio` and run:

```bash
git init
git add .
git commit -m "My portfolio ready for deployment"
```

Then create repository on GitHub:
1. Go to: https://github.com/new
2. Name: `varun-portfolio`
3. Click "Create repository"
4. Copy the commands shown and run them

OR use these (replace YOUR_USERNAME):

```bash
git remote add origin https://github.com/YOUR_USERNAME/varun-portfolio.git
git branch -M main
git push -u origin main
```

---

### **STEP 2: Deploy on Railway** (3 mins)

1. Go to: https://railway.app
2. Click "Login with GitHub"
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose `varun-portfolio`
6. Railway auto-deploys! ✨

---

### **STEP 3: Configure** (2 mins)

In Railway dashboard:

1. **Add Variables:**
   - Click "Variables"
   - Add:
     ```
     DEBUG=False
     SECRET_KEY=change-this-to-random-long-string
     ```

2. **Generate Domain:**
   - Click "Settings" → "Networking"
   - Click "Generate Domain"
   - Copy your URL (e.g., `yourapp.up.railway.app`)

3. **Update ALLOWED_HOSTS:**
   - Go back to "Variables"
   - Add:
     ```
     ALLOWED_HOSTS=yourapp.up.railway.app
     ```

4. **Create Admin User:**
   - In Railway, click "Deployments"
   - Click latest deployment
   - Open "Console" tab
   - Run:
     ```
     python manage.py createsuperuser
     ```
   - Enter username, email, password

---

## 🎉 DONE!

Your portfolio is LIVE at:
```
https://yourapp.up.railway.app
```

Admin panel:
```
https://yourapp.up.railway.app/admin
```

---

## 🔥 FREE Forever!

Railway free tier includes:
- ✅ 500 hours/month (plenty!)
- ✅ Free domain
- ✅ Free HTTPS
- ✅ Auto-deploy from GitHub

Your portfolio will NEVER cost money! 💰

---

## 📝 Quick Commands Reference:

**Update your live site:**
```bash
git add .
git commit -m "Updated content"
git push
```
Railway auto-deploys! No other steps needed!

---

## 🎯 What to Do After Deployment:

1. Visit your live site
2. Go to `/admin`
3. Login with superuser
4. Upload:
   - Your photo
   - Resume PDF  
   - Project images
5. Share your link everywhere!

---

**Need detailed help?** Read `DEPLOYMENT_GUIDE.md`

**Ready to deploy?** Start with STEP 1 above! 🚀
