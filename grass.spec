#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grass
Version  : 7.4.3
Release  : 1
URL      : https://grass.osgeo.org/grass74/source/grass-7.4.3.tar.gz
Source0  : https://grass.osgeo.org/grass74/source/grass-7.4.3.tar.gz
Summary  : Multi-producer-multi-consumer signal dispatching mechanism
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ LGPL-2.1 MIT
BuildRequires : bison
BuildRequires : buildreq-distutils3
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
BuildRequires : netcdf-dev
BuildRequires : openblas
BuildRequires : pkgconfig(x11)
BuildRequires : proj-dev
BuildRequires : sqlite-autoconf-dev
BuildRequires : tiff-dev

%description
GRASS (Geographic Resources Analysis Support System) is a Geographic
Information System (GIS) used for geospatial data management and
analysis, image processing, graphics/maps production, spatial
modeling, and visualization. GRASS is currently used in academic and
commercial settings around the world, as well as by many governmental
agencies and environmental consulting companies.

%package dev
Summary: dev components for the grass package.
Group: Development
Provides: grass-devel = %{version}-%{release}

%description dev
dev components for the grass package.


%prep
%setup -q -n grass-7.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545342133
export CFLAGS="$CFLAGS  "
export FCFLAGS="$CFLAGS  "
export FFLAGS="$CFLAGS  "
export CXXFLAGS="$CXXFLAGS  -std=gnu++98"
%configure --disable-static --with-fftw \
--with-openmp \
--without-freetype
make || :

