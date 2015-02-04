# LaTex Tutorial/Fall Report guide

Hi again. Here's another tutorial for you guys. This time we'll learn how to use LaTeX for our tube notcher final report(s). This tutorial will cover only the basics of LaTeX. I've set up the LaTeX framework for the fall report so that you shouldn't have to go and learn too much about it on your own. If you need more information on any particular thing, however, you should start your search at the [Latex Wikibook](http://en.wikibooks.org/wiki/LaTeX). 

## Intro

LaTeX is a markup language. You write a LaTex document in any text editor, give it a `.tex` extension, and build it using a typesetter called pdfTeX, which will output a nicely formatted pdf. Since LaTeX documents can be stored as plain text, we'll be tracking them as part of our larger repository on BitBucket.

## Setup

Like Git, LaTeX has been packaged in many different ways, depending on what people need. You can work from the command line or use a GUI. The Cooper computers have various LateX setups already installed. You can also install a GUI on your own computer. This tutorial will over using the TexWorks GUI. To work on the report, just work out of the Git repo on your computer or flash drive.

### Installing TexWorks

First, install TeX Live by downloading the `.exe` [here](https://www.tug.org/texlive/acquire-netinstall.html). If you run into permission issues, use the `.zip`. 

Then, to install TexWorks, select your OS [here](http://tug.org/texworks/#Getting_TeXworks), then download and run the `.exe` file. If you're on a school computer that doesn't have TeXworks, download and extract the `.zip` folder.

## Our report  

I've outlined the fall report and started adding content. It lives in our repo in the `docs/fall-report` folder. Most of the syntax we need should be in there and ready for copying.

### File structure

Here's what the file tree of the report looks like before compiling. 

    docs/fall-report
    ├── basics.tex
    ├── bill-of-materials.tex
    ├── calculations.tex
    ├── catalog-pages.tex
    ├── catalogs -> /media/jackie/Internal Storage/Google Drive/Tube Notcher/Catalogs
    │   ├── super-precision-bearings-for-machine-tool-applications-catalog.pdf
    │   ├── timken-ball-bearings-catalog.pdf
    │   ├── timken-tapered-roller-bearing-catalog.pdf
    │   └── VPS24-1800-transformer-catalog-pages.pdf
    ├── datasheets -> /media/jackie/Internal Storage/Google Drive/Tube Notcher/Datasheets
    │   ├── DC-variator-motor-worldwide-electric-motor-manual.pdf
    │   ├── SNL1E-RC-dial-switch.pdf
    │   ├── VPS24-1800-transformer-datasheet.pdf
    │   ├── worldwide-electric-motor-wiring.pdf
    │   ├── worldwide-T1_5-18-56CB-dimensions.pdf
    │   └── worldwide-T1_5-18-56CB-spec-sheet.pdf
    ├── datasheets.tex
    ├── drawings -> /media/jackie/Internal Storage/Google Drive/Tube Notcher/Drawings
    │   └── dovetail-top.pdf
    ├── drawings.tex
    ├── fall-report.bib
    ├── fall-report.tex
    ├── fancyhdr.sty
    ├── gensymb.sty
    ├── images
    │   └── notched-tube.jpg
    ├── introduction.tex
    ├── literature -> /media/jackie/Internal Storage/Google Drive/Tube Notcher/Literature
    │   ├── chapter03_helical_gears.pdf
    │   ├── indesym.pdf
    │   └── variable-radius-notching-machine-patent.pdf
    ├── machine-description.tex
    ├── placeins.sty
    └── preface.tex

These are all the files necessary to build the report from scratch. The written part of the report consists of a few `.tex ` source files. These contain all the text and commands that make up the report itself. `fall-report.tex` is the main report file.

The `fall-report.bib` file contains bibliography entries in the BibTeX format. 

The subfolders, like `images` and `drawings` contain things like photographs and datasheets; those will be included in report when it's built. Those files live on our Google Drive because they're too big for Git to efficiently track. I use the Google Drive sync program, so those folders are available on my computer. The `->` arrows represent symbolic links; using symlinks allows me to include Google Drive folders that aren't in the Git repo. If you don't want to set this up, don't worry about it. You'll build only a partial report and I'll build the full one. If you do want to set it up, open the Windows command line, `cd` into your tube notcher Git repo, and use the `mklink` command:

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor01.png)

The `.sty` files contain some extra style information for things like headers, math symbols, and hyperlinking. Those are LaTeX add-ons that might not be installed on every computer.

Compiling the report will result in some more auxiliary files being generated. Those files won't be tracked using Git, to avoid unnecessary merge conflicts.

### Opening in TexWorks

To get a feel for what LaTeX really does, we'll take a look at each of the report files, see what they do,  and then compile the report before talking about actually editing it.

To start, open `fall-report.tex` in TeXworks. Turn on syntax coloring using `Format > Syntax Coloring > LaTeX`. 

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor03.png)

Everything before `\begin{document}` is the preamble; this section sets settings for the entire document. Everything between `\begin{document}` and `\end{document}` is the content of the report.

All of the lines with `\input{<file>.tex}` import a new chapter, written as a `.tex` file, into the main report. This allows us to separate the report into a few large chunks (one file for each chapter) instead of one huge file. Most of your work will be done in those chapter files.

If you open `basics.tex` (Chapter 1: Tube notching basics) you'll see a `\chapter{}` command followed by some actual content. 

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor04.png)

