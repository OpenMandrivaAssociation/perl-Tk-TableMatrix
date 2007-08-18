%define module 	Tk-TableMatrix
%define name 	perl-%{module}
%define version 1.23
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:	Tk-TableMatrix perl module
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://cpan.org/authors/id/C/CE/CERNEY/%{module}-%{version}.tar.bz2
# for fake X display:
BuildRequires:	XFree86-Xvfb
BuildRequires:	XFree86-devel
BuildRequires:	perl-devel
BuildRequires:	perl-Tk-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
Tk::TableMatrix is a table/matrix widget extension to perl/tk
for displaying data in a table (or spreadsheet) format.

%package devel
Summary:	Tk::TableMatrix modules for Perl (development package)
Group:		Development/C
Requires:	%{name} = %{version}

%description devel
Tk::TableMatrix is a table/matrix widget extension to perl/tk
for displaying data in a table (or spreadsheet) format.

This is the development package.

%prep
%setup -q -n %{module}-%{version}

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

%files devel
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Tk


