#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Tie
%define		pnam	Config
Summary:	Tie::Config - class definitions for tied hashes config file reading
Summary(pl.UTF-8):	Tie::Config - klasa do czytania pliku konfiguracyjnego z powiązanymi haszami
Name:		perl-Tie-Config
Version:	0.04
Release:	6
License:	custom (free, Artistic-like)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46013a4e91a6cc6ba8af0bebb92373b5
URL:		http://search.cpan.org/dist/Tie-Config/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie::Config - class definitions for tied hashes config file reading.

%description -l pl.UTF-8
Tie::Config - definicje klasy do czytania pliku konfiguracyjnego z
powiązanymi haszami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Tie::Config")' Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
