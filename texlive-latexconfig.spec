%global tl_name latexconfig
%global tl_revision 68923

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	configuration files for LaTeX-related formats
Group:		Publishing
URL:		https://www.ctan.org/pkg/latexconfig
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latexconfig.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
configuration files for LaTeX-related formats

