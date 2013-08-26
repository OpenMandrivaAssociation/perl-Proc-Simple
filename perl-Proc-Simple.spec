%define upstream_name    Proc-Simple
%define upstream_version 1.31

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.31
Release:	1

Summary:	Launch and control background processes
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Proc/Proc-Simple-1.31.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Proc::Simple package provides objects mimicing real-life processes
from a user's point of view.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS="vendor"
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Proc
# %{perl_vendorlib}/auto/Proc

%changelog
* Tue Jun 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.280.0-1mdv2011.0
+ Revision: 687711
- update to new version 1.28

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.270.0-1mdv2011.0
+ Revision: 596011
- update to new version 1.27

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2010.0
+ Revision: 394274
- tarball has been fixed, removing hack
- update to 1.26

* Tue Jul 07 2009 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2010.0
+ Revision: 393145
- update to 1.25
- using %%perl_convert_version

* Fri Mar 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2009.1
+ Revision: 359078
- update to new version 1.24

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2009.0
+ Revision: 230279
- update to new version 1.23

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.22-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdv2008.0
+ Revision: 52526
- update to new version 1.22


* Sun Apr 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdk
- contributed by Kyle Yencer <kyle@yencer.net>


