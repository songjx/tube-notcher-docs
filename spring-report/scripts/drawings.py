import os

os.chdir('..')
walk = os.walk('./Drawings')

#latex integration
latexLevels = ['\chapter','\section','\subsection','\subsubsection']

with open('drawings.tex','w') as drawings:
    for roots, dirs, files in walk:
        level = os.path.relpath(roots).count(os.sep)
        drawings.write(
            '{0}{{{1}}}\n\n'.format(latexLevels[level],os.path.basename(roots)))
        files = [os.path.basename(file) for file in files]
        for file in files:
            drawings.write('\includepdf[pages=-,\n')
            drawings.write('pagecommand={\\thispagestyle{pdfpage}},\n')
            drawings.write('scale=0.9,offset=0 -.25in,\n')
            drawings.write('landscape=true]\n')
            drawings.write('{{{}}}\n\n'.format(
                #os.path.join(os.path.relpath(roots),file).replace(os.sep,os.altsep)))
                os.path.join(os.path.relpath(roots),file)))