%install
export SOURCE_DATE_EPOCH=1545342133
rm -rf %{buildroot}
## install_prepend content
mkdir -p %{buildroot}/usr/etc
touch  %{buildroot}/usr/etc/fontcap
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/grass
cp GPL.TXT %{buildroot}/usr/share/package-licenses/grass/GPL.TXT
cp lib/external/ccmath/lgpl.license %{buildroot}/usr/share/package-licenses/grass/lib_external_ccmath_lgpl.license
cp lib/python/ctypes/ctypesgencore/LICENSE %{buildroot}/usr/share/package-licenses/grass/lib_python_ctypes_ctypesgencore_LICENSE
cp lib/python/pydispatch/license.txt %{buildroot}/usr/share/package-licenses/grass/lib_python_pydispatch_license.txt
cp lib/vector/dglib/COPYING %{buildroot}/usr/share/package-licenses/grass/lib_vector_dglib_COPYING
cp macosx/pkg/resources/License.rtf %{buildroot}/usr/share/package-licenses/grass/macosx_pkg_resources_License.rtf
cp mswindows/external/rbatch/COPYING %{buildroot}/usr/share/package-licenses/grass/mswindows_external_rbatch_COPYING
cp vector/v.lrs/LICENSE %{buildroot}/usr/share/package-licenses/grass/vector_v.lrs_LICENSE
%make_install prefix=%{buildroot}%{_libdir} UNIX_BIN=%{buildroot}%{_bindir} || :
## install_append content
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/include/grass
cp -r include/* %{buildroot}/usr/include/grass
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/grass/Make/Compile.make
/usr/include/grass/Make/DB.make
/usr/include/grass/Make/Dir.make
/usr/include/grass/Make/Docs.make
/usr/include/grass/Make/Doxyfile_arch_html
/usr/include/grass/Make/Doxyfile_arch_html.in
/usr/include/grass/Make/Doxyfile_arch_latex
/usr/include/grass/Make/Doxyfile_arch_latex.in
/usr/include/grass/Make/Doxygen.make
/usr/include/grass/Make/Etc.make
/usr/include/grass/Make/Grass.make
/usr/include/grass/Make/GuiScript.make
/usr/include/grass/Make/Html.make
/usr/include/grass/Make/HtmlRules.make
/usr/include/grass/Make/Install.make
/usr/include/grass/Make/Lib.make
/usr/include/grass/Make/Module.make
/usr/include/grass/Make/Multi.make
/usr/include/grass/Make/NoHtml.make
/usr/include/grass/Make/Other.make
/usr/include/grass/Make/Platform.make
/usr/include/grass/Make/Platform.make.in
/usr/include/grass/Make/Python.make
/usr/include/grass/Make/Rules.make
/usr/include/grass/Make/Script.make
/usr/include/grass/Make/ScriptRules.make
/usr/include/grass/Make/ShScript.make
/usr/include/grass/Make/ShScriptRules.make
/usr/include/grass/Make/Shlib.make
/usr/include/grass/Make/Sphinx.make
/usr/include/grass/Make/Stlib.make
/usr/include/grass/Make/Vars.make
/usr/include/grass/Makefile
/usr/include/grass/VERSION
/usr/include/grass/arraystats.h
/usr/include/grass/bitmap.h
/usr/include/grass/blas.h
/usr/include/grass/btree.h
/usr/include/grass/calc.h
/usr/include/grass/cdhc.h
/usr/include/grass/cluster.h
/usr/include/grass/colors.h
/usr/include/grass/config.h
/usr/include/grass/config.h.in
/usr/include/grass/datetime.h
/usr/include/grass/dbmi.h
/usr/include/grass/defs/Paintlib.h
/usr/include/grass/defs/arraystats.h
/usr/include/grass/defs/bitmap.h
/usr/include/grass/defs/btree.h
/usr/include/grass/defs/calc.h
/usr/include/grass/defs/cdhc.h
/usr/include/grass/defs/cluster.h
/usr/include/grass/defs/colors.h
/usr/include/grass/defs/datetime.h
/usr/include/grass/defs/dbmi.h
/usr/include/grass/defs/devlib.h
/usr/include/grass/defs/dig_atts.h
/usr/include/grass/defs/display.h
/usr/include/grass/defs/form.h
/usr/include/grass/defs/gis.h
/usr/include/grass/defs/glocale.h
/usr/include/grass/defs/gmath.h
/usr/include/grass/defs/gprojects.h
/usr/include/grass/defs/imagery.h
/usr/include/grass/defs/la.h
/usr/include/grass/defs/linkm.h
/usr/include/grass/defs/manage.h
/usr/include/grass/defs/neta.h
/usr/include/grass/defs/nviz.h
/usr/include/grass/defs/ogsf.h
/usr/include/grass/defs/ortholib.h
/usr/include/grass/defs/raster.h
/usr/include/grass/defs/raster3d.h
/usr/include/grass/defs/rbtree.h
/usr/include/grass/defs/rowio.h
/usr/include/grass/defs/segment.h
/usr/include/grass/defs/spawn.h
/usr/include/grass/defs/sqlp.h
/usr/include/grass/defs/stats.h
/usr/include/grass/defs/symbol.h
/usr/include/grass/defs/vector.h
/usr/include/grass/defs/vedit.h
/usr/include/grass/display.h
/usr/include/grass/fontcap.h
/usr/include/grass/form.h
/usr/include/grass/gis.h
/usr/include/grass/glocale.h
/usr/include/grass/gmath.h
/usr/include/grass/gprojects.h
/usr/include/grass/imagery.h
/usr/include/grass/iostream/ami.h
/usr/include/grass/iostream/ami_config.h
/usr/include/grass/iostream/ami_sort.h
/usr/include/grass/iostream/ami_sort_impl.h
/usr/include/grass/iostream/ami_stream.h
/usr/include/grass/iostream/embuffer.h
/usr/include/grass/iostream/empq.h
/usr/include/grass/iostream/empq_adaptive.h
/usr/include/grass/iostream/empq_adaptive_impl.h
/usr/include/grass/iostream/empq_impl.h
/usr/include/grass/iostream/imbuffer.h
/usr/include/grass/iostream/mem_stream.h
/usr/include/grass/iostream/minmaxheap.h
/usr/include/grass/iostream/mm.h
/usr/include/grass/iostream/mm_utils.h
/usr/include/grass/iostream/pqheap.h
/usr/include/grass/iostream/queue.h
/usr/include/grass/iostream/quicksort.h
/usr/include/grass/iostream/replacementHeap.h
/usr/include/grass/iostream/replacementHeapBlock.h
/usr/include/grass/iostream/rtimer.h
/usr/include/grass/la.h
/usr/include/grass/lapack.h
/usr/include/grass/linkm.h
/usr/include/grass/manage.h
/usr/include/grass/neta.h
/usr/include/grass/nviz.h
/usr/include/grass/ogsf.h
/usr/include/grass/ortholib.h
/usr/include/grass/raster.h
/usr/include/grass/raster3d.h
/usr/include/grass/rbtree.h
/usr/include/grass/rowio.h
/usr/include/grass/segment.h
/usr/include/grass/spawn.h
/usr/include/grass/sqlp.h
/usr/include/grass/stats.h
/usr/include/grass/symbol.h
/usr/include/grass/temporal.h
/usr/include/grass/vect/dig_defines.h
/usr/include/grass/vect/dig_externs.h
/usr/include/grass/vect/dig_macros.h
/usr/include/grass/vect/dig_structs.h
/usr/include/grass/vect/digit.h
/usr/include/grass/vector.h
/usr/include/grass/vedit.h
/usr/include/grass/version.h
/usr/include/grass/version.h.in
