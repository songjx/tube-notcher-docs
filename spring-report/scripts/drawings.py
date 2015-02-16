import os

os.chdir('..')
walk = os.walk('./drawings')

#latex integration
latexLevels = ['chapter','section','subsection','subsubsection']

for roots, dirs, files in walk:
    level = os.path.relpath(roots).count(os.sep)
    #print('root:', os.path.relpath(roots), '(level', level, ')')
    print('heading:',latexLevels[level],os.path.basename(roots))
    files = [os.path.splitext(file)[0] for file in files]
    print('files:',files)
    print('---')
