Summary:	A userspace library to the in-kernel connection tracking state table
Summary(pl.UTF-8):	Biblioteka przestrzeni użytkownika do tabeli stanów śledzenia połączeń w jądrze
Name:		libnetfilter_conntrack
Version:	0.0.99
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.netfilter.org/projects/libnetfilter_conntrack/files/%{name}-%{version}.tar.bz2
# Source0-md5:	960c3d347d7f4e3fe7437aa198f36e6e
URL:		http://www.netfilter.org/projects/libnetfilter_conntrack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnfnetlink-devel >= 0.0.39
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	libnfnetlink >= 0.0.39
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libnetfilter_conntrack is a userspace library providing a programming
interface (API) to the in-kernel connection tracking state table.

Main features:
- listing/retrieving entries from the kernel connection tracking table
- inserting/modifying/deleting entries from the kernel connection
  tracking table
- listing/retrieving entries from the kernel expect table
- inserting/modifying/deleting entries from the kernel expect table

%description -l pl.UTF-8
libnetfilter_conntrack to biblioteka przestrzeni użytkownika
udostępniająca interfejs programistyczny (API) do tabeli stanów
śledzenia połączeń w jądrze.

Główne możliwości:
- lista/pobieranie wpisów z tabeli śledzenia połączeń jądra
- wstawianie/modyfikowanie/usuwanie wpisów z tabeli śledzenia połączeń
  jądra
- lista/odtwarzanie wpisów z tabeli oczekiwania jądra
- wstawianie/modyfikowanie/usuwanie wpisów z tabeli oczekiwania jądra

%package devel
Summary:	Header files for libnetfilter_conntrack library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libnetfilter_conntrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnfnetlink-devel >= 0.0.39

%description devel
Header files for libnetfilter_conntrack library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libnetfilter_conntrack.

%package static
Summary:	Static libnetfilter_conntrack library
Summary(pl.UTF-8):	Statyczna biblioteka libnetfilter_conntrack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_conntrack library.

%description static -l pl.UTF-8
Statyczna biblioteka libnetfilter_conntrack.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_conntrack.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetfilter_conntrack.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetfilter_conntrack.so
%{_libdir}/libnetfilter_conntrack.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetfilter_conntrack.a
