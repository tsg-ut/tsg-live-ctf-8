#!/usr/bin/env bash
set -ue -o pipefail
export LC_ALL=C

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 [web/giita etc...]"
  exit 1
fi

dirname=$(git rev-parse --show-toplevel)

slashes=`echo $1 | tr -cd /`
slashes_cnt=${#slashes}
if [[ $slashes_cnt -ne 1 ]] && [[ $slashes_cnt -ne 2 ]]; then
  echo "Usage: $0 [web/giita etc...]"
  exit 1
fi

challenge=$1
tokens=(${challenge//\// })
category=${tokens[0]}
title=${tokens[1]}

echo "Category: $category"
echo "Title: $title"

temprepo=`mktemp -d`
echo "Temporary repo: $temprepo"

git clone $dirname $temprepo

distdir="$temprepo/$category/$title/dist"
echo "Dist dir: $distdir"
if [[ ! -d $distdir ]]; then
  echo "dist dir not exist"
  exit 1
fi

tempdist=`mktemp -d`
echo "Temporary dist: $tempdist"
cp $distdir $tempdist/$title -r --dereference

cd $tempdist && tar caf $title.tar.gz --sort=name --owner=root:0 --group=root:0 --mtime='2022-05-13T07:00:00Z' --dereference $title && cd -
mkdir -p $dirname/dist
cp -f $tempdist/$title.tar.gz $dirname/dist

rm -rf $temprepo $tempdist

