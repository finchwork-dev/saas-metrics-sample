#!/usr/bin/env python3
"""Compute MRR, churn, NRR from a CSV: month,starting_mrr,new,expansion,contraction,churned"""
import csv,sys
for r in csv.DictReader(open(sys.argv[1])):
    s,n,e,c,ch=[float(r[k]) for k in("starting_mrr","new","expansion","contraction","churned")]
    end=s+n+e-c-ch
    print(f"{r['month']}: end MRR {end:.0f} | gross churn {(c+ch)/s:.1%} | NRR {(s+e-c-ch)/s:.1%}")
