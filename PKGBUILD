# Script generated with Bloom
pkgdesc="ROS - An implementation of ROS in pure-Java with Android support."
url='http://ros.org/wiki/rosjava_core'

pkgname='ros-kinetic-rosjava-core'
pkgver='0.3.5_1'
pkgrel=1
arch=('any')
license=('Apache 2.0'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-nav-msgs'
'ros-kinetic-rosgraph-msgs'
'ros-kinetic-rosjava-bootstrap'
'ros-kinetic-rosjava-build-tools'
'ros-kinetic-rosjava-messages'
'ros-kinetic-rosjava-test-msgs'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf2-msgs'
)

depends=()

conflicts=()
replaces=()

_dir=rosjava_core
source=()
md5sums=()

prepare() {
    cp -R $startdir/rosjava_core $srcdir/rosjava_core
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

