# a_values=(0.5 0.6 0.7 0.8 0.9 0.92 0.94 0.96 0.98 0.99)
a_values=(0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8 0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.90 0.91 0.92 0.93)

for a in ${a_values[@]};
do
    python3 script.py $a &
done