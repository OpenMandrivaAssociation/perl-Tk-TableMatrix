%define upstream_name 	 Tk-TableMatrix
%define upstream_version 1.23

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 2

Summary:	Tk-TableMatrix perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://cpan.org/authors/id/C/CE/CERNEY/%{upstream_name}-%{upstream_version}.tar.bz2

# for fake X display:
BuildRequires:	perl-Tk-devel
BuildRequires:	perl-devel
BuildRequires:	libx11-devel
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
