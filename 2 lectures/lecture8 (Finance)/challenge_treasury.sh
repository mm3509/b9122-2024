curl https://home.treasury.gov/system/files/276/yield-curve-rates-1990-2021.csv | sed '/,,,,/d' | sort -k6 -t , | head -n 5 > 6months.tsv



