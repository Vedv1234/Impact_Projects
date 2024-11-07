# 3D Carrot Visualization Project 🥕

## Overview
Hey there! Welcome to my 3D Carrot project. This is a fun Python program that creates a rotating 3D carrot using OpenGL. I made this to practice 3D graphics programming and because, well, who doesn't love carrots?

## Features
- 🌟 Realistic 3D carrot model
- 🔄 Smooth rotation animation
- 🎮 Interactive controls
- 🌿 Detailed leaves and texture
- 🎨 Custom coloring and shading

## Prerequisites
Before you run this awesome carrot, you'll need:
1. Python 3.x
2. PyGame library
3. PyOpenGL library

## Installation
1. First, make sure you have Python installed. If not, download it from [python.org](https://python.org)

2. Install the required libraries using pip:
```bash
pip install pygame
pip install pyopengl
pip install pyopengl-accelerate
```

3. Download the carrot.py file

4. Run it:
```bash
python carrot.py
```

## How to Use
Once you start the program, you'll see a rotating 3D carrot. Here's how to control it:

- ⬆️ Up Arrow: Rotate up
- ⬇️ Down Arrow: Rotate down
- ⬅️ Left Arrow: Rotate left
- ➡️ Right Arrow: Rotate right
- ❌ Close window to exit

## How It Works
The carrot is built using several components:
1. **Body**: A cone-shaped structure with orange gradient
2. **Texture**: Lines running down the body
3. **Leaves**: Multiple triangular shapes in a crown formation
4. **Animation**: Continuous rotation with user control

## Code Structure
```
carrot.py
├── draw_carrot_body()   # Creates the main orange part
├── draw_leaf()          # Draws individual leaves
├── draw_leaves()        # Arranges leaves in a circle
├── draw_carrot()        # Combines all components
└── main()              # Handles display and interaction
```

## Troubleshooting
If you're seeing a black screen:
1. Update your graphics drivers
2. Verify PyOpenGL installation
3. Try running in a different Python environment

If the carrot is invisible:
1. Check if OpenGL is properly initialized
2. Ensure all dependencies are correctly installed
3. Try adjusting the viewing distance in the code

## Future Improvements
I'm planning to add:
- [ ] More realistic texturing
- [ ] Shadow effects
- [ ] Different carrot varieties
- [ ] Size customization
- [ ] Export as 3D model

## Contributing
Feel free to fork this project and make your own veggie variations! If you've got ideas for making this carrot even better, here's how you can contribute:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License
This project is open source - feel free to use it, just remember to credit me if you do something cool with it!

## Contact
Got questions about my carrot? Feel free to reach out!
- Created by: Ved Vyas
- GitHub: Vedv1234

## Acknowledgments
- Thanks to the PyGame and PyOpenGL communities
- Inspired by real carrots 🥕
- Special thanks to anyone who believes vegetables can be fun coding projects!

---
Made with 🥕 by Ved Vyas