%define	package	lettre
%define	name	latex-%{package}
%define	version	2.346
%define	release	%mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Letters and faxes in French
License: 	LPPL
Group: 		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lettre/
Source:	 	ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/%{package}.tar.bz2
Requires: 	tetex-latex
BuildRequires:	tetex-latex
Requires(post):	tetex
Requires(postun):	tetex
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package provides a latex class for letters and faxes in French.

%prep
%setup -q -n %{package}

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/texmf/tex/latex/%{package}
install -m 644 inputs/* %{buildroot}%{_datadir}/texmf/tex/latex/%{package}

install -d -m 755 %{buildroot}%{_datadir}/texmf/doc/latex/%{package}
install -m 644 doc/* %{buildroot}%{_datadir}/texmf/doc/latex/%{package}

%clean
rm -rf %{buildroot}

%post
/usr/bin/env - /usr/bin/texhash 2>/dev/null

%postun
/usr/bin/env - /usr/bin/texhash 2>/dev/null

%files
%defattr(-,root,root)
%doc ALIRE LICENSE lppl.txt README
%{_datadir}/texmf/tex/latex/%{package}
%{_datadir}/texmf/doc/latex/%{package}

