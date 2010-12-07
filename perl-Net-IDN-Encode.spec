#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	IDN-Encode
Summary:	Encoding/decoding of Internationalized Domain Names (IDNs)
Summary(pl.UTF-8):	Kodowanie/dekodowanie międzynarodowych nazw domenowych (IDN)
Name:		perl-Net-IDN-Encode
Version:	1.100
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/CFAERBER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a90b0d9bcc7886c0f7214df94bfa62f
URL:		http://search.cpan.org/dist/Net-IDN-Encode/
%if %{with tests}
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Net-IDN-Nameprep >= 1.100
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The "Net::IDN::Encode" module provides an easy-to-use interface for
Internationalized Domain Names (IDNs).

%description -l pl.UTF-8
Moduł Net::IDN::Encode dostarcza łatwego w użyciu interfejsu do
obsługi Międzynarodowych Nazw Domenowych (Internationalized Domain
Names - IDN).

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
%{perl_vendorlib}/Net/IDN/Punycode.pm
%{perl_vendorlib}/Net/IDN/Punycode.xs
%{perl_vendorlib}/Net/IDN/Punycode
%{_mandir}/man3/Net::IDN::Encode.3pm*
%{_mandir}/man3/Net::IDN::Punycode*.3pm*
