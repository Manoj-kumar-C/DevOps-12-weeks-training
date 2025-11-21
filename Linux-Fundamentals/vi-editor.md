# VI / Vim Editor Commands Cheat Sheet

## 📝 Opening & Saving Files
- `vi filename` — Open or create a file  
- `:w` — Save  
- `:w filename` — Save as  
- `:q` — Quit  
- `:q!` — Quit without saving  
- `:wq` — Save and quit  
- `:x` — Save and quit (same as `wq`)  

---

## 🖥️ Switching Modes
- `i` — Insert mode (start typing)  
- `a` — Append after cursor  
- `I` — Insert at beginning of line  
- `A` — Append at end of line  
- `o` — Open new line below  
- `O` — Open new line above  
- `Esc` — Return to command mode  

---

## ⌨️ Navigation (Command Mode)
- `h` — Move left  
- `j` — Move down  
- `k` — Move up  
- `l` — Move right  

### Word Navigation
- `w` — Next word start  
- `b` — Previous word start  
- `e` — End of word  

### Line Navigation
- `0` — Start of line  
- `$` — End of line  

### File Navigation
- `gg` — Go to first line  
- `G` — Go to last line  
- `:10` — Go to line 10  

---

## ✂️ Deleting Text
- `x` — Delete character  
- `dd` — Delete entire line  
- `2dd` — Delete 2 lines  
- `d$` — Delete from cursor to end of line  
- `dw` — Delete word  

---

## 📋 Copy (Yank) & Paste
- `yy` — Copy (yank) line  
- `2yy` — Copy 2 lines  
- `yw` — Yank word  
- `p` — Paste below  
- `P` — Paste above  

---

## ✏️ Editing & Replacing
- `r` — Replace single character  
- `R` — Replace mode  
- `cw` — Change word  
- `cc` — Change entire line  
- `u` — Undo  
- `Ctrl + r` — Redo  

---

## 🔍 Searching & Replacing
- `/word` — Search forward  
- `?word` — Search backward  
- `n` — Next match  
- `N` — Previous match  

### Replace
- `:%s/old/new/` — Replace first occurrence in each line  
- `:%s/old/new/g` — Replace all occurrences globally  
- `:s/old/new/` — Replace in current line  

---

## 📄 Visual Mode (Selection)
- `v` — Visual mode (character selection)  
- `V` — Visual line mode  
- `Ctrl + v` — Block visual mode  
- Use `d`, `y`, `p` to delete/copy/paste on selected blocks  

---

## 🔧 Useful Commands
- `:set number` — Show line numbers  
- `:set nonumber` — Hide line numbers  
- `:syntax on` — Enable syntax highlighting  
- `:set paste` — Paste text without formatting issues  
- `:set nopaste` — Exit paste mode  

