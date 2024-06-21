Summary:	zlib data compression library for the next generation systems
Summary(pl.UTF-8):	Biblioteka kompresji danych zlib dla systemów nowej generacji
Name:		zlib-ng
Version:	2.1.7
Release:	1
License:	Zlib
Group:		Libraries
#Source0Download: https://github.com/zlib-ng/zlib-ng/releases
Source0:	https://github.com/zlib-ng/zlib-ng/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	3da9adadcbb1c9c842b9f81df145bb6f
URL:		https://github.com/zlib-ng/zlib-ng
BuildRequires:	cmake >= 3.5.1
BuildRequires:	gcc >= 6:4.7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zlib data compression library for the next generation systems.

%description -l pl.UTF-8
Biblioteka kompresji danych zlib dla systemów nowej generacji.

%package devel
Summary:	Header files for zlib-ng library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zlib-ng
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for zlib-ng library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zlib-ng.

%prep
%setup -q

%build
install -d build
cd build
# no ZLIB_COMPAT to get z-ng names
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include/zlib-ng \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.md PORTING.md README.md
%attr(755,root,root) %{_libdir}/libz-ng.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libz-ng.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_libdir}/libz-ng.so
%{_includedir}/zlib-ng
%{_libdir}/cmake/zlib-ng
%{_pkgconfigdir}/zlib-ng.pc
