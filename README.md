# conky_advent
Conky widget for Advent of Code and dJulkalendern
# Screenshot
![alt text](screen.png)

# Install and run

Install within your home dir (should work in Gnome 3 at least)
```bash
sudo apt-get install conky-all
mkdir -p ~/.conky/conky_advent
git clone --depth=1 https://github.com/Schwusch/conky_advent ~/.conky/conky_advent
cp ~/.conky/conky_advent/conky.desktop ~/.config/autostart/
ln -s ~/.conky/conky_advent/advent.lua ~/.conkyrc
```

Start
```
conky -c ~/.conky/conky_advent/advent.lua
```

Stop
```
killall conky
```
