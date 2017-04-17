Name:           ros-kinetic-rosjava-core
Version:        0.3.3
Release:        0%{?dist}
Summary:        ROS rosjava_core package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/rosjava_core
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-rosgraph-msgs
BuildRequires:  ros-kinetic-rosjava-bootstrap
BuildRequires:  ros-kinetic-rosjava-build-tools
BuildRequires:  ros-kinetic-rosjava-messages
BuildRequires:  ros-kinetic-rosjava-test-msgs
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-tf2-msgs

%description
An implementation of ROS in pure-Java with Android support.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon Apr 17 2017 Damon Kohler <damonkohler@google.com> - 0.3.3-0
- Autogenerated by Bloom

* Mon Mar 06 2017 Damon Kohler <damonkohler@google.com> - 0.3.2-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Damon Kohler <damonkohler@google.com> - 0.3.1-0
- Autogenerated by Bloom

* Sat Dec 24 2016 Damon Kohler <damonkohler@google.com> - 0.3.0-0
- Autogenerated by Bloom

