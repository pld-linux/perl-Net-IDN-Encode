#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IDN-Encode
Summary:	Encoding/decoding of Internationalized Domain Names (IDNs)
Summary(pl):	Kodowanie/dekodowanie miêdzynarodowych nazw domenowych (IDN)
Name:		perl-Net-IDN-Encode
Version:	0.02
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3e5925e8dc04a53fd68972d14ce3d5a8
URL:		http://search.cpan.org/dist/Net-IDN-Encode/
%if %{with tests}
BuildRequires:	perl-Net-IDN-Nameprep >= 0.02
BuildRequires:	perl-IDNA-Punycode >= 0.02
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6.0)'

%description
The "Net::IDN::Encode" module provides an easy-to-use interface for
Internationalized Domain Names (IDNs).

%description -l pl
Modu³ Net::IDN::Encode dostarcza ³atwego w u¿yciu interfejsu do
obs³ugi Miêdzynarodowych Nazw Domenowych (Internationalized Domain
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
