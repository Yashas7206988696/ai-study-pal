# 🎓 AI Study Pal

*An intelligent companion for modern learners*

[![Made with Flask](https://img.shields.io/badge/Backend-Flask-blue?style=flat-square)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/Frontend-React-61dafb?style=flat-square)](https://reactjs.org/)
[![AI Powered](https://img.shields.io/badge/AI-Powered-ff6b6b?style=flat-square)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

## 🌟 Overview

AI Study Pal is a revolutionary learning platform that harnesses the power of artificial intelligence to transform your study experience. Designed specifically for engineering and computer science students, this full-stack application combines intelligent quiz generation, content summarization, and personalized study planning to help you achieve academic excellence.

### ✨ Key Features

- 🤖 **AI-Powered Quiz Generation**: Automatically create comprehensive quizzes from your study materials
- 📊 **Intelligent Study Analytics**: Track your progress with detailed performance insights
- 📝 **Smart Content Summarization**: Get concise summaries of complex topics
- 🎯 **Personalized Study Plans**: Adaptive learning paths tailored to your needs
- 📈 **Progress Visualization**: Beautiful charts and graphs powered by Matplotlib
- 🔄 **Real-time Learning**: Interactive React frontend with seamless API integration

## 🏗️ Architecture

```
ai-study-pal/
├── 📁 .vscode/              # VS Code configuration
├── 📁 backend/              # Flask API server
│   ├── 📄 app.py           # Main Flask application
│   ├── 📁 models/          # AI models and algorithms
│   ├── 📁 routes/          # API route handlers
│   └── 📁 utils/           # Helper functions
├── 📁 frontend/             # React application
│   ├── 📁 public/          # Static assets
│   ├── 📁 src/             # React components and logic
│   │   ├── 📁 components/  # Reusable UI components
│   │   ├── 📁 pages/       # Application pages
│   │   ├── 📁 hooks/       # Custom React hooks
│   │   └── 📁 utils/       # Frontend utilities
│   └── 📄 package.json    # Node.js dependencies
├── 📄 requirements.txt      # Python dependencies
├── 📄 start_dev.ps1        # Development startup script
├── 📄 start_site.ps1       # Production startup script
├── 📄 .gitignore          # Git ignore rules
├── 📄 LICENSE             # MIT License
└── 📄 README.md           # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm or yarn
- Git

### 🔧 Backend Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yashas7206988696/ai-study-pal.git
   cd ai-study-pal
   ```

2. **Create and activate virtual environment**
   ```powershell
   # Windows PowerShell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Flask server**
   ```bash
   python backend/app.py
   ```
   
   🌐 Backend server will be running at `http://127.0.0.1:5000`

### ⚛️ Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Start the React development server**
   ```bash
   npm start
   # or
   yarn start
   ```
   
   🌐 Frontend will be available at `http://localhost:3000`

### 🎯 One-Click Setup (Windows)

For Windows users, we've included convenient PowerShell scripts:

```powershell
# Development mode
.\start_dev.ps1

# Production mode
.\start_site.ps1
```

## 📖 Usage Guide

### Getting Started

1. **Launch the Application**: Start both backend and frontend servers
2. **Create Your Profile**: Set up your study preferences and goals
3. **Upload Study Materials**: Add your notes, textbooks, or lecture slides
4. **Generate Quizzes**: Let AI create personalized quizzes from your content
5. **Track Progress**: Monitor your learning journey with detailed analytics

### Advanced Features

- **Custom Study Plans**: Create tailored learning schedules
- **Topic Mastery Tracking**: Monitor understanding across different subjects
- **Collaborative Learning**: Share quizzes and study materials with peers
- **Export Results**: Download your progress reports and quiz results

## 🛠️ Development

### Tech Stack

**Backend:**
- Flask (Web Framework)
- SQLAlchemy (ORM)
- Matplotlib (Data Visualization)
- NumPy & Pandas (Data Processing)
- Scikit-learn (Machine Learning)

**Frontend:**
- React 18 (UI Framework)
- React Router (Navigation)
- Axios (HTTP Client)
- Chart.js (Data Visualization)
- Material-UI (Component Library)

### API Documentation

The backend provides RESTful API endpoints:

- `GET /api/quizzes` - Retrieve all quizzes
- `POST /api/quiz/generate` - Generate new quiz
- `GET /api/analytics` - Get study analytics
- `POST /api/summarize` - Summarize content

### Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for JavaScript/React
- Write unit tests for new features
- Update documentation for API changes

## 🔒 Security & Privacy

- All user data is processed locally
- No sensitive information is stored permanently
- Secure API endpoints with authentication
- Regular security audits and updates

## 📊 Performance

- Optimized React components with lazy loading
- Efficient database queries with SQLAlchemy
- Matplotlib configured for headless rendering
- Responsive design for all device sizes

## 🤝 Contributing

We believe in the power of community-driven development! Whether you're fixing bugs, adding features, or improving documentation, your contributions are valuable.

### Ways to Contribute

- 🐛 Report bugs and issues
- 💡 Suggest new features
- 📚 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repository

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact & Support

- **Developer**: Yashas7206988696
- **Repository**: [ai-study-pal](https://github.com/Yashas7206988696/ai-study-pal)
- **Issues**: [Report a Bug](https://github.com/Yashas7206988696/ai-study-pal/issues)

## 🙏 Acknowledgments

- Thanks to the open-source community for amazing tools and libraries
- Special recognition to Flask and React communities
- Inspired by the need for intelligent learning tools in modern education

## 🗺️ Roadmap

- [ ] Mobile application (React Native)
- [ ] Advanced AI models for content analysis
- [ ] Real-time collaboration features
- [ ] Integration with popular LMS platforms
- [ ] Multi-language support
- [ ] Voice-to-text quiz generation

---

<div align="center">
  <strong>🎓 Happy Learning with AI Study Pal! 🎓</strong>
  <br>
  <em>Empowering students through intelligent technology</em>
</div>
