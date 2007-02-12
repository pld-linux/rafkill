Summary:	2D arcade-style jet fighting shooter
Summary(pl.UTF-8):	Strzelanka 2D w stylu arcade
Name:		rafkill
Version:	1.2.0
Release:	1
License:	GPL (unofficially)
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/raptorv2/raptor-%{version}.tar.gz
#Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	d6b5cddfd5fc21c5199d7d3e3089b245
Patch0:		%{name}-datadir.patch
URL:		http://raptorv2.sourceforge.net/
BuildRequires:	allegro-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dumb-devel
BuildRequires:	libstdc++-devel
Obsoletes:	raptor <= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags_ia32	 -fomit-frame-pointer 

%description
More or less a clone of a 2D vertical scroller much like Raptor: Call
of the Shadows or Tyrian.

%description -l pl.UTF-8
Mniej lub bardziej klon strzelanki 2D Raptor: Call of the Shadows lub
Tyrian.

%prep
%setup -q -n raptor-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/rafkill}

install src/raptor $RPM_BUILD_ROOT%{_bindir}
install data/* $RPM_BUILD_ROOT%{_datadir}/rafkill

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/rafkill
