"""
PREAMBULATORY CLAUSES

DEEPLY CONCERNED that 94% of sexual violence offenders are men and 95% of survivors do not 
report assaults to police, making sexual violence the most under-reported crime in Canada, 
with an estimated 1.8 million Albertans - 45% of Alberta's population having experienced 
sexual violence in their lifetime ("What Is Sexual Violence." Government of Alberta, 2024);

ALARMED by the fact that in Afghanistan, 64% of women reported feeling "not at all" safe 
leaving home by themselves compared to 2% of men, with 8% of surveyed women knowing at 
least one woman or girl who has attempted suicide in the last three years ("Facts and 
Figures: Ending Violence against Women." UN Women, 2024);

DISTRESSED that in Haiti, 8% of women in camps have resorted to sex work/prostitution to 
meet their needs, with an additional 20.6% reporting knowledge of at least one person who 
had done so ("Facts and Figures: Ending Violence against Women." UN Women, 2024);

GRAVELY CONCERNED that globally, 6% of women report experiencing sexual violence from 
non-partners, with actual numbers likely being significantly higher due to stigma ("Facts 
and Figures: Ending Violence against Women." UN Women, 2024);

EMPHASIZING that approximately 15 million adolescent girls worldwide, aged 15-19 years, 
have experienced forced sex, with only 1% seeking professional help based on data from 
30 countries ("Facts and Figures: Ending Violence against Women." UN Women, 2024);

OPERATIVE CLAUSES

Authors: Ved Vyas , Maarifa International Club
Functionality of code: This Flask application serves as a comprehensive platform for women's 
safety resources worldwide. Given the alarming statistics about violence against women, 
this platform aims to provide easy access to country-specific safety information, emergency 
contacts, and support resources.

Works Cited:
"Facts and Figures: Ending Violence against Women." UN Women, 2024, 
    www.unwomen.org/en/what-we-do/ending-violence-against-women/facts-and-figures.
"What Is Sexual Violence." Government of Alberta, 2024, 
    www.alberta.ca/what-is-sexual-violence.

"""

# I'm importing all the Flask goodies I need to build this app
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Setting up my Flask application instance
app = Flask(__name__)

# I'm using SQLite for my database - keeping it simple and portable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///safety.db'
db = SQLAlchemy(app)

# Here's my database model for storing country-specific information
class Country(db.Model):
    # Each country needs a unique identifier
    id = db.Column(db.Integer, primary_key=True)
    # The country's name is required - can't have blank entries!
    name = db.Column(db.String(100), nullable=False)
    # Emergency contact numbers - these are crucial for safety
    emergency_number = db.Column(db.String(20))
    police_number = db.Column(db.String(20))
    # Helpline specifically for women's issues
    womens_helpline = db.Column(db.String(50))
    # List of organizations that can help - storing as text to allow for multiple entries
    support_organizations = db.Column(db.Text)
    
# This model holds my safety resources - tips, guides, and procedures
class SafetyResource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Categories help organize different types of resources
    category = db.Column(db.String(50))
    title = db.Column(db.String(200))
    # The actual content of the resource
    content = db.Column(db.Text)
    # Linking each resource to a specific country
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

# My route to the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route to the precaution section - this is where women can learn about safety measures
@app.route('/precaution')
def precaution():
    return render_template('precaution.html')

# Route to the prevention section - this is where I educate about respecting women
@app.route('/prevention')
def prevention():
    return render_template('prevention.html')

# This route shows resources specific to each country
@app.route('/country/<country_name>')
def country_resources(country_name):
    country = Country.query.filter_by(name=country_name).first_or_404()
    return render_template('country.html', country=country)

# API endpoint to get a list of all countries in my database
@app.route('/api/countries')
def get_countries():
    countries = Country.query.all()
    return jsonify([{'name': c.name, 'id': c.id} for c in countries])

# Running my application and setting up the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
