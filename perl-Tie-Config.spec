#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Config
Summary:	Tie::Config - class definitions for tied hashes config file reading
Summary(pl):	Tie::Config - klasa do czytania pliku konfiguracyjnego z powi±zanymi haszami
Name:		perl-Tie-Config
Version:	0.04
Release:	2
License:	custom (free, Artistic-like)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::Config - class definitions for tied hashes config file reading.

%description -l pl
Tie::Config - definicje klasy do czytania pliku konfiguracyjnego z
powi±zanymi haszami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Tie::Config")' Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man3
pod2man --section=3pm Config.pm > $RPM_BUILD_ROOT%{_mandir}/man3/Tie::Config.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
