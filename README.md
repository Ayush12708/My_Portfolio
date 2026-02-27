# Ayush Kumar - Software Engineering Portfolio 🚀

A modern, responsive portfolio website built with **Django**, **AWS**, and optimized for deployment on **Vercel**. This project showcases my technical skills, featured projects, certifications, and achievements in a sleek, glassmorphism-inspired interface.

## ✨ Key Features

- **Dynamic Content**: Managed via Django Admin and AWS RDS (MySQL).
- **Responsive Design**: Modern UI with a focus on usability and professional aesthetics.
- **Project Showcase**: Displaying full-view project images with direct links to GitHub and Live Apps.
- **Production Ready**: Configured with `Whitenoise` for static file serving and `vercel.json` for serverless deployment.
- **Contact Integration**: Integrated Gmail SMTP for secure email notifications.

## 🛠️ Technical Engine

- **Backend**: Python 3.12, Django 6.0
- **Database**: AWS RDS (MySQL)
- **DevOps & Hosting**: Vercel, Git
- **Static Files**: Whitenoise
- **Frontend**: HTML5, Vanilla CSS3 (Glassmorphism), JavaScript

## 🚀 Getting Started

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ayush12708/My_Portfolio.git
   cd My_Portfolio
   ```

2. **Set up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory and add your credentials:
   ```env
   SECRET_KEY=your_secret_key
   DB_HOST=your_rds_endpoint
   DB_NAME=your_db_name
   DB_USER=your_user
   DB_PASSWORD=your_password
   SMTP_USER=your_gmail
   SMTP_PASSWORD=your_app_password
   ```

5. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## 🌍 Deployment on Vercel

This project is optimized for **Vercel**. To deploy:

1. Import this repository into Vercel.
2. Add the `.env` variables in the Vercel Dashboard (Settings > Environment Variables).
3. The `vercel.json` will automatically handle the build and deployment.

---
Built with ❤️ by [Ayush Kumar](https://github.com/Ayush12708)
