%define upstream_name 	 Tk-TableMatrix
%define upstream_version 1.23

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Tk-TableMatrix perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://cpan.org/authors/id/C/CE/CERNEY/%{upstream_name}-%{upstream_version}.tar.bz2

# for fake X display:
BuildRequires:	perl-Tk-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(x11)
Obsoletes:	%{name}-devel < %version-%release
Provides:	%{name}-devel = %version-%release

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Tk::TableMatrix is a table/matrix widget extension to perl/tk
for displaying data in a table (or spreadsheet) format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# DISABLE the check for now. It's won't work with build bots. 20061104.SE
#XDISPLAY=$(i=2; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
#{_prefix}/X11R6/bin/Xvfb :$XDISPLAY &
#export DISPLAY=:$XDISPLAY
#xauth add $DISPLAY . EE
#{__make} test

#xauth remove $DISPLAY
#kill $(cat /tmp/.X$XDISPLAY-lock)

%install
rm -rf %{buildroot}
%makeinstall_std

# 20070818 remove file owned by perl-Tk-804.027-7mdv2007.0.i586
rm -rf %{buildroot}/%{perl_vendorarch}/Tk/pTk/extralibs.ld

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Tk
%{perl_vendorarch}/auto/Tk
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.230.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Feb 07 2011 Funda Wang <fwang@mandriva.org> 1.230.0-2
+ Revision: 636514
- no need to provide additional devel package

* Wed Jul 21 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2011.0
+ Revision: 556327
- update buildrequires:

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2010.0
+ Revision: 401502
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.23-6mdv2009.0
+ Revision: 258658
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.23-5mdv2009.0
+ Revision: 246655
- rebuild

* Mon Feb 04 2008 Jérôme Quelin <jquelin@mandriva.org> 1.23-3mdv2008.1
+ Revision: 162067
- forcing rebuild with new perl 5.10

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Aug 18 2007 Stefan van der Eijk <stefan@mandriva.org> 1.23-1mdv2008.0
+ Revision: 65426
- remove file owned by perl-Tk


* Thu Feb 01 2007 Stefan van der Eijk <stefan@mandriva.org> 1.23-1mdv2007.0
+ Revision: 115815
- 1.23

* Sat Nov 04 2006 Stefan van der Eijk <stefan@mandriva.org> 1.22-2mdv2007.1
+ Revision: 76554
- DISABLE the check for now. It's won't work with build bots.
- Import perl-Tk-TableMatrix

* Tue Mar 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.22-1mdk
- New release 1.22

* Wed Mar 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.21-1mdk
- New release 1.21
- spec cleanup
- fix directory ownership"

* Mon Dec 26 2005 Stefan van der Eijk <stefan@eijk.nu> 1.2-1mdk
- 1.2
- %%mkrel

* Mon Nov 29 2004 Stefan van der Eijk <stefan@mandrake.org> 1.1-2mdk
- rebuild for new perl

* Thu Jul 22 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.1-1mdk
- 1.1

