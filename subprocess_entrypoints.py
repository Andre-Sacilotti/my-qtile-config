import subprocess

def background_entrypoint():
    
    subprocess.call(['xsetroot',
                    '-cursor_name', 'left_prt',
                    '-solid', '#000000'])
    
    subprocess.call(['nitrogen', '--no-recurse', './resources/wallpaper.jpg'])