#! /bin/bash

getFileName() {
  # trim off initial "./" and ending "Tests.py", which have lengths 2 and 8 respectively
  filename=${testName:2:-8}
}

getTestFolder() {
  testFolder=$(dirname $testName)
}

getSrcName() {
  getFileName
  srcName="../src/$filename.py"
}

# copy each test file's corresponding source file to a location the test file can read it
for testName in $(find -name "*Tests.py" | grep -v "__init__"); do
  getSrcName
  getTestFolder
  cp $srcName $testFolder
done

# run all the tests
for testName in $(find -name "*Tests.py" | grep -v "__init__"); do
  python3 $testName
done


