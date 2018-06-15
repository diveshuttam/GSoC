function container --description "run the container"
  set pgpgdir ~/Desktop/gsoc/pgpg
  set containerdir /var/ds/pgpg-bionic/
  echo "copying $pgpgdir to $containerdir Confirm?"
  read -p '' -l confirm
  sudo cp -r $pgpgdir $containerdir
  cd $containerdir
  sudo ds exec make
  sudo ds shell
  cd -
end
