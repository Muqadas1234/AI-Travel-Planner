

# 🚀 Raise Your Hack Hackathon – lablab.ai 2025

# 🧳 AI Travel Planner project

## 📚 Table of Contents
- 🔖 <u>[📄 Overview](#-overview)</u>
- ✨ <u>[Features](#-features)</u>
- 🛠️ <u>[Technologies Used](#️-technologies-used)</u>
- 📦 <u>[Project Structure](#-project-structure)</u>
- 🚀 <u>[Key Features Explained](#-key-features-explained)</u>
- ⚙️ <u>[Installation & Setup](#️-installation--setup)</u>
- 🔑 <u>[API Keys Required](#-api-keys-required)</u>
- 📊 <u>[Database Schema](#-database-schema)</u>
- 🧪 <u>[Testing](#-testing)</u>
- 🔒 <u>[Security Considerations](#-security-considerations)</u>
- 🚀 <u>[Deployment](#-deployment)</u>
- 📝 <u>[API Documentation](#-api-documentation)</u>
- 🐛 <u>[Troubleshooting](#-troubleshooting)</u>
- 🤝 <u>[Contributing](#-contributing)</u>
- 🙋‍♂️ <u>[Authors & Contributors](#-authors--contributors)</u>
- 📞 <u>[Support](#-support)</u>
- 🔄 <u>[Version History](#-version-history)</u>


# 🧳 AI Travel Planner
📄 Overview
AI Travel Planner is an intelligent, AI-powered web app designed to simplify trip planning. It creates personalized itineraries, smart budget breakdowns, and destination suggestions using real-time travel data and user preferences. Powered by LLaMA via Groq, and integrated with APIs like Tavily and Booking.com, it offers a seamless experience with a modern UI, secure authentication, and dynamic traveler profiling.

## ✨ Features

### 🔐 Authentication & User Management
- **User Registration** with email verification
- **Secure Login/Logout** with session management
- **Email Verification** with 6-digit code system
- **Password Reset** with secure email-based recovery
- **Remember Me** functionality with extended session
- **Password Hashing** using Werkzeug security

### 👤 Traveler Profile System
- **Graph-Based Profile Management** using NetworkX
- **Dynamic Profile Building** from user interactions
- **Budget Preferences** tracking and analysis
- **Interest-Based Recommendations** system
- **Travel History** and preference learning
- **Profile Export** to CSV format
- **Profile Clearing** functionality

### 🎯 AI-Powered Travel Planning
- **Personalized Itinerary Generation** using LLaMA model via Groq API
- **Smart Budget Analysis** with category breakdown
- **Travel Tips & Recommendations** based on destination and preferences
- **Context-Aware Suggestions** using traveler profile data
- **Advanced Prompt Engineering** for structured AI responses

### ✈️ Real-Time Travel Data
- **Flight Search** via Tavily API integration
- **Hotel Booking** via Booking.com RapidAPI
- **Destination Information** and recommendations
- **Price Comparison** and budget-friendly options

### 📋 Travel Plan Management
- **Create Travel Plans** with detailed itineraries
- **View Plan Details** with comprehensive breakdown
- **Edit Existing Plans** with form-based updates
- **Delete Plans** with confirmation
- **Plan History** tracking and storage
- **CSV Export** of travel history

### 🎨 Modern User Interface
- **Responsive Design** for all devices (mobile, tablet, desktop)
- **Beautiful UI** with Tailwind CSS
- **Glass Morphism Effects** and modern styling
- **Animated Backgrounds** and floating elements
- **Interactive Forms** with validation
- **Flash Messages** for user feedback
- **Loading States** and smooth transitions

### 📧 Email System
- **Professional Email Templates** with HTML formatting
- **Gmail SMTP Integration** for reliable delivery
- **Verification Emails** with branded design
- **Password Reset Emails** with security codes
- **Email Error Handling** and logging

### 🔒 Security Features
- **CSRF Protection** with Flask-WTF
- **Session Management** with secure cookies
- **Input Validation** and sanitization
- **SQL Injection Prevention** with SQLAlchemy ORM
- **XSS Protection** with proper escaping
- **Secure Password Storage** with hashing

---

## 🛠️ Technologies Used

### Backend Framework
- **Python 3.8+** - Core programming language
- **Flask 3.0.3** - Lightweight web framework
- **Flask-SQLAlchemy** - Database ORM
- **Werkzeug** - Security utilities

### Database
- **SQLite** - Lightweight database
- **SQLAlchemy ORM** - Database abstraction layer
- **Database Migrations** - Schema management

### AI & Machine Learning
- **Groq API** - LLaMA model access
- **Prompt Engineering** - Custom AI prompts
- **JSON Response Parsing** - Structured AI outputs
- **Context-Aware Generation** - Personalized AI responses

### Data Processing & Analysis
- **NetworkX 3.2.1** - Graph-based profile system
- **JSON Processing** - Data serialization
- **CSV Generation** - Data export functionality
- **Regular Expressions** - Text processing

### External APIs
- **Tavily API** - Flight search and travel information
- **Booking.com RapidAPI** - Hotel booking data
- **Requests Library** - HTTP client for API calls

### Frontend Technologies
- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework
- **Jinja2 Templates** - Server-side templating
- **JavaScript** - Interactive functionality
- **CSS3** - Advanced styling and animations

### Email & Communication
- **SMTP (Gmail)** - Email delivery
- **MIME Multipart** - HTML email formatting
- **Email Templates** - Professional messaging

### Development & Testing
- **Python-dotenv** - Environment variable management
- **Unit Testing** - Test cases and validation
- **Error Handling** - Comprehensive error management
- **Logging** - Debug and error tracking

---

## 📦 Project Structure

```
Flask project folder/
│
├── traveler_planer.py         # Main Flask application (721 lines)
│   ├── Database Models (User, TravelerProfile, TravelPlan)
│   ├── Authentication Routes (login, register, verify, reset)
│   ├── Travel Planning Routes (home, profile, plan management)
│   ├── API Integrations (Groq, Tavily, Booking.com)
│   ├── Email System (verification, password reset)
│   └── CSV Export functionality
│
├── traveler_profile.py        # Graph-based profile system (279 lines)
│   ├── NetworkX graph implementation
│   ├── Profile node management
│   ├── Interest and budget tracking
│   └── Recommendation engine
│
├── prompt_engine.py           # AI prompt engineering (282 lines)
│   ├── Structured prompt templates
│   ├── Context-aware generation
│   ├── JSON response formatting
│   └── Multi-component prompts
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── templates/                 # HTML templates (Jinja2)
│   ├── index.html            # Main travel planning interface
│   ├── login.html            # Authentication page
│   ├── register.html         # User registration
│   ├── verify.html           # Email verification
│   ├── forgot_password.html  # Password reset request
│   ├── reset_password.html   # Password reset form
│   ├── profile.html          # User profile management
│   ├── plan_detail.html      # Travel plan details
│   └── plan_edit.html        # Plan editing interface
│
├── static/                    # Static assets
│   └── images/
│       └── airport_bg.jpg    # Background images
│
├── instance/                  # Application data
│   └── travel_planner.db     # SQLite database
│
├── test_phase3.py            # Test cases and validation
├── groq_json_test.py         # API testing utilities
└── venv/                     # Python virtual environment
```

---

## 🚀 Key Features Explained

### 1. **Graph-Based Traveler Profiles**
- Uses NetworkX to create dynamic user profiles
- Tracks budget preferences, interests, and travel history
- Generates personalized recommendations based on profile data
- Supports profile export and management

### 2. **Advanced Prompt Engineering**
- Custom prompts for LLaMA model to generate structured responses
- Context-aware generation using traveler profile data
- Multi-component prompts for itineraries, budget analysis, and tips
- JSON response parsing for consistent data structure

### 3. **Real-Time API Integrations**
- **Tavily API**: Flight search and travel information
- **Booking.com API**: Hotel availability and pricing
- **Groq API**: LLaMA model for AI-powered content generation

### 4. **Comprehensive Email System**
- Professional HTML email templates
- Gmail SMTP integration for reliable delivery
- Verification and password reset functionality
- Error handling and logging

### 5. **Modern UI/UX Design**
- Responsive design for all devices
- Glass morphism effects and modern styling
- Interactive forms with validation
- Smooth animations and transitions

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Gmail account (for email functionality)

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Flask project folder
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```env
   SECRET_KEY=your_flask_secret_key_here
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   RAPIDAPI_KEY=your_rapidapi_key
   GMAIL_USER=your_gmail@gmail.com
   GMAIL_PASSWORD=your_gmail_app_password
   ```

5. **Run the application:**
   ```bash
   python traveler_planer.py
   ```

6. **Access the application:**
   Open your browser and visit: `http://localhost:5000`

---

## 🔑 API Keys Required

### 1. **Groq API Key**
- Sign up at [groq.com](https://groq.com)
- Used for LLaMA model access and AI content generation

### 2. **Tavily API Key**
- Sign up at [tavily.com](https://tavily.com)
- Used for flight search and travel information

### 3. **RapidAPI Key (Booking.com)**
- Sign up at [rapidapi.com](https://rapidapi.com)
- Used for hotel booking data

### 4. **Gmail App Password**
- Enable 2-factor authentication on your Gmail account
- Generate an app password for SMTP access
- Used for email verification and password reset

---

## 📊 Database Schema

### User Table
- `id` (Primary Key)
- `name` (String)
- `email` (Unique String)
- `password_hash` (String)
- `is_verified` (Boolean)
- `verification_code` (String)
- `reset_code` (String)
- `reset_code_expiry` (DateTime)

### TravelerProfile Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `budget` (String)
- `interests` (String)
- `preferences` (String)

### TravelPlan Table
- `id` (Primary Key)
- `user_id` (Foreign Key)
- `destination` (String)
- `departure_city` (String)
- `checkin_date` (String)
- `checkout_date` (String)
- `days` (Integer)
- `budget` (String)
- `preferences` (String)
- `itinerary` (Text - JSON)
- `created_at` (DateTime)

---

## 🧪 Testing

The project includes comprehensive testing:

```bash
# Run test cases
python test_phase3.py

# Test Groq API integration
python groq_json_test.py
```

### Test Coverage
- Profile system functionality
- Prompt engineering validation
- API integration testing
- Database operations
- Error handling scenarios

---

## 🔒 Security Considerations

### Implemented Security Measures
- **Password Hashing**: Using Werkzeug's security functions
- **Session Management**: Secure session handling
- **Input Validation**: Form validation and sanitization
- **SQL Injection Prevention**: Using SQLAlchemy ORM
- **XSS Protection**: Proper template escaping
- **CSRF Protection**: Form token validation

### Best Practices
- Environment variables for sensitive data
- Secure email handling
- Input sanitization
- Error handling without information disclosure
- Regular dependency updates

---

## 🚀 Deployment

### Local Development
```bash
python traveler_planer.py
```

### Production Deployment
1. Set up a production server (AWS, Heroku, DigitalOcean)
2. Configure environment variables
3. Set up a production database (PostgreSQL recommended)
4. Configure reverse proxy (Nginx)
5. Set up SSL certificates
6. Configure logging and monitoring

### Environment Variables for Production
```env
FLASK_ENV=production
SECRET_KEY=your_secure_secret_key
DATABASE_URL=your_database_url
```

---

## 📝 API Documentation

### Internal APIs

#### Travel Planning
- `POST /` - Generate travel plan
- `GET /profile` - View user profile
- `GET /plan/<id>` - View specific plan
- `POST /plan/<id>/edit` - Edit travel plan
- `POST /plan/<id>/delete` - Delete travel plan

#### Authentication
- `POST /register` - User registration
- `POST /login` - User login
- `POST /verify` - Email verification
- `POST /forgot-password` - Password reset request
- `POST /reset-password` - Password reset

#### Profile Management
- `GET /download_profile_csv` - Export profile data
- `POST /clear_profile` - Clear user profile

### External APIs Used
- **Groq API**: AI content generation
- **Tavily API**: Flight and travel information
- **Booking.com API**: Hotel data
- **Gmail SMTP**: Email delivery

---

## 🐛 Troubleshooting

### Common Issues

1. **Email not sending**
   - Check Gmail app password
   - Verify SMTP settings
   - Check firewall settings

2. **API errors**
   - Verify API keys in .env file
   - Check API rate limits
   - Validate API endpoints

3. **Database issues**
   - Ensure SQLite file permissions
   - Check database path
   - Verify schema migrations

4. **Import errors**
   - Activate virtual environment
   - Install missing dependencies
   - Check Python version compatibility

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include error handling
- Write unit tests for new features
- Update documentation.
- 
---

# 🚀 Raise Your Hack Hackathon – lablab.ai 2025


![raise your hackathon](https://github.com/user-attachments/assets/440d59c6-04c5-4c42-9886-ceccc144829b)
# 🧳 AI Travel Planner
- ![login page](https://github.com/user-attachments/assets/ac8ab04e-79c2-4922-a995-8993f8432ec6)
- ![create account](https://github.com/user-attachments/assets/11127640-b06f-491d-8aa5-e011560e1309)
- ![forgot password](https://github.com/user-attachments/assets/6440bd85-8deb-46bc-a03e-0201c2e6440d)

- ![plan trip](https://github.com/user-attachments/assets/e8ab86fa-f5ed-4ee5-80de-57c99b174241)

- ![detail](https://github.com/user-attachments/assets/66ac8dcf-c4a0-41c4-adcf-b7aff49851b4)
- ![details](https://github.com/user-attachments/assets/96605d12-9195-4a14-92be-cd2a14217c14)
- ![profile](https://github.com/user-attachments/assets/681992c4-cb01-4839-8e73-10b43d32e855)
- ![profile_details](https://github.com/user-attachments/assets/cc6decdf-2532-47ee-9bcc-eadb9b891d50)
- ![edit plan](https://github.com/user-attachments/assets/893129d4-0f7f-43f9-bcd0-308314fb7bbd)



## 🙋‍♂️ Authors & Contributors

[Ahmad gul]
[Muqaddas Akram]

### Acknowledgments
- Groq for AI model access
- Tavily for travel data
- Booking.com for hotel information
- Tailwind CSS for styling framework
- Flask community for web framework

---

## 📞 Support

- Contact: muqadasakram.13@gmail.com



## 🔄 Version History

- **v1.0.0** - Initial release with core features
- **v1.1.0** - Added profile export and management
- **v1.2.0** - Enhanced UI and responsive design
- **v1.3.0** - Added comprehensive testing suite

---

*Last updated: [8/7/2025]* 












