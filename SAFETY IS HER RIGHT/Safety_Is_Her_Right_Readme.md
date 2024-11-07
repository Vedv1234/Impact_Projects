# Women's Safety Global Resource Platform

## PREAMBULATORY CLAUSES

DEEPLY CONCERNED that 94% of sexual violence offenders are men and 95% of survivors do not report assaults to police, making sexual violence the most under-reported crime in Canada, with an estimated 1.8 million Albertans - 45% of Alberta's population having experienced sexual violence in their lifetime ("What Is Sexual Violence." Government of Alberta, 2024);

ALARMED by the fact that in Afghanistan, 64% of women reported feeling "not at all" safe leaving home by themselves compared to 2% of men, with 8% of surveyed women knowing at least one woman or girl who has attempted suicide in the last three years ("Facts and Figures: Ending Violence against Women." UN Women, 2024);

DISTRESSED that in Haiti, 8% of women in camps have resorted to sex work/prostitution to meet their needs, with an additional 20.6% reporting knowledge of at least one person who had done so ("Facts and Figures: Ending Violence against Women." UN Women, 2024);

GRAVELY CONCERNED that globally, 6% of women report experiencing sexual violence from non-partners, with actual numbers likely being significantly higher due to stigma ("Facts and Figures: Ending Violence against Women." UN Women, 2024);

EMPHASIZING that approximately 15 million adolescent girls worldwide, aged 15-19 years, have experienced forced sex, with only 1% seeking professional help based on data from 30 countries ("Facts and Figures: Ending Violence against Women." UN Women, 2024);

## Project Overview
This open-source platform aims to provide comprehensive safety resources and information for women worldwide. The project consists of two main modules:
- **Precaution**: Resources and information for women about available safety measures
- **Prevention**: Educational content focusing on respect, dignity, and appropriate behavior

## Features
- Country-specific safety resources
- Emergency contact information
- Legal resources and guidance
- Support organization directories
- Mobile-responsive design
- Multi-language support (planned)

## Technical Stack
- Backend: Python/Flask
- Database: SQLite
- Frontend: HTML5, CSS3
- Deployment: Docker support planned

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/womens-safety-platform.git
cd womens-safety-platform

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask db upgrade

# Run the application
flask run
```

## Project Structure
```
women_safety/
├── app.py                 # Main Flask application
├── requirements.txt       # Project dependencies
├── static/               # Static files
│   └── css/
│       └── style.css     # Custom styling
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── precaution.html
│   └── prevention.html
└── instance/             # Instance-specific files
    └── safety.db         # SQLite database
```

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Works Cited
"Facts and Figures: Ending Violence against Women." UN Women, 2024, 
    www.unwomen.org/en/what-we-do/ending-violence-against-women/facts-and-figures.

"What Is Sexual Violence." Government of Alberta, 2024, 
    www.alberta.ca/what-is-sexual-violence.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
- UN Women for comprehensive statistics and research
- Government of Alberta for regional statistics
- All contributors and supporters of women's safety initiatives worldwide