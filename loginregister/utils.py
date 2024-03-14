#definiciones para sign

def on_enter(e, default_text):
    entry = e.widget
    if entry.get() == default_text:
        entry.delete(0, 'end')

def on_leave(e, default_text):
    entry = e.widget
    if entry.get() == '':
        entry.insert(0, default_text)