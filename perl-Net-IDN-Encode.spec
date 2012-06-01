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
Version:	2.003
Release:	1
# "same as perl"
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e5832ea0d3f5e4997e0361a1951f569
URL:		http://search.cpan.org/dist/Net-IDN-Encode/
%if %{with tests}
BuildRequires:	perl-ExtUtils-CBuilder
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Unicode-Normalize
%endif
BuildRequires:	perl-devel >= 1:5.8.5
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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Net/IDN/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/IDN/Encode.pm
%{perl_vendorlib}/Net/IDN/Punycode.pm
%{perl_vendorlib}/Net/IDN/Punycode.xs
%{perl_vendorlib}/Net/IDN/Punycode
%{perl_vendorlib}/Net/IDN/UTS46.pm
%{perl_vendorlib}/Net/IDN/UTS46
%{_mandir}/man3/Net::IDN::Encode.3pm*
%{_mandir}/man3/Net::IDN::Overview.3pm*
%{_mandir}/man3/Net::IDN::Punycode*.3pm*
%{_mandir}/man3/Net::IDN::Standards.3pm*
%{_mandir}/man3/Net::IDN::UTS46*.3pm*
