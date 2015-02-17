import os

os.chdir('..')
walk = os.walk('./drawings')

#latex integration
latexLevels = ['\chapter','\section','\subsection','\subsubsection']

for roots, dirs, files in walk:
    level = os.path.relpath(roots).count(os.sep)
    print(latexLevels[level],'{',os.path.basename(roots),'}',sep='')
    files = [os.path.splitext(file)[0] for file in files]
    #print('files:',files)
    for file in files:
        print('\n\includepdf[pages=-,')
        print('pagecommand={\\thispagestyle{pdfpage}},')
        print('scale=0.9,offset=0 -.25in,')
        print('landscape=true]')
        print('{',os.path.join(os.path.relpath(roots),file),'}',sep='')
    print('\n%---\n')
