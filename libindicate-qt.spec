#
# Conditional build:
#
%define		state		unstable
%define		qt_ver		4.6.0

Summary:	Qt bindings for libindicate
Summary(pl.UTF-8):	Dowiązania Qt dla biblioteki indicate
Name:		libindicate-qt
Version:	0.2.5.91
Release:	1
License:	LGPL v2.1 or LGPL v3
Group:		X11/Libraries
Source0:	https://launchpad.net/libindicate-qt/libindicate-0.5/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	67e474d55c8ab0d7d2fd3f9da651eba3
Patch0:		%{name}-build.patch
URL:		https://launchpad.net/libindicate-qt/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	libindicate-devel >= 12.0.0
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	QtCore >= %{qt_ver}
Requires:	QtGui >= %{qt_ver}
Requires:	libindicate >= 12.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides a set of Qt bindings for libindicate, the
indicator system developed by Canonical Desktop Experience team.

%description -l pl.UTF-8
Ten pakiet dostarcza wiązania Qt do libindicate - systemu kontrolek
stworzonego przez zespół Canonical Desktop Experience.

%package devel
Summary:        Header files for libindicate-qt library
Summary(pl.UTF-8):      Pliki nagłówkowe biblioteki indicate-qt
Group:          X11/Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qt_ver}

%description devel
Header files for libindicate-qt library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki indicate-qt.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_libdir}/libindicate-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libindicate-qt.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libindicate-qt.so
%{_includedir}/libindicate-qt
%{_pkgconfigdir}/indicate-qt.pc
