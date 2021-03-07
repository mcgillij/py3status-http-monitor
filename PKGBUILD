# Maintainer: Jason McGillivray < mcgillivray dot jason at gmail dot com>


pkgname=py3status-http-monitor
pkgdesc="Python daemon for controlling the fans on amdgpu cards"
pkgver=0.1.0
pkgrel=1
arch=('any')
license=('GPL2')
depends=('python' 'py3status')
makedepends=('python-setuptools')
url="https://github.com/mcgillij/py3status-http-monitor"
source=("py3status-http-monitor-0.1.0.tar.gz")
#source=("https://github.com/mcgillij/amdfan/releases/download/0.1.7/amdfan-0.1.7.tar.gz")
md5sums=('dd00f7e8fb722a776b630d525e3c6d8e')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --prefix=/usr --root="$pkgdir"
} 
