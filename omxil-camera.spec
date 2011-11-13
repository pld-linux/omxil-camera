Summary:	Motorola Camera video source component for Bellagio OpenMAX IL
Summary(pl.UTF-8):	Komponent źródła obrazu Motorola Camera dla implementacji Bellagio OpenMAX IL
Name:		omxil-camera
Version:	0.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/omxil/libomxcamera-%{version}.tar.gz
# Source0-md5:	01b61cf925b6240cc3345025aa4d54b9
URL:		http://omxil.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libomxil-bellagio-devel >= 0.9
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libomxil-bellagio >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/usr/%{_lib}/bellagio

%description
Motorola Camera component is a video source component for Bellagio
OpenMAX IL that uses Video4Linux2 interface. It supports preview,
video capture, image capture, video thumbnail and image thumbnail.

%description -l pl.UTF-8
Komponent Motorola Camera to komponent źródła obrazu dla implementacji
Bellagio OpenMAX IL, wykorzystujący interfejs Video4Linux2. Obsługuje
podgląd, nagrywanie filmów, przechwytywanie obrazu oraz tworzenie
miniaturek dla filmów i obrazów.

%prep
%setup -q -n libomxcamera-%{version}

%build
# rebuild for as-needed to work
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libomxcamera.so*
