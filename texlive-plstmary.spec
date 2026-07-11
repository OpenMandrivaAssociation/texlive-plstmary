%global tl_name plstmary
%global tl_revision 31088

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5c
Release:	%{tl_revision}.1
Summary:	St. Marys Road font support for plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/plstmary
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plstmary.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/plstmary.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to produce all the symbols of the St
Mary's Road fonts, in a Plain TeX environment.

