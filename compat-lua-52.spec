#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : compat-lua-52
Version  : 5.2.4
Release  : 8
URL      : https://www.lua.org/ftp/lua-5.2.4.tar.gz
Source0  : https://www.lua.org/ftp/lua-5.2.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: compat-lua-52-bin = %{version}-%{release}
Requires: compat-lua-52-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Build-fixes.patch

%description
This is Lua 5.2.4, released on 25 Feb 2015.
For installation instructions, license details, and
further information about Lua, see doc/readme.html.

%package bin
Summary: bin components for the compat-lua-52 package.
Group: Binaries

%description bin
bin components for the compat-lua-52 package.


%package dev
Summary: dev components for the compat-lua-52 package.
Group: Development
Requires: compat-lua-52-bin = %{version}-%{release}
Provides: compat-lua-52-devel = %{version}-%{release}
Requires: compat-lua-52 = %{version}-%{release}

%description dev
dev components for the compat-lua-52 package.


%package man
Summary: man components for the compat-lua-52 package.
Group: Default

%description man
man components for the compat-lua-52 package.


%package staticdev
Summary: staticdev components for the compat-lua-52 package.
Group: Default
Requires: compat-lua-52-dev = %{version}-%{release}

%description staticdev
staticdev components for the compat-lua-52 package.


%prep
%setup -q -n lua-5.2.4
cd %{_builddir}/lua-5.2.4
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689829468
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  MYCFLAGS="${CFLAGS} -fpic" MYLIBS="-lncurses -lm"


%install
export SOURCE_DATE_EPOCH=1689829468
rm -rf %{buildroot}
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cp lua52.pc %{buildroot}/usr/lib64/pkgconfig/lua52.pc
mv %{buildroot}/usr/bin/lua %{buildroot}/usr/bin/lua5.2
mv %{buildroot}/usr/bin/luac %{buildroot}/usr/bin/luac5.2
mv %{buildroot}/usr/share/man/man1/lua.1 %{buildroot}/usr/share/man/man1/lua5.2.1
mv %{buildroot}/usr/share/man/man1/luac.1 %{buildroot}/usr/share/man/man1/luac5.2.1
cp src/liblua.a %{buildroot}/usr/lib64/liblua5.2.a
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lua5.2
/usr/bin/luac5.2

%files dev
%defattr(-,root,root,-)
/usr/include/lua-5.2/lauxlib.h
/usr/include/lua-5.2/lua.h
/usr/include/lua-5.2/lua.hpp
/usr/include/lua-5.2/luaconf.h
/usr/include/lua-5.2/lualib.h
/usr/lib64/pkgconfig/lua52.pc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lua5.2.1
/usr/share/man/man1/luac5.2.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/liblua5.2.a
