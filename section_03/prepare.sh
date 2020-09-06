cd input
if [ ! -f jawiki-country.json ]; then
    wget https://nlp100.github.io/data/jawiki-country.json.gz
    gunzip jawiki-country.json.gz
fi
cd ../
for i in $(seq 20 29); do
    touch $i.py
done