#!/bin/bash
mkdir /tmp/name/
cd /tmp/name
file=`hostname -I | cut -d ' ' -f 1|sed 's/ //g'`
file=`echo From_$file`
ps aux >>$file
