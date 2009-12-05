#
# Conditional build:
#
%define		state		unstable
%define		qt_ver		4.6.0

Summary:	Qt bindings for libindicate
Summary(pl.UTF-8):	Dowiązania Qt dla biblioteki indicate
Name:		libindicate-qt
Version:	0.2.2
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://launchpad.net/libindicate-qt/trunk/0.2.2/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	edc09ce095e7aab01b85291ce9e5f78c
URL:		http://https://launchpad.net/libindicate-qt/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtGui-devel >= %{qt_ver}
BuildRequires:	QtTest-devel >= %{qt_ver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.6.1-2
BuildRequires:	libindicate-devel >= 0.2.3
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project provides a set of Qt bindings for libindicate, the
indicator system developed by Canonical Desktop Experience team.

#%description -l pl.UTF-8

%package devel
Summary:        Header files for libindicate-qt
Summary(pl.UTF-8):      Pliki nagłówkowe biblioteki indicate-qt
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for libindicate-qt.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki indicate-qt.


%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

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
%attr(755,root,root) %ghost %{_libdir}/libindicate-qt.so.1
%attr(755,root,root) %{_libdir}/libindicate-qt.so.1.1.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/libindicate-qt
%attr(755,root,root) %{_libdir}/libindicate-qt.so
%attr(755,root,root) %{_libdir}/pkgconfig/indicate-qt.pc
