%define upstream_name    Dist-Zilla-Plugin-MatchManifest
%define upstream_version 4.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Ensure that MANIFEST is correct
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Throwable)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl(Role::HasMessage)
BuildRequires:	perl(Role::Identifiable::HasIdent)
BuildRequires:	perl(autodie)
BuildRequires:	perl(MooseX::OneArgNew)
BuildRequires:	perl(Test::Fatal)

BuildArch:	noarch

%description
If included, this plugin will ensure that the distribution contains a
_MANIFEST_ file and that its contents match the files collected by
Dist::Zilla. If not, it will display the differences and (if STDIN & STDOUT
are TTYs) offer to update the _MANIFEST_.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


