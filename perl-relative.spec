#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	relative
Summary:	relative - Load modules with relative names
Name:		perl-relative
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://search.cpan.org/dist/relative/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SAPER/%{pdir}-%{version}.tar.gz
# Source0-md5:  923b48653599f2f7fcc7eba12db462ea
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to load modules using only parts of their name,
relatively to the current module or to a given module. Module names
are by default searched below the current module, but can be searched
upper in the hierarchy using the ..:: syntax.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/relative.pm
%{_mandir}/man3/*
