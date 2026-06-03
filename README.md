# Varun K N - Professional Portfolio

[![Live Demo](https://img.shields.io/badge/Live-Portfolio-6366f1?style=for-the-badge&logo=google-chrome&logoColor=white)](https://varun-portfolio-a43b.onrender.com)
[![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> **🌐 [View Live Portfolio](https://varun-portfolio-a43b.onrender.com)** - AI Researcher & IEEE Published Developer

A modern, professional portfolio website showcasing AI/ML projects, IEEE research publications, and technical expertise. Built with Django and deployed on Render.

![Portfolio Preview](https://img.shields.io/badge/Status-Live-success?style=flat-square)

## ✨ Highlights

- 🎓 **IEEE Published Researcher** - Real-Time Snake Detection Using Deep Learning
- 🚀 **4 Production ML Projects** - 91.5% accuracy, R² = 0.94
- 🏆 **4 Cloud Certifications** - AWS, Google Cloud, Azure, Tata Group
- 📊 **24+ Technical Skills** - Python, ML/DL, Computer Vision, Cloud

## 🚀 Features

- **Modern UI/UX**: Clean, professional design with smooth animations
- **Responsive Design**: Works perfectly on all devices (mobile, tablet, desktop)
- **Video Introduction**: Cloudinary-hosted intro video
- **Project Showcase**: Featured projects with live demos and metrics
- **Research Publications**: IEEE published work display
- **Skills Visualization**: Interactive technical skills with proficiency levels
- **Admin Panel**: Easy content management
- **SEO Optimized**: Meta tags and structured data
- **Production Ready**: Deployed on Render with automatic deployments

## 🛠️ Tech Stack

**Backend:**
- Django 5.0 - Web framework
- Python 3.11 - Programming language
- SQLite - Database
- WhiteNoise - Static file serving

**Frontend:**
- HTML5 - Structure
- CSS3 - Styling with CSS Variables
- JavaScript (ES6+) - Interactivity
- AOS Library - Scroll animations

**Hosting & Media:**
- Render.com - Web hosting (free tier)
- Cloudinary - Video hosting
- GitHub - Source control

**Color Palette:**
- Primary: #6366f1 (Indigo)
- Secondary: #8b5cf6 (Purple)
- Accent: #06b6d4 (Cyan)
- Dark: #0f172a (Slate)
- Light: #f8fafc (Slate)

## 🌟 Live Portfolio

**Visit:** [https://varun-portfolio-a43b.onrender.com](https://varun-portfolio-a43b.onrender.com)

### Portfolio Sections:
- 🏠 **Home** - Introduction with video
- 💼 **Projects** - 4 featured ML/AI projects
- 🔬 **Research** - IEEE publication
- 👤 **About** - Background and expertise
- 📬 **Contact** - Get in touch form

## 📦 Local Development

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/varunnatesh/varun-portfolio.git
cd varun-portfolio
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
# Create .env file (optional for local development)
# SECRET_KEY and DEBUG are set with defaults
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Load initial data**
```bash
python manage.py load_initial_data
```

7. **Create admin user**
```bash
# Default admin created automatically:
# Username: admin
# Password: admin123
# (Change this in production!)
```

8. **Run the development server**
```bash
python manage.py runserver
```

9. **Access the site**
- Portfolio: http://localhost:8000
- Admin Panel: http://localhost:8000/admin

## 📝 Admin Panel

Access the admin panel to manage content:

**Local:** http://localhost:8000/admin  
**Production:** https://varun-portfolio-a43b.onrender.com/admin

**Default Credentials:**
- Username: `admin`
- Password: `admin123` (change in production!)

### Manage Content:
- ✏️ Projects - Add/edit project details, metrics, technologies
- 🎯 Skills - Update skills and proficiency levels
- 🏆 Certifications - Add new certifications
- 📚 Publications - Manage research papers
- 💼 Experience - Update work experience
- 📧 Contact Messages - View submissions
- ⚙️ Site Configuration - Hero text, video URL, about section

## 🚀 Deployment

This portfolio is deployed on **Render.com** (free tier).

### Deployment Features:
- ✅ Automatic deployments from GitHub
- ✅ HTTPS enabled
- ✅ Custom domain support
- ✅ Environment variables
- ✅ Build automation via `build.sh`

### Deploy Your Own:

1. Fork this repository
2. Create account on [Render.com](https://render.com)
3. Create new Web Service
4. Connect your GitHub repository
5. Render will auto-detect Django and deploy!

**Note:** Free tier sleeps after 15 minutes of inactivity. First load may take 30-60 seconds.

### Alternative Platforms:
- Railway.app
- Heroku
- PythonAnywhere
- AWS EC2
- DigitalOcean

## 📊 Project Structure

```
varun-portfolio/
├── portfolio/                 # Main Django app
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py               # URL routing
│   ├── admin.py              # Admin configuration
│   └── management/           # Custom commands
│       └── commands/
│           ├── load_initial_data.py
│           └── setup_video.py
├── portfolio_project/        # Django project settings
│   ├── settings.py           # Configuration
│   ├── urls.py               # Root URL config
│   └── wsgi.py               # WSGI config
├── templates/                # HTML templates
│   └── portfolio/
│       ├── base.html
│       ├── home.html
│       ├── projects.html
│       ├── about.html
│       └── contact.html
├── static/                   # Static files
│   ├── css/
│   │   └── style.css        # Main stylesheet (1000+ lines)
│   ├── js/
│   │   └── main.js          # JavaScript
│   └── images/
├── media/                    # User uploads
│   └── videos/
│       └── intro.mp4
├── build.sh                  # Render build script
├── requirements.txt          # Python dependencies
├── runtime.txt              # Python version
├── render.yaml              # Render configuration
└── manage.py                # Django management
```

## 📸 Screenshots

### Home Page with Video Introduction
![Home Page](https://via.placeholder.com/800x400/6366f1/ffffff?text=Portfolio+Home+Page)

### Projects Showcase
![Projects](https://via.placeholder.com/800x400/8b5cf6/ffffff?text=Featured+Projects)

### Skills & Expertise
![Skills](https://via.placeholder.com/800x400/06b6d4/ffffff?text=Technical+Skills)

## 🎯 Key Features Implemented

### Video Integration
- ✅ Cloudinary CDN hosting
- ✅ HTML5 video player
- ✅ Responsive display
- ✅ Google Drive fallback support
- ✅ YouTube embed support

### Professional Design
- ✅ Modern gradient backgrounds
- ✅ Smooth scroll animations (AOS)
- ✅ Typing effect on hero section
- ✅ Interactive skill bars
- ✅ Responsive navigation
- ✅ Mobile-first approach

### Content Management
- ✅ Django admin panel
- ✅ Automatic data loading
- ✅ Easy content updates
- ✅ Contact form submissions
- ✅ SEO optimization

## 🤝 Contributing

This is a personal portfolio project. However, if you'd like to use it as a template:

1. Fork the repository
2. Customize the content in `load_initial_data.py`
3. Update colors in `style.css` CSS variables
4. Modify templates to match your style
5. Deploy to your preferred platform

## 📄 License

© 2024-2026 Varun K N. All rights reserved.

This portfolio is for personal use. Feel free to use it as inspiration for your own portfolio, but please don't use my personal content (projects, publications, etc.).

## 👤 Author

**Varun K N**  
*AI Researcher & IEEE Published Developer*

- 🌐 Portfolio: [varun-portfolio-a43b.onrender.com](https://varun-portfolio-a43b.onrender.com)
- 💼 LinkedIn: [varun-k-n-566135251](https://linkedin.com/in/varun-k-n-566135251)
- 💻 GitHub: [varunnatesh](https://github.com/varunnatesh)
- 📧 Email: varunnatesh10@gmail.com
- 📍 Location: Mysuru, Karnataka, India

## 🙏 Acknowledgments

- Django Framework - [djangoproject.com](https://www.djangoproject.com/)
- Render.com - Free web hosting
- Cloudinary - Media hosting
- Font Awesome - Icons
- AOS Library - Scroll animations
- Google Fonts - Inter typeface

---

### 📈 Stats

![GitHub repo size](https://img.shields.io/github/repo-size/varunnatesh/varun-portfolio?style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/varunnatesh/varun-portfolio?style=flat-square)
![GitHub stars](https://img.shields.io/github/stars/varunnatesh/varun-portfolio?style=social)

**⭐ Star this repository if you find it helpful!**

---

**Built with ❤️ by Varun K N** | [View Live Portfolio →](https://varun-portfolio-a43b.onrender.com)
