Name:		texlive-latexconfig
Version:	20111102
Release:	1
Summary:	TeXLive latexconfig package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexconfig.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive latexconfig package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/latexconfig/color.cfg
%{_texmfdistdir}/tex/latex/latexconfig/dvilualatex.ini
%{_texmfdistdir}/tex/latex/latexconfig/epstopdf-sys.cfg
%{_texmfdistdir}/tex/latex/latexconfig/graphics.cfg
%{_texmfdistdir}/tex/latex/latexconfig/hyperref.cfg
%{_texmfdistdir}/tex/latex/latexconfig/latex.ini
%{_texmfdistdir}/tex/latex/latexconfig/lualatex-patch-kernel.tex
%{_texmfdistdir}/tex/latex/latexconfig/lualatex-reset-codes.tex
%{_texmfdistdir}/tex/latex/latexconfig/lualatex.ini
%{_texmfdistdir}/tex/latex/latexconfig/lualatexiniconfig.tex
%{_texmfdistdir}/tex/latex/latexconfig/lualatexquotejobname.lua
%{_texmfdistdir}/tex/latex/latexconfig/lualatexquotejobname.tex
%{_texmfdistdir}/tex/latex/latexconfig/mllatex.ini
%{_texmfdistdir}/tex/latex/latexconfig/pdflatex.ini
%{_texmfdistdir}/tex/latex/latexconfig/xelatex.ini

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
