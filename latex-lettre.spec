Name: 		latex-lettre
Version: 	2.346
Release: 	3
Summary: 	Letters and faxes in French
License: 	LPPL
Group: 		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lettre/
Source0: 	ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/lettre.tar.bz2
Requires: 	texlive-latex texlive-collection-latex
BuildRequires:	texlive-latex texlive-collection-latex
BuildArch:	noarch

%description
This package provides a latex class for letters and faxes in French.

%prep
%setup -q -n lettre

%build

%install
install -d -m 755 %{buildroot}%{_datadir}/texmf/tex/latex/lettre
install -m 644 inputs/* %{buildroot}%{_datadir}/texmf/tex/latex/lettre

install -d -m 755 %{buildroot}%{_datadir}/texmf/doc/latex/lettre
install -m 644 doc/* %{buildroot}%{_datadir}/texmf/doc/latex/lettre

%post -p %_bindir/texhash

%postun -p %_bindir/texhash

%files
%defattr(-,root,root)
%doc ALIRE LICENSE lppl.txt README
%{_datadir}/texmf/tex/latex/lettre
%{_datadir}/texmf/doc/latex/lettre

%changelog
* Tue Jun 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.346-1mdv2007.0
- first mdv package
