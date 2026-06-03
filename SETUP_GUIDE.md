# 🚀 Varun K N Portfolio - Setup Guide

## ✅ Installation Complete!

Your professional portfolio is ready to launch! Here's everything you need to know.

## 🎯 Quick Start

### 1. Run the Development Server
```bash
python manage.py runserver
```

Visit: **http://localhost:8000**

### 2. Access Admin Panel
- URL: **http://localhost:8000/admin**
- Username: **admin**
- Password: **admin123**

⚠️ **Important:** Change the admin password after first login!

## 📊 What's Already Loaded

✓ **Skills** - 24 technical skills across 5 categories
✓ **Projects** - 4 featured projects with metrics
✓ **Certifications** - 4 professional certifications
✓ **Publications** - 1 IEEE research paper
✓ **Site Configuration** - All contact info and settings

## 🎨 Features

### 🏠 Homepage
- **Hero Section** with animated typing effect
- **Featured Projects** with metrics and demos
- **Skills** organized by category with progress bars
- **Publications** IEEE research showcase
- **Certifications** professional credentials
- **CTA Section** for conversions

### 📁 Projects Page
- **All Projects** with filtering (All/Completed/Ongoing)
- **Project Cards** with status, tech stack, metrics
- **Pagination** for large collections

### 📄 Project Detail Pages
- **Full Description** with formatted text
- **Key Metrics** in visual cards
- **Technologies** used
- **Links** to GitHub and live demos

### 📚 Research Page
- **IEEE Publications** with abstracts
- **Keywords** and conference details
- **Links** to full papers

### 👤 About Page
- **Education** background
- **Certifications** with verification links
- **Professional narrative**

### 📧 Contact Page
- **Contact Form** with validation
- **Contact Information** email, phone, location
- **Social Links** LinkedIn, GitHub

## 🎨 Color Palette

- **Primary:** #6366f1 (Indigo)
- **Secondary:** #8b5cf6 (Purple)
- **Accent:** #06b6d4 (Cyan)
- **Dark:** #0f172a (Slate)
- **Light:** #f8fafc (Slate)

## 📝 Admin Panel - Managing Content

### Adding/Editing Projects
1. Go to **Admin Panel** → **Projects**
2. Click **Add Project** or edit existing
3. Fill in:
   - Title, description, technologies
   - Upload project image
   - Add GitHub/Demo URLs
   - Set metrics (accuracy, R², mAP, etc.)
   - Mark as **Featured** for homepage

### Managing Skills
1. **Admin Panel** → **Skills**
2. Categories: Programming, ML, DL, Data, Tools
3. Set proficiency level (0-100)

### Adding Certifications
1. **Admin Panel** → **Certifications**
2. Add title, issuer, date
3. Upload certificate image (optional)
4. Add verification URL

### Site Configuration
1. **Admin Panel** → **Site Configuration**
2. Edit:
   - Hero section text
   - About description
   - Contact information
   - Upload resume PDF
   - SEO meta tags

## 🚀 Customization Tips

### Changing Colors
Edit `static/css/style.css` - CSS variables at the top:
```css
:root {
    --color-primary: #6366f1;
    --color-secondary: #8b5cf6;
    /* ... */
}
```

### Adding Your Photo
1. Upload via **Admin Panel** → **Site Configuration**
2. Or place in `media/profile/` folder

### Updating Resume
1. Upload PDF via **Admin Panel** → **Site Configuration**
2. Download button appears automatically

### Typing Effect Text
Edit `static/js/main.js` - `phrases` array:
```javascript
const phrases = [
    'AI Researcher',
    'Your Custom Title',
    // Add more...
];
```

## 📱 Responsive Design

✓ Mobile-friendly navigation
✓ Responsive grids and layouts
✓ Touch-optimized interactions
✓ Works on all screen sizes

## 🎭 Animations

- **AOS (Animate On Scroll)** - Fade, slide effects
- **Typing Effect** - Dynamic hero text
- **Skill Bars** - Progress animations
- **Hover Effects** - Interactive cards
- **Smooth Scrolling** - Navigation

## 🔧 Project Structure

```
vaunportfolio/
├── portfolio/              # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # View logic
│   ├── admin.py           # Admin configuration
│   └── urls.py            # URL routing
├── templates/portfolio/    # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Homepage
│   ├── projects.html      # Projects list
│   ├── project_detail.html
│   ├── about.html
│   ├── contact.html
│   └── research.html
├── static/                 # Static files
│   ├── css/style.css      # Main styles
│   └── js/main.js         # JavaScript
├── media/                  # Uploaded files
└── portfolio_project/      # Project settings
    └── settings.py
```

## 🌐 Deployment

### Option 1: Railway
```bash
# Add Procfile
web: gunicorn portfolio_project.wsgi --log-file -
```

### Option 2: Heroku
```bash
heroku create your-portfolio
git push heroku main
```

### Option 3: PythonAnywhere
1. Upload code
2. Set virtualenv
3. Configure WSGI

### Environment Variables for Production
```
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=yourdomain.com
```

## 🎯 Next Steps

1. ✅ Change admin password
2. ✅ Upload your photo
3. ✅ Add your resume PDF
4. ✅ Customize about section
5. ✅ Add project images
6. ✅ Test contact form
7. ✅ Deploy to production

## 📞 Support

- **GitHub:** https://github.com/varunnatesh
- **Email:** varunnatesh10@gmail.com
- **LinkedIn:** https://linkedin.com/in/varun-k-n-566135251

## 🎉 You're All Set!

Your professional portfolio is ready to showcase your AI/ML expertise!

**Run:** `python manage.py runserver`
**Visit:** http://localhost:8000

---

Built with ❤️ using Django, Modern CSS, and JavaScript
