Name:		texlive-plstmary
Version:	31088
Release:	2
Summary:	St. Mary's Road font support for plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/plstmary
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plstmary.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plstmary.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to produce all the symbols of the
St Mary's Road fonts, in a Plain TeX environment.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/plstmary/stmary.tex
%doc %{_texmfdistdir}/doc/plain/plstmary/README
%doc %{_texmfdistdir}/doc/plain/plstmary/plstmary-doc.pdf
%doc %{_texmfdistdir}/doc/plain/plstmary/plstmary-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
