# Geometry Dash Notepad Level Editor

*A tool you never knew you needed, and still don’t.*

Have you ever wanted to make Geometry Dash levels with a text file and like 6 objects?  
No?  
Well I don’t care!

---

## Features (the list is pretty short):

1. Like 6 objects  
2. Wait, that’s it??

This is *totally intended* so other people can add to it and maybe implement colors or layers  
(oh yeah, that also doesn’t exist).

---

## How to use:

### For non-jokesters and non-programmers:

1. [Install Python](https://www.python.org/downloads/) — make sure to check *“Add Python to PATH”* during installation  
2. Click the green **Code** button on this page and choose *“Download ZIP”*, then extract it  
3. Open the folder and double-click `level.txt`  
4. Edit the symbols to build your level (we’ll explain how below)  
5. Double-click `decoder.bat` to turn that chaos into a real Geometry Dash level  
6. Double-click `injector.bat`, follow the instructions, and paste the level code when asked  
7. Open Geometry Dash and look in your *saved levels*. Your creation awaits!

---

## Example `level.txt` Format

Use these characters in the file:

- `.` → Empty space  
- `#` → Block  
- `>` → Spike  
- `0` → Jump orb  
- `_` → Jump pad  

Each character is one grid unit. New lines = new rows.

Example:
 1,36,2,135,3,120;1,1,2,75,3,135;1,8,2,90,3,135;


 If the output from `decoder.bat` doesn’t look *vaguely* like that —  
or you just get an error...

**Figure it out. It worked on my device.**

---

## Contributing

Go wild. Add more objects. Fix my bad Python. Add support for colors or editor layers.  
Or just fork it and make it worse — I won’t stop you.

---

## License

[Unlicense](https://unlicense.org/) — do whatever you want. Really.

---

## Warning

Not responsible for corrupted save files, eye strain, or Geometry Dash existential crises.


