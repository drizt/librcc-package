Name:           librcc
Version:        0.2.9
Release:        2%{?dist}
Summary:        RusXMMS Charset Conversion Library

License:        LGPLv2+
URL:            http://rusxmms.sourceforge.net
Group:          System Environment/Libraries
Source0:        http://downloads.sourceforge.net/rusxmms/%{name}-%{version}.tar.bz2
# To fix building against new version of glib
Patch0:         %{name}-glib2-2.32.0.patch
# To fix a compilation warning
Patch1:         %{name}-rccstring.patch

BuildRequires:  libxml2-devel
BuildRequires:  enca-devel
BuildRequires:  gtk2-devel
BuildRequires:  aspell-devel

%description
The Abilities of LibRCC Library

- Language Autodetection.
- On the fly translation between languages, using online-services!
- Encoding Autodetection for most of European Languages.
- Support for encoding detection plugins (besides Enca and LibRCD)
- Recoding/translation of multi-language playlists!
- Cache to speed-up re-recoding.
- Possibility to configure new languages and encodings.
- Shared configuration file. For example mentioned TagLib and LibID3
  patches do not have their own user interface, but will utilize the
  same recoding configuration as XMMS.
- As well the separate program for configuration adjustment is
  available.
- GTK2 UI Library: you can add properties page to your GTK application
  with 3 lines of code.
- Menu localization opportunity.


%package        gtk2
Summary:        RusXMMS Encoding Conversion Library GTK2 bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Group:          System Environment/Libraries

%description    gtk2
The %{name}-devel package contains GTK2 bindings for RusXMMS Encoding
Conversion Library

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk2%{?_isa} = %{version}-%{release}
Group:          Development/Libraries

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

# fix permissions
chmod 644 examples/rusxmms_cache.pl

%build
%configure --disable-static --disable-libtranslate --disable-bdb
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post gtk2 -p /sbin/ldconfig

%postun gtk2 -p /sbin/ldconfig


%files
%doc COPYING NEWS AUTHORS README
%{_libdir}/librcc.so.*
%{_libdir}/librccui.so.*
%{_libdir}/rcc


%files gtk2
%{_libdir}/librccgtk2.so.*

%files devel
%doc examples
%{_includedir}/librcc*.h
%{_libdir}/librcc.so
%{_libdir}/librccui.so
%{_libdir}/librccgtk2.so

%changelog
* Fri Nov  2 2012 Ivan Romanov <drizt@land.ru> - 0.2.9-1
- corrected Source0
- add patch1
- explicity turn off libtranslate and db4 support
- added aspell to BR

* Mon Oct 29 2012 Ivan Romanov <drizt@land.ru> - 0.2.9-1
- initial version of package
