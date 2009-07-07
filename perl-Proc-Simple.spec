%define upstream_name    Proc-Simple
%define upstream_version 1.25

Name:    perl-%{upstream_name}
Version: %perl_convert_version %{upstream_version}
Release: %mkrel 1

Summary: Launch and control background processes
License: Artistic
Group:   Development/Perl
Url:     http://search.cpan.org/dist/%{upstream_name}
Source0: http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tgz

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The Proc::Simple package provides objects mimicing real-life processes
from a user's point of view.

%prep
%define extract_dir %( tar ztvf %{_topdir}/SOURCES/%{upstream_name}-%{upstream_version}.tgz | head -1 | awk '{print $NF}' )
%setup -q -n %{extract_dir}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor"
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Proc
%{perl_vendorlib}/auto/Proc

