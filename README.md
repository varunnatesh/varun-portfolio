# Varun K N - Professional Portfolio

A modern, professional portfolio website showcasing AI/ML projects, research publications, and technical expertise.

## 🚀 Features

- **Modern UI/UX**: Clean, professional design with smooth animations
- **Responsive Design**: Works perfectly on all devices
- **Project Showcase**: Featured projects with live demos and metrics
- **Research Publications**: IEEE published work
- **Skills Visualization**: Interactive technical skills display
- **Admin Panel**: Easy content management
- **SEO Optimized**: Ready for professional visibility

## 🛠️ Tech Stack

- Django 5.0
- HTML5, CSS3, JavaScript
- SQLite (Development) / PostgreSQL (Production)
- WhiteNoise for static files

## 📦 Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd portfolio
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
cp .env.example .env
# Edit .env with your settings
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Load initial data (optional)**
```bash
python manage.py loaddata initial_data.json
```

8. **Run the development server**
```bash
python manage.py runserver
```

Visit: http://localhost:8000

## 🎨 Color Palette

- Primary: #6366f1 (Indigo)
- Secondary: #8b5cf6 (Purple)
- Accent: #06b6d4 (Cyan)
- Dark: #0f172a (Slate)
- Light: #f8fafc (Slate)

## 📝 Admin Panel

Access the admin panel at: http://localhost:8000/admin

Manage:
- Projects
- Skills
- Certifications
- Experience
- Contact messages

## 🚀 Deployment

Ready to deploy on:
- Railway
- Heroku
- PythonAnywhere
- AWS
- DigitalOcean

## 📄 License

Personal Portfolio - All Rights Reserved

## 👤 Author

**Varun K N**
- LinkedIn: [varun-k-n-566135251](https://linkedin.com/in/varun-k-n-566135251)
- GitHub: [varunnatesh](https://github.com/varunnatesh)
- Email: varunnatesh10@gmail.com