In `fall-report.bib`, you'll see one BibTeX entry for Machinery's Handbook. This entry gets cited in the Calculations chapter. 

## Compiling with TeXworks

Compiling the report takes a few steps. First, make sure you're working in the `fall-report.tex` window; running on any of the other `.tex` files won't work. Make sure `pdfLaTeX` is selected in the dropdown menu. Hit the green "Typeset" button or use `ctrl+T` to compile.

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor05.png)

If you haven't set up symlinks, it'll complain about missing files. To suppress these messages, type `R` in the command line and hit `Enter`. It'll try to run to completion.

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor06.png)

It might also ask you about corrupt `.aux` files. Don't worry, and hit `No`. 

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor07.png)

Now you'll see the pdf output. It'll be missing some things, like the Contents and Bibliography. These take multiple runs to generate, because LaTeX needs to create and read from a bunch of auxiliary files first. 

If you need to re-run, you'll see warnings like this in the bottom window: 

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor10.png)

To include the bibliography, open `fall-report.bib`, choose `BibTeX` from the dropdown, and run. 

![latex-tutor##](https://s3.amazonaws.com/tube-notcher/latex-tutorial/latex-tutor09.png)

Then, run pdfLaTeX on the main document two(ish) more times. The missing pieces should show up.


## The basics

Here, I'll briefly cover the syntax you need to know to add to the final report.

### Adding text

Easy. Just type wherever you want text. Add an extra line to start a new paragraph.

    Many framing applications require sections of round tube to be welded together. Welding tubes requires notching.

    Here are some examples of welded round tubes:
    % pictures! car frames, guide rails, etc

    Most tube notching methods are inadequate because of extensive setup time and tool cost. This machine cuts down setup time and provides variety of different notch configurations. Most importantly, the machine can cut notches of any radius in its operating range, due to its eccentric spindle mechanism.

### Sections and subsections

Using the `\section` and `\subsection` commands makes auto-numbered divisions. Even `\subsubsecction` works. If those commands are in place, then we can make a `\tableofcontents`. 

    \chapter{Machine Description}
    \section{Overview}
    \subsection{Operating ranges}
    \subsection{Overall dimensions}
    \section{Description of subsystems}
    \subsection{Structural}
    \subsection{Driveline}
    \subsection{Fixturing}
    \subsection{Electrical}
    \subsection{Safety Features}

### Including images

Let's add some images. Images can be included using relative paths. 

    \begin{figure}[htp]
        \centering
        \includegraphics[width=0.8\textwidth]{./images/notched-tube}
        \caption{A welded notched tube.}
        \label{fig:notched-tube}
    \end{figure}
	
Use the `width=` option to set the image with as a fraction of the text witdh. Use `./images/<filename>` to specify the image. You can leave off the file extension. Use `\label{<label>}` to give the image a name for cross referencing. To cross reference a figure, use `\ref{<label>}`. For example, to cross reference `notched-tube`, you'd use `See Figure~\ref{fig:notched-tube}` or a similar wording.

### Including PDFs (datasheets & catalog pages)

To include PDFs, we're using the pdfpages package. For datasheets, use this:

    \includepdf[pages=-,
                pagecommand={\thispagestyle{pdfpage}},
                scale=0.9,offset=0 -.25in,
                addtotoc={1,section,1,Transformer Datasheet,transformer-datasheet}]
                {datasheets/VPS24-1800-transformer-datasheet}
                
`Transformer Datasheet` will show up as a Table of Contents entry and a page header. `transformer-datasheet` can be used as a cross referencing label (I think). See the [package documentation](http://texdoc.net/texmf-dist/doc/latex/pdfpages/pdfpages.pdf) for more details, like how to insert only some pages.

### Including PDFs (SolidWorks drawings & electrical schematics)

For SolidWorks drawings, save the `.SLDDRW` file in the Git repo with the rest of the CAD. Save the drawing as a PDF in Google Drive. Insert it like this:

    \subsection{Dovetail stage}
    \includepdf[pages=-,
                pagecommand={\thispagestyle{pdfpage}},
                scale=0.9,offset=0 -.25in,
                landscape=true]
                {drawings/dovetail-top}
                
For part/assembly drawings, we won't make a Table of Contents entry. `landscape=true` inserts a landscape document properly. 

### Cross referencing

Anything with a label (figures, tables, sections, chapters, etc) can be cross referenced using the `\ref{}` command. Prepending things like `fig:` for figures and `tab:` for tables helps keep labels organized.

### Modular chapter files

Each chapter is in its own `.tex` file and is included in the main report with an `\input{}` command. FOr example, for the "basics" chapter, the `\chapter{Tube notching basics}` creates the pretty chapter title and the table of contents entry. The `\input{basics.tex}` includes the file.

### BibTeX (bibliography/citations)

To add a bibliography entry, see the Wikipedia [BibTeX page](http://en.wikipedia.org/wiki/BibTeX), which lists the standard entry types and what fields they require. Add entries to `fall-report.bib`.

