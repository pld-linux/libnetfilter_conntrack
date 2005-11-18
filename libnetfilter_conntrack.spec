Summary:	A userspace library to the in-kernel connection tracking state table
Summary(pl):	Biblioteka przestrzeni u¿ytkownika do tabeli stanów ¶ledzenia po³±czeñ w j±drze
Name:		libnetfilter_conntrack
Version:	0.0.28
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	ftp://ftp.netfilter.org/pub/libnetfilter_conntrack/%{name}-%{version}.tar.bz2
# Source0-md5:	2e64ceb5625d518882c52c37721295bb
URL:		http://www.netfilter.org/projects/libnetfilter_conntrack/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnfnetlink-devel
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

%description -l pl
libnetfilter_conntrack to biblioteka przestrzeni u¿ytkownika
udostêpniaj±ca interfejs programistyczny (API) do tabeli stanów
¶ledzenia po³±czeñ w j±drze.

G³ówne mo¿liwo¶ci:
- lista/pobieranie wpisów z tabeli ¶ledzenia po³±czeñ j±dra
- wstawianie/modyfikowanie/usuwanie wpisów z tabeli ¶ledzenia po³±czeñ
  j±dra
- lista/odtwarzanie wpisów z tabeli oczekiwania j±dra
- wstawianie/modyfikowanie/usuwanie wpisów z tabeli oczekiwania j±dra

%package devel
Summary:	Header files for libnetfilter_conntrack library
Summary(pl):	Pliki nag³ówkowe biblioteki libnetfilter_conntrack
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libnfnetlink-devel

%description devel
Header files for libnetfilter_conntrack library.

%description devel -l pl
Pliki nag³ówkowe biblioteki libnetfilter_conntrack.

%package static
Summary:	Static libnetfilter_conntrack library
Summary(pl):	Statyczna biblioteka libnetfilter_conntrack
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libnetfilter_conntrack library.

%description static -l pl
Statyczna biblioteka libnetfilter_conntrack.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/nfct_proto_*-*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/%{name}/nfct_proto_*.so
%exclude %{_libdir}/%{name}/nfct_proto_*-*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
