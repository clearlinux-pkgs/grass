#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grass
Version  : 7.6.1
Release  : 16
URL      : https://github.com/OSGeo/grass/archive/grass_7_6_1.tar.gz
Source0  : https://github.com/OSGeo/grass/archive/grass_7_6_1.tar.gz
Summary  : Multi-producer-multi-consumer signal dispatching mechanism
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-SA-3.0 GPL-2.0 GPL-2.0+ LGPL-2.1 MIT
BuildRequires : bison
BuildRequires : buildreq-distutils3
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
Requires: grass = %{version}-%{release}

%description dev
dev components for the grass package.


%package staticdev
Summary: staticdev components for the grass package.
Group: Default
Requires: grass-dev = %{version}-%{release}

%description staticdev
staticdev components for the grass package.


%prep
%setup -q -n grass-grass_7_6_1
cd %{_builddir}/grass-grass_7_6_1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588970575
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -std=gnu++98"
%configure --disable-static --with-fftw \
--with-openmp \
--without-freetype
make  || :

%install
export SOURCE_DATE_EPOCH=1588970575
rm -rf %{buildroot}
## install_prepend content
mkdir -p %{buildroot}/usr/etc
touch  %{buildroot}/usr/etc/fontcap
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/grass
cp %{_builddir}/grass-grass_7_6_1/COPYING %{buildroot}/usr/share/package-licenses/grass/fec4c918439699ee30a9d9d3c6871eab45246425
cp %{_builddir}/grass-grass_7_6_1/GPL.TXT %{buildroot}/usr/share/package-licenses/grass/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/grass-grass_7_6_1/gui/icons/grass/LICENSE.TXT %{buildroot}/usr/share/package-licenses/grass/0747c895de1a0b941f6b0abdd187a107993e417f
cp %{_builddir}/grass-grass_7_6_1/lib/external/ccmath/lgpl.license %{buildroot}/usr/share/package-licenses/grass/da016558d8dd563e6693582be08505ac1a5387a1
cp %{_builddir}/grass-grass_7_6_1/lib/init/license.txt %{buildroot}/usr/share/package-licenses/grass/9fb43ecc8e9ad6fa06ea95c49ca2bbe7f9917f11
cp %{_builddir}/grass-grass_7_6_1/lib/python/ctypes/ctypesgencore/LICENSE %{buildroot}/usr/share/package-licenses/grass/0e8932b32ff8fa9942ca97b138f518cddf430977
cp %{_builddir}/grass-grass_7_6_1/lib/python/pydispatch/license.txt %{buildroot}/usr/share/package-licenses/grass/0053f5f87a9855e99be2109f0afefbd03783eb94
cp %{_builddir}/grass-grass_7_6_1/lib/vector/dglib/COPYING %{buildroot}/usr/share/package-licenses/grass/170b015707d69b319293cdd2cf5707b9abb113aa
cp %{_builddir}/grass-grass_7_6_1/macosx/pkg/resources/License.rtf %{buildroot}/usr/share/package-licenses/grass/65242d3cadbf641fa880ae981c906ff2c0b56d2b
cp %{_builddir}/grass-grass_7_6_1/mswindows/external/rbatch/COPYING %{buildroot}/usr/share/package-licenses/grass/b9e28040de9d8773c5b0cc8108869e8f3f287798
cp %{_builddir}/grass-grass_7_6_1/mswindows/external/rbatch/LICENSE %{buildroot}/usr/share/package-licenses/grass/3e214f9d2536757b88a59d2d5a05f5e38d660e46
cp %{_builddir}/grass-grass_7_6_1/vector/v.lrs/LICENSE %{buildroot}/usr/share/package-licenses/grass/0dffcc72bb327ff5b4dc2158e1723f334779543b
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
/usr/include/grass/N_gwflow.h
/usr/include/grass/N_heatflow.h
/usr/include/grass/N_pde.h
/usr/include/grass/N_solute_transport.h
/usr/include/grass/VERSION
/usr/include/grass/arraystats.h
/usr/include/grass/bitmap.h
/usr/include/grass/blas.h
/usr/include/grass/btree.h
/usr/include/grass/calc.h
/usr/include/grass/card.h
/usr/include/grass/ccmath_grass.h
/usr/include/grass/cdhc.h
/usr/include/grass/citing.h
/usr/include/grass/cluster.h
/usr/include/grass/colors.h
/usr/include/grass/config.h
/usr/include/grass/config.h.in
/usr/include/grass/confparms.h
/usr/include/grass/copying.h
/usr/include/grass/dataquad.h
/usr/include/grass/datetime.h
/usr/include/grass/dbmi.h
/usr/include/grass/dbstubs.h
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
/usr/include/grass/dgl.h
/usr/include/grass/dgl/avl.h
/usr/include/grass/dgl/graph.h
/usr/include/grass/dgl/graph_v1.h
/usr/include/grass/dgl/graph_v2.h
/usr/include/grass/dgl/heap.h
/usr/include/grass/dgl/helpers.h
/usr/include/grass/dgl/tavl.h
/usr/include/grass/dgl/tree.h
/usr/include/grass/dgl/type.h
/usr/include/grass/dgl/v1-defs.h
/usr/include/grass/dgl/v2-defs.h
/usr/include/grass/display.h
/usr/include/grass/fontcap.h
/usr/include/grass/form.h
/usr/include/grass/gis.h
/usr/include/grass/glocale.h
/usr/include/grass/gmath.h
/usr/include/grass/gprojects.h
/usr/include/grass/imagery.h
/usr/include/grass/index.h
/usr/include/grass/interpf.h
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
/usr/include/grass/kdtree.h
/usr/include/grass/la.h
/usr/include/grass/lapack.h
/usr/include/grass/lidar.h
/usr/include/grass/linkm.h
/usr/include/grass/lrs.h
/usr/include/grass/manage.h
/usr/include/grass/neta.h
/usr/include/grass/nviz.h
/usr/include/grass/ogsf.h
/usr/include/grass/ortholib.h
/usr/include/grass/qtree.h
/usr/include/grass/raster.h
/usr/include/grass/raster3d.h
/usr/include/grass/rbtree.h
/usr/include/grass/rowio.h
/usr/include/grass/rtree.h
/usr/include/grass/segment.h
/usr/include/grass/shapefil.h
/usr/include/grass/simlib.h
/usr/include/grass/spawn.h
/usr/include/grass/split.h
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
/usr/include/grass/waterglobs.h
/usr/lib64/libgrass_arraystats.7.6.so
/usr/lib64/libgrass_arraystats.so
/usr/lib64/libgrass_bitmap.7.6.so
/usr/lib64/libgrass_bitmap.so
/usr/lib64/libgrass_btree.7.6.so
/usr/lib64/libgrass_btree.so
/usr/lib64/libgrass_btree2.7.6.so
/usr/lib64/libgrass_btree2.so
/usr/lib64/libgrass_cairodriver.7.6.so
/usr/lib64/libgrass_cairodriver.so
/usr/lib64/libgrass_calc.7.6.so
/usr/lib64/libgrass_calc.so
/usr/lib64/libgrass_ccmath.7.6.so
/usr/lib64/libgrass_ccmath.so
/usr/lib64/libgrass_cdhc.7.6.so
/usr/lib64/libgrass_cdhc.so
/usr/lib64/libgrass_cluster.7.6.so
/usr/lib64/libgrass_cluster.so
/usr/lib64/libgrass_datetime.7.6.so
/usr/lib64/libgrass_datetime.so
/usr/lib64/libgrass_dbmibase.7.6.so
/usr/lib64/libgrass_dbmibase.so
/usr/lib64/libgrass_dbmiclient.7.6.so
/usr/lib64/libgrass_dbmiclient.so
/usr/lib64/libgrass_dbmidriver.7.6.so
/usr/lib64/libgrass_dbmidriver.so
/usr/lib64/libgrass_dbstubs.7.6.so
/usr/lib64/libgrass_dbstubs.so
/usr/lib64/libgrass_dgl.7.6.so
/usr/lib64/libgrass_dgl.so
/usr/lib64/libgrass_dig2.7.6.so
/usr/lib64/libgrass_dig2.so
/usr/lib64/libgrass_display.7.6.so
/usr/lib64/libgrass_display.so
/usr/lib64/libgrass_driver.7.6.so
/usr/lib64/libgrass_driver.so
/usr/lib64/libgrass_dspf.7.6.so
/usr/lib64/libgrass_dspf.so
/usr/lib64/libgrass_g3d.7.6.so
/usr/lib64/libgrass_g3d.so
/usr/lib64/libgrass_gis.7.6.so
/usr/lib64/libgrass_gis.so
/usr/lib64/libgrass_gmath.7.6.so
/usr/lib64/libgrass_gmath.so
/usr/lib64/libgrass_gpde.7.6.so
/usr/lib64/libgrass_gpde.so
/usr/lib64/libgrass_gproj.7.6.so
/usr/lib64/libgrass_gproj.so
/usr/lib64/libgrass_htmldriver.7.6.so
/usr/lib64/libgrass_htmldriver.so
/usr/lib64/libgrass_imagery.7.6.so
/usr/lib64/libgrass_imagery.so
/usr/lib64/libgrass_interpdata.7.6.so
/usr/lib64/libgrass_interpdata.so
/usr/lib64/libgrass_interpfl.7.6.so
/usr/lib64/libgrass_interpfl.so
/usr/lib64/libgrass_iortho.7.6.so
/usr/lib64/libgrass_iortho.so
/usr/lib64/libgrass_lidar.7.6.so
/usr/lib64/libgrass_lidar.so
/usr/lib64/libgrass_linkm.7.6.so
/usr/lib64/libgrass_linkm.so
/usr/lib64/libgrass_lrs.7.6.so
/usr/lib64/libgrass_lrs.so
/usr/lib64/libgrass_manage.7.6.so
/usr/lib64/libgrass_manage.so
/usr/lib64/libgrass_neta.7.6.so
/usr/lib64/libgrass_neta.so
/usr/lib64/libgrass_nviz.7.6.so
/usr/lib64/libgrass_nviz.so
/usr/lib64/libgrass_ogsf.7.6.so
/usr/lib64/libgrass_ogsf.so
/usr/lib64/libgrass_pngdriver.7.6.so
/usr/lib64/libgrass_pngdriver.so
/usr/lib64/libgrass_psdriver.7.6.so
/usr/lib64/libgrass_psdriver.so
/usr/lib64/libgrass_qtree.7.6.so
/usr/lib64/libgrass_qtree.so
/usr/lib64/libgrass_raster.7.6.so
/usr/lib64/libgrass_raster.so
/usr/lib64/libgrass_rli.7.6.so
/usr/lib64/libgrass_rli.so
/usr/lib64/libgrass_rowio.7.6.so
/usr/lib64/libgrass_rowio.so
/usr/lib64/libgrass_rtree.7.6.so
/usr/lib64/libgrass_rtree.so
/usr/lib64/libgrass_segment.7.6.so
/usr/lib64/libgrass_segment.so
/usr/lib64/libgrass_shape.7.6.so
/usr/lib64/libgrass_shape.so
/usr/lib64/libgrass_sim.7.6.so
/usr/lib64/libgrass_sim.so
/usr/lib64/libgrass_sqlp.7.6.so
/usr/lib64/libgrass_sqlp.so
/usr/lib64/libgrass_stats.7.6.so
/usr/lib64/libgrass_stats.so
/usr/lib64/libgrass_symb.7.6.so
/usr/lib64/libgrass_symb.so
/usr/lib64/libgrass_temporal.7.6.so
/usr/lib64/libgrass_temporal.so
/usr/lib64/libgrass_vector.7.6.so
/usr/lib64/libgrass_vector.so
/usr/lib64/libgrass_vedit.7.6.so
/usr/lib64/libgrass_vedit.so

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libgrass_iostream.7.6.a
