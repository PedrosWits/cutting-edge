include config.mk

# Get Dataset
.PHONY: dataset
dataset: $(GET_DATASET_SRC)
	$(info Fetching dataset)
	@$(GET_DATASET_EXE)

# Categorise items
.PHONY: categorise
categorise: dataset $(CATEGORISE_SRC)
	$(info Categorising items)
	@$(CATEGORIZE_EXE)	

# Extract Relevant information
.PHONY: extract
extract: categorise $(EXTRACT_SRC)
	$(info Extracting relevant information)
	@$(EXTRACT_EXE)

# Build additional text files
.PHONY: additional
additional: $(ADDITIONAL_SRC)
	$(info Parsing and building additional txt files)
	@$(ADDITIONAL_EXE)

# Merge extracted info with additional text files
.PHONY: merge
merge: extract additional $(MERGE_SRC)
	$(info Merging extracted info with additional txt files)
	@$(MERGE_EXE)

# Remove duplicates
.PHONY: unique
unique: merge $(UNIQUE_SRC)
	$(info Removing duplicate items)
	@$(UNIQUE_EXE)


# Clean
.PHONY: clean
clean:
	rm -f *.csv
