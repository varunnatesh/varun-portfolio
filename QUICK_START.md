# ⚡ Quick Start - Varun K N Portfolio

## 🚀 Start the Server
```bash
python manage.py runserver
```
**Visit:** http://localhost:8000

## 🔐 Admin Panel
**URL:** http://localhost:8000/admin  
**Username:** `admin`  
**Password:** `admin123`  

⚠️ **Change this password immediately!**

## 📋 What's Included

✅ **4 Featured Projects** - With real metrics from your resume  
✅ **24 Technical Skills** - Organized by category  
✅ **4 Certifications** - AWS, Azure, Google Cloud, Tata  
✅ **1 IEEE Publication** - Snake Detection Research  
✅ **Professional Design** - Modern, responsive, animated  

## 🎨 Design Features

- 🌈 **Modern Color Palette** - Indigo, Purple, Cyan
- ✨ **Smooth Animations** - Fade, slide, typing effects
- 📱 **Fully Responsive** - Mobile, tablet, desktop
- ⚡ **Fast & Lightweight** - Optimized performance
- 🎯 **SEO Ready** - Meta tags configured

## 📝 Quick Tasks

### Add Your Photo
1. Admin Panel → Site Configuration
2. Upload profile image
3. Save

### Upload Resume
1. Admin Panel → Site Configuration  
2. Upload resume PDF file
3. Save

### Add Your Intro Video 🎥 NEW!
1. Admin Panel → Site Configuration
2. Upload your intro video (MP4, under 50MB)
3. Or paste external video URL
4. Save
5. See **VIDEO_SETUP_GUIDE.md** for details

### Add Project Images
1. Admin Panel → Projects
2. Edit any project
3. Upload project image
4. Save

### Customize About Section
1. Admin Panel → Site Configuration
2. Edit "About Description"
3. Save

### Add GitHub/Demo Links
1. Admin Panel → Projects
2. Edit project
3. Fill in GitHub URL and Live Demo URL
4. Save

## 🎯 Pages Available

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Hero, featured projects, skills |
| Projects | `/projects/` | All projects with filtering |
| Project Detail | `/projects/<slug>/` | Individual project page |
| Research | `/research/` | Publications & papers |
| About | `/about/` | Education & certifications |
| Contact | `/contact/` | Contact form & info |
| Admin | `/admin/` | Content management |

## 🔧 Useful Commands

```bash
# Start server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Load sample data (already done)
python manage.py load_initial_data

# Collect static files (for production)
python manage.py collectstatic
```

## 📦 Project Files

```
Key Files:
├── manage.py              # Django management
├── SETUP_GUIDE.md         # Detailed setup instructions
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── templates/portfolio/   # HTML templates
├── static/               # CSS, JS, images
├── portfolio/models.py   # Database models
└── portfolio/admin.py    # Admin configuration
```

## 💡 Customization

### Change Colors
Edit: `static/css/style.css` (Line 11-19)

### Change Typing Effect
Edit: `static/js/main.js` (Line 54-60)

### Update Hero Text
Admin Panel → Site Configuration

### Add Social Links
Admin Panel → Site Configuration

## 🌐 Ready to Deploy?

### Railway
```bash
railway login
railway init
railway up
```

### Heroku
```bash
heroku create varun-portfolio
git push heroku main
```

### Requirements
- Set `DEBUG=False` in production
- Set proper `SECRET_KEY`
- Add your domain to `ALLOWED_HOSTS`

## 🎉 You're Ready!

Your portfolio is **live and running**!

**Portfolio URL:** http://localhost:8000  
**Admin Panel:** http://localhost:8000/admin

---

**Need Help?**  
Read the detailed **SETUP_GUIDE.md** for more information.

**Contact:**
- Email: varunnatesh10@gmail.com
- LinkedIn: https://linkedin.com/in/varun-k-n-566135251
- GitHub: https://github.com/varunnatesh
