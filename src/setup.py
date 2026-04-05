from setuptools import setup
import setup_translate

pkg = 'Extensions.DVDBackup'
setup(name='enigma2-plugin-extensions-dvdbackup',
       version='3.0',
       description='Create a backup of your Video-DVD',
       package_dir={pkg: 'DVDBackup'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'DVDBackup.png', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
