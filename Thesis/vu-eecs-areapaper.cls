% Modified from vuthesis.sty in /opt/local/cs/lib/TeX/inputs 29 Oct 1998
% by Matt Domsch (mdomsch@vuse.vanderbilt.edu) 24 Mar 1999
% Changes:
%   - Renamed this vuthesis.cls
%   - Added dependency on LaTeX2e
%   - Conforms to 1999 Vanderbilt University Graduate School format
%     for thesis and dissertations (to the best of my knowledge)
%

% STOLEN FROM STANFORD: by Brian Carlson, Vanderbilt University
% Stanford University PhD thesis style -- modifications to the report style
% For LaTeX2e version 2e
%
% Edit Tue Sep 13 14:40:26 1988 by Joseph Pallas
% Edit Tue Thu 24 10:14:00 1999 by Matt Domsch


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{vu-eecs-areapaper}[1999/03/24 Document Class `vu-eecs-areapaper'.]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax
\LoadClass{report}
% Load the indentfirst package so that the first paragraph following a
% heading is indented (normally it's not with the report class)
\usepackage{indentfirst}
% Load float package to move figure caption to below figure
\usepackage{float}
% Load doublespace package to define spacing environment
%\usepackage{doublespace}
\usepackage{setspace}
\singlespacing

% Give lots of context when TeX finds a problem
\errorcontextlines 999

% Set the baselinestretch values for single and double spacing
% appropriate for a 12pt normal font
\newcommand{\doublespacesize}{1.66}
\newcommand{\singlespacesize}{1}
\renewcommand{\baselinestretch}{1}

% Print chapter number in roman numerals
\renewcommand{\thechapter}{\Roman{chapter}}
% Number only chapters, not sections, or subsections
\setcounter{secnumdepth}{0}
% Print chapters, sections, and subsections in the TOC
\setcounter{tocdepth}{2}
% Set the names of these areas to be what we want, all caps
\renewcommand{\contentsname}{TABLE OF CONTENTS}
\renewcommand{\listfigurename}{LIST OF FIGURES}
\renewcommand{\listtablename}{LIST OF TABLES}
\renewcommand{\bibname}{BIBLIOGRAPHY}
\renewcommand\chaptername{CHAPTER}
\renewcommand\appendixname{APPENDIX}

\def\centund#1{\begin{center}\underline{#1}\end{center}}

%make section titles bold, underlined, and 12 point, 2 blank line before, 2 after 
\renewcommand\section{\@startsection {section}{1}{\z@}{4.5ex}{0ex}{\normalsize\bfseries\centund}}
%make subsection titles bold and 12 point, 1 blank line before, 1 after 
\renewcommand\subsection{\@startsection {subsection}{2}{\z@}{4.5ex}{1ex}{\normalsize\center}}

%set spacing around floats
\floatsep 4.5ex
\intextsep 4.5ex

%set distance between footer and bottom of text
\footskip 0.5in

\long\def\comment#1{}
\comment{

  Example of use:
    \documentclass[12pt]{vuthesis}
    \begin{document}
    \title{How to Write Theses\\
            With Two Line Titles}
    \author{John Henry Candidate}
    \principaladviser{John Parker}
    \firstreader{John Green}
    \secondreader{John BigBooty\\(Another Department)}
 
    \beforepreface
    \prefacesection{Preface}
        This thesis tells you all you need to know about...
    \prefacesection{Acknowledgements}
        I would like to thank...
    \afterpreface
 
    \chapter{Introduction}
         ...
    \chapter{Conclusions}
         ...
    \appendix
    \chapter{A Long Proof}
         ...
    \bibliographystyle{plain}
    \bibliography{mybib}
    \end{document}

Documentation:
    This style file modifies the standard report style to follow the
    Graduate Program Offices's "Directions for Preparing Doctoral
    Dissertations ".  It sets the margins and interline spacing and"
    disallows page breaks at hyphens.

    The \beforepreface command creates the title page, a copyright page
    (optionally), and a signature page.  Then the user should put
    preface section(s), using the \prefacesection{section title}
    command.  The \afterpreface command then produces the tables of
    contents, tables and figures, and sets things up to start
    the main body (on arabic page 1).
    
    The following commands can control what goes in the front matter
material:
    
        \title{thesis title}
        \author{author's name}
        \dept{author's department}
                - Computer Science if omitted
        \principaladviser{the principal advisor's name}
           (or \principaladvisor, if you prefer advisor spelled with o)
        \firstreader{the first reader's name}
        \secondreader{the second reader's name}
        \submitdate{month year in which submitted to GPO}
                - date LaTeX'd if omitted
        \copyrightyear{year degree conferred (next year if submitted in Dec.)}
                - year LaTeX'd (or next year, in December) if omitted
        \copyrighttrue or \copyrightfalse
                - produce or don't produce a copyright page (true by default)
        \figurespagetrue or \figurespagefalse
                - produce or don't produce a List of Figures page
                  (true by default)
        \tablespagetrue or \tablespagefalse
                - produce or don't produce a List of Tables page
                  (true by default)

This style uses interline spacing that is 1.3 times normal, except
in the figure and table environments where normal spacing is used.
That can be changed by doing:
    \renewcommand{\baselinestretch}{1.6}
(or whatever you want instead of 1.6)
Unfortunately, that command probably won't take effect unless it comes
before the \begin{document} or after something like \small \normalsize.

The example above shows the 12pt substyle being used.  This seems to give
acceptable looking results, but it may be omitted to get smaller print.

}

\widowpenalty=10000 % don't allow widow lines
\clubpenalty=10000 % don't allow orphan lines
% Disallow page breaks at hyphens (this will give some underfull vbox's,
% so an alternative is to use \brokenpenalty=100 and manually search
% for and fix such page breaks)
\brokenpenalty=10000

% \author, \title are defined in report; here are the rest of the
% front matter defining macros
\def\dept#1{\gdef\@dept{#1}}
\def\principaladviser#1{\gdef\@principaladviser{#1}}
\def\advis@r{Adviser} % default spelling
\def\principaladvisertitle#1{\gdef\@principaladvisertitle{#1}}
\def\principaladvisor#1{\gdef\@principaladviser{#1}\gdef\advis@r{Advisor}}
\def\firstreadertitle#1{\gdef\@firstreadertitle{#1}}
\def\firstreader#1{\gdef\@firstreader{#1}}
\def\secondreadertitle#1{\gdef\@secondreadertitle{#1}}
\def\secondreader#1{\gdef\@secondreader{#1}}
\def\thirdreadertitle#1{\gdef\@thirdreadertitle{#1}}
\def\thirdreader#1{\gdef\@thirdreader{#1}}
\def\fourthreadertitle#1{\gdef\@fourthreadertitle{#1}}
\def\fourthreader#1{\gdef\@fourthreader{#1}}
\def\submitdate#1{\gdef\@submitdate{#1}}
\def\copyrightyear#1{\gdef\@copyrightyear{#1}} % \author, \title in report
\def\@title{}\def\@author{}\def\@dept{computer science}
\def\@principaladviser{}\def\@firstreader{}\def\@secondreader{}
\def\@submitdate{\ifcase\the\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space \number\the\year}

% Stanford says that December theses should have the next year as the
% copyright year
\ifnum\month=12
    \@tempcnta=\year \advance\@tempcnta by 1
    \edef\@copyrightyear{\number\the\@tempcnta}
\else
    \def\@copyrightyear{\number\the\year}
\fi
\newif\ifcopyright \newif\iffigurespage \newif\iftablespage
\copyrighttrue \figurespagetrue \tablespagetrue


\def\titlep{{%
        \thispagestyle{empty}%
        \null
        \begin{center}
                \uppercase\expandafter{\@title}\\
                \vfil
                By\\
                \vfil
                \@author\\
                \vfil
                \begin{spacing}{\doublespacesize}
                Major Area Paper and Research Proposal \\
                %Submitted to the Faculty of the \\
                Graduate School of Vanderbilt University \\
                in partial fulfillment of the requirements\\
                for the degree of\\
                \end{spacing}
                \vfil
                Doctor of Philosophy \\
                \vfil
                in  \\
                \vfil
                Electrical Engineering \\
                \vfil
                \@submitdate\\
                \vfil
                Nashville, Tennessee \\
        \end{center}
        \vfil
        \vfil
        \nobreak
        \begin{center}
        Approved: \\
        \vfil
        \@principaladvisertitle \space \@principaladviser \\
        \vfil
        \@firstreadertitle \space \@firstreader \\
        \vfil
        \@secondreadertitle \space \@secondreader \\
        \vfil
        \@thirdreadertitle \space \@thirdreader \\
        \vfil
        \@fourthreadertitle \space \@fourthreader \\
        \end{center}
        \newpage}}

\def\copyrightpage{%
        \thispagestyle{empty}
        \null\vfill
        \begin{center}
                \copyright\ Copyright by \@author \ \@copyrightyear \\
                All Rights Reserved
        \end{center}
        \vfill\newpage}


\def\beforepreface{
        \pagenumbering{roman}
        \pagestyle{plain}
        \titlep
        \ifcopyright\copyrightpage\fi
        \addtocontents{toc}{\hfill Page}
        \addtocontents{toc}{}
        }

\newcommand{\prefacesection}[1]
{
\chapter*{#1}
\addcontentsline{toc}{chapter}{\protect\uppercase{#1}}
}

\def\afterpreface{
        \newpage
        \tableofcontents
        \newpage
        \addcontentsline{toc}{chapter}{\listtablename}
        \addtocontents{lot}{Table \hfill Page}
        \addtocontents{lot}{}
        \listoftables
        \newpage
        \addcontentsline{toc}{chapter}{\listfigurename}
        \addtocontents{lof}{Figure \hfill Page}
        \addtocontents{lof}{}
        \listoffigures
        %\newpage
        \addtocontents{toc}{\protect\flushleft Chapter}
        \newpage
        \pagenumbering{arabic}
        \pagestyle{plain}
        % make rest of document (main text) double space
        \renewcommand{\baselinestretch}{\doublespacesize}\@normalsize
}
% Redefine \thebibliography to go to a new page and put an entry in the
% table of contents
\let\@ldthebibliography\thebibliography
\renewcommand{\thebibliography}[1]{\newpage
        \addcontentsline{toc}{chapter}{BIBLIOGRAPHY}
        \@ldthebibliography{#1}}


% Start out normal
\pagestyle{plain}
\renewcommand{\textfraction}{0.1}



\def\advisor#1{\gdef\@advisor{#1}}
\def\academicarea#1{\gdef\@academicarea{\uppercase{#1}}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Definition of 'abstract' page style.
%

\renewenvironment{abstract}{
              \bgroup
              \newpage
              \newcounter{savepageno}
              \setcounter{savepageno}{\value{page}}
              \thispagestyle{empty}
              \hfill\normalsize\rm\underline{\@academicarea}
              \vspace{1.5\baselineskip}
              \begin{center}
              \begin{spacing}{\doublespacesize}
                 \normalsize\uppercase\expandafter{\@title}\\
                 \vspace{1.5\baselineskip}
                 \uppercase\expandafter{\@author}
              \end{spacing}
              \end{center}
   \begin{spacing}{1}
   \centerline{\underline{Thesis under the direction of Professor \@advisor}}\par
   \vspace{\baselineskip}
   \end{spacing}
   \begin{spacing}{\doublespacesize}
}
{
   \end{spacing}
   {\vfill
   Approved\,\rule[-1mm]{2.5in}{0.4pt}\ \ Date\,\rule[-1mm]{1.5in}{0.4pt}\\
   \par\newpage\setcounter{page}{\value{savepageno}}\egroup}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Single-space quote and quotation environments
\renewenvironment{quotation}
               {\list{}{\listparindent 1.5em%
                        \itemindent    \listparindent
                        \rightmargin   \leftmargin
                        \parsep        \z@ \@plus\p@}%
                        \begin{spacing}{\singlespacesize}
                \item\relax}
               {\end{spacing}\endlist}
\renewenvironment{quote}
               {\list{}{\rightmargin\leftmargin}%
                        \begin{spacing}{\singlespacesize}
                \item\relax}
               {\end{spacing}
                \endlist}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Print the caption for a figure below the figure
% Uses package ``float''
\floatstyle{plain}
\restylefloat{figure}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Center top of page upper case large chapter and chapter* titles,
% single spaced
\def\@makechapterhead#1{%
\begin{spacing}{1}
  {\parindent \z@ \centering \normalfont
    \ifnum \c@secnumdepth >\m@ne
        \normalsize\bfseries \uppercase{\@chapapp}\space \thechapter \vspace{4.5ex}
        \par\nobreak
    \fi
    \interlinepenalty\@M
    \normalsize \bfseries \uppercase{#1}\par\nobreak
    \vskip 4.5ex
  }
\end{spacing}
}

\def\@makeschapterhead#1{%
\begin{spacing}{1}
  {\parindent \z@ \centering
    \normalfont
    \interlinepenalty\@M
    \normalsize \bfseries  \uppercase{#1}\par\nobreak
    \vskip 4.5ex
  }
\end{spacing}
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Fix up the table of contents
% Print chapter lines uppercase, with a blank line above and below
\def\l@chapter#1#2{\pagebreak[3]
 \vskip 1.0em plus 1pt % space above chapter line
 \@dottedtocline{0}{0em}{4em}{\uppercase{#1}}{#2}
 \vskip 0.25em plus 1pt % space below chapter line
}

% Print sub-chapter lines indented appropriately
\renewcommand\l@section{\@dottedtocline{1}{5.5em}{2.4em}}
\renewcommand\l@subsection{\@dottedtocline{2}{8.5em}{3.2em}}
\renewcommand\l@subsubsection{\@dottedtocline{3}{11em}{4.1em}}
\renewcommand\l@paragraph{\@dottedtocline{4}{13.5em}{5em}}
\renewcommand\l@subparagraph{\@dottedtocline{5}{16em}{6em}}

% Put a blank line above figure and table entries in their lists
\renewcommand{\l@figure}{
 \vskip 1.0em plus 1pt % space above figure name
 \@dottedtocline{1}{1.5em}{3.3em}
}
\renewcommand{\l@table}{\l@figure}

% Put a period after the item number in the table of contents
\def\numberline#1{\hb@xt@\@tempdima{{#1.}\hfil}}

% Redefine \appendix to put an entry in the table of contents
\let\@ldappendix\appendix
\renewcommand{\appendix}{
        \@ldappendix
        \addtocontents{toc}{\protect\flushleft Appendix}}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%