#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
Name     : grass
Version  : 8.3.1
Release  : 36
URL      : https://github.com/OSGeo/grass/archive/8.3.1/grass-8.3.1.tar.gz
Source0  : https://github.com/OSGeo/grass/archive/8.3.1/grass-8.3.1.tar.gz
Summary  : Multi-producer-multi-consumer signal dispatching mechanism
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC-BY-SA-3.0 GPL-2.0 GPL-2.0+ LGPL-2.1 MIT
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : buildreq-kde
BuildRequires : bzip2-dev
BuildRequires : cairo-dev
BuildRequires : fftw-dev
BuildRequires : flex
BuildRequires : freetype-dev
BuildRequires : gdal-dev
BuildRequires : geos
BuildRequires : geos-dev
BuildRequires : gfortran
BuildRequires : glu-dev
BuildRequires : libpng-dev
BuildRequires : mesa-dev
BuildRequires : netcdf
BuildRequires : netcdf-dev
BuildRequires : openblas
BuildRequires : pkgconfig(pdal)
BuildRequires : pkgconfig(x11)
BuildRequires : proj-dev
BuildRequires : pypi-wxPython
BuildRequires : sqlite-autoconf-dev
BuildRequires : tiff-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PyDispatcher is an enhanced version of Patrick K. O'Brien's
        original dispatcher.py module.  It provides the Python
        programmer with a robust mechanism for event routing within
        various application contexts.

        Included in the package are the robustapply and saferef
        modules, which provide the ability to selectively apply
        arguments to callable objects and to reference instance
        methods using weak-references.

%prep
%setup -q -n grass-8.3.1
cd %{_builddir}/grass-8.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704298488
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static --with-fftw \
--with-openmp \
--without-freetype
make  || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1704298488
rm -rf %{buildroot}
## install_prepend content
mkdir -p %{buildroot}/usr/etc
touch  %{buildroot}/usr/etc/fontcap
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/grass
cp %{_builddir}/grass-%{version}/GPL.TXT %{buildroot}/usr/share/package-licenses/grass/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/grass-%{version}/gui/icons/grass/LICENSE.TXT %{buildroot}/usr/share/package-licenses/grass/095127a16b456be28e180b85c739535e9de42ec2 || :
cp %{_builddir}/grass-%{version}/lib/external/ccmath/lgpl.license %{buildroot}/usr/share/package-licenses/grass/85b6c317814eb04c6ef5f0090037358e1be06b12 || :
cp %{_builddir}/grass-%{version}/lib/vector/dglib/COPYING %{buildroot}/usr/share/package-licenses/grass/6e3c11e241d01ccacf94f5c138f9150bd8a5b65f || :
cp %{_builddir}/grass-%{version}/mswindows/external/rbatch/COPYING %{buildroot}/usr/share/package-licenses/grass/b9e28040de9d8773c5b0cc8108869e8f3f287798 || :
cp %{_builddir}/grass-%{version}/mswindows/external/rbatch/LICENSE %{buildroot}/usr/share/package-licenses/grass/3e214f9d2536757b88a59d2d5a05f5e38d660e46 || :
cp %{_builddir}/grass-%{version}/python/grass/pydispatch/license.txt %{buildroot}/usr/share/package-licenses/grass/59d4a2706b04976b460f78fb96c232ceeb155302 || :
cp %{_builddir}/grass-%{version}/python/libgrass_interface_generator/LICENSE %{buildroot}/usr/share/package-licenses/grass/083f420d5cabd4e87c1cced4399546adf61c03bd || :
cp %{_builddir}/grass-%{version}/vector/v.lrs/LICENSE %{buildroot}/usr/share/package-licenses/grass/0dffcc72bb327ff5b4dc2158e1723f334779543b || :
%make_install prefix=%{buildroot}%{_libdir} UNIX_BIN=%{buildroot}%{_bindir} || :
## install_append content
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/include/grass/dgl
mkdir -p %{buildroot}/usr/lib64
# Copy headers.
cp -r include/* %{buildroot}/usr/include/grass/
# Copy DGLib headers.
cp lib/vector/dglib/*.h %{buildroot}/usr/include/grass/dgl/
mv %{buildroot}/usr/include/grass/dgl/dgl.h %{buildroot}/usr/include/grass/
# Copy RTree headers.
cp lib/vector/rtree/*.h %{buildroot}/usr/include/grass/
# Copy shapefil header.
cp lib/external/shapelib/shapefil.h %{buildroot}/usr/include/grass/
# Rest grass headers.
cp -a dist.x86_64-generic-linux-gnu/include/grass/*.h %{buildroot}/usr/include/grass/
# Copy Libraries.
cp dist.x86_64-generic-linux-gnu/lib/* %{buildroot}/usr/lib64
# Fixup the pc file
sed 's|/usr/grass-[0-9\.]\+/lib|/usr/lib64|g' -i grass.pc
sed 's|/usr/grass-[0-9\.]\+/include|/usr/include/grass|g' -i grass.pc
sed 's|/usr/grass-[0-9\.]\+|/usr|g' -i grass.pc
mkdir -p %{buildroot}/usr/lib64/pkgconfig
cp -a grass.pc %{buildroot}/usr/lib64/pkgconfig
## install_append end

%files
%defattr(-,root,root,-)
