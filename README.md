## 📃 Table of Contents
- [⚙ Steel Warriors](#-steel-warriors)
  - [🕹 Features](#-features)
  - [🎮 Controls](#-controls)
  - [📥 Installation](#-installation)
  - [🎯 Todos](#-todos)
  - [🤝 Contributing](#-contributing)
  - [💖 Supporting](#-supporting)
  - [📚 Resources](#-resources)
  - [🎨 Artwork](#-artwork)
  - [📜 License](#-license)

# ⚙ Steel Warriors

Top down shooter game created with Python Arcade library. In this game, player controls a tank and must defeat waves of enemy tanks while avoiding missles and collecting power ups.

![Demo](/demo_gameplay.gif)


## 🕹 Features

- The game consists of only one level 
- Map is generated with **WFC algorithm**
- Enemy tanks have different hitpoints and fire rates
- Must defeat all tanks before they invade the border
- Gamover conditions:
  - if one enemy escapes
  - if player runs out of lives
  - if collision with enemy

## 🎮 Controls

- Use **LEFT**|**RIGHT**|**UP**|**DOWN** arrows to move the tank
- Press **SPACE** to shoot
- Press **P** to pause; **R** to restart
- Press **G** to generate new map

## 📥 Installation

To play this game, you will need to have Python 3.10+ installed on your computer. Once you have cloned this repo, install the necessary dependencies using `pip install -r requirements.txt`. Then, you can run the game with `python -m game`.

## 🎯 Todos

- [ ] Add levels and highscore
- [ ] Obstacles
- [ ] Sound effects
- [ ] Power ups

## 🤝 Contributing

If you have any ideas for new features or improvements to the game, please submit a PR or reach out to me. I'd love to hear from you.

## 💖 Supporting

If you like this project, please consider giving this repo a ⭐. It only takes a second and means a lot to me.

## 📚 Resources

- [Arcade Library](https://arcade.academy/)
- [RealPython Tutorial](https://realpython.com/arcade-python-game-framework/)
- [WFC map generation](https://github.com/IndieCoderMM/algo-lab/tree/master/Map-generator)

## 🎨 Artwork

- [Top-down tanks package](https://www.kenney.nl/assets/topdown-tanks-redux)

## 📜 License

This project is licensed under the [MIT License](./LICENSE).