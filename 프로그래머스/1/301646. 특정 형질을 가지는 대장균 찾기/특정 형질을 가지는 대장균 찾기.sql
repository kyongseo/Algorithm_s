select count(*) as count
from ECOLI_DATA
where GENOTYPE & 2 != 2 
AND (GENOTYPE & 1 = 1 OR GENOTYPE & 4 = 4);
