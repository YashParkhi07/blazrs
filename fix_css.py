css_file = 'styles.css'
with open(css_file, 'r') as f:
    lines = f.readlines()

# Find where /* FLASHCARDS */ is
idx = -1
for i, line in enumerate(lines):
    if "/* FLASHCARDS */" in line:
        idx = i
        break

if idx != -1:
    lines = lines[:idx]

new_css = """
/* DIALOG MODAL */
.cloud-dialog {
  padding: 32px;
  background-color: var(--panel);
  border: 1px solid var(--cyan);
  border-radius: 12px;
  color: var(--paper);
  max-width: 500px;
  width: 90%;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  margin: auto;
}

.cloud-dialog::backdrop {
  background: rgba(10, 10, 15, 0.85);
  backdrop-filter: blur(4px);
}

.cloud-dialog .dialog-content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.cloud-dialog h3 {
  color: var(--cyan);
  font-size: 24px;
  font-weight: 600;
  margin: 0;
}

.cloud-dialog p {
  color: var(--grey);
  font-size: 15px;
  line-height: 1.6;
  margin: 0;
}

.cloud-dialog button {
  align-self: flex-end;
  background-color: transparent;
  color: var(--paper);
  border: 1px solid var(--line);
  padding: 8px 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 8px;
}

.cloud-dialog button:hover {
  border-color: var(--cyan);
  color: var(--cyan);
}
"""

lines.append(new_css)

with open(css_file, 'w') as f:
    f.writelines(lines)
