# revision 26375
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-latexconfig
Version:	20120807
Release:	1
Summary:	TeXLive latexconfig package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexconfig.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive latexconfig package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812363
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 753161
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718817
- texlive-latexconfig
- texlive-latexconfig
- texlive-latexconfig
- texlive-latexconfig

