#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IDN-Encode
Summary:	Encoding/Decoding of Internationalized Domain Names (IDNs
Summary(pl):	Kodowanie/dekodowanie międzynarodowych nazw domenowych (IDN)
Name:		perl-%{pdir}-%{pnam}
Version:	0.01
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4c6ab56c32ea13278c22f96dcd63399f
URL:		http://search.cpan.org/dist/Net-IDN-Encode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6.0)'

%description
The "Net::IDN::Encode" module provides an easy-to-use interface for
Internationalized Domain Names (IDNs).

%description -l pl
Moduł Net::IDN::Encode dostarcza łatwego w użyciu interfejsu do
obsługi Międzynarodowych Nazw Domenowych (Internationalized Domain
Names [IDNs]).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README
%{perl_vendorlib}/Net/IDN/Encode.pm
%{_mandir}/man3/*
