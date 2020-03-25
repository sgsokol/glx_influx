ln -s "$1" "$2"
fb="${2/.ftbl/}"
influx_s "$fb" > "$fb".stdout 2>"$fb".stderr
zip tmp.zip -r *"$fb"*
mv tmp.zip "$3"
