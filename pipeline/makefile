.PHONY: dataset
dataset:
	bash $@/dl_dataset.sh $@/$@.csv 

.PHONY: categorise
categorise: dataset
	bash $@/$@.sh $</$<.csv $@/$@.csv


.PHONY: clean
clean:
	rm -f *.csv
