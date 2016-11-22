include config.mk

# Get Dataset
.PHONY: dataset
dataset: $(GET_DATASET_SRC)
	$(info Fetching dataset)
	@$(GET_DATASET_EXE)

# Categorise items
.PHONY: categorise
categorise: dataset $(CATEGORISE_SRC) $(RAW_CSV)
	$(info Categorising items)
	@$(CATEGORISE_EXE)	

# Extract Relevant information
.PHONY: extract
extract: categorise $(EXTRACT_SRC) $(CATEGORISED_CSV)
	$(info Extracting relevant information)
	@$(EXTRACT_EXE)

# Build additional text files
.PHONY: additional
additional: $(ADDITIONAL_SRC)
	$(info Parsing and building additional txt files)
	@$(ADDITIONAL_EXE)

# Merge extracted info with additional text files
.PHONY: merge
merge: extract additional $(MERGE_SRC) $(EXTRACTED_CSV) $(ADDITIONAL_CSV)  
	$(info Merging extracted info with additional txt files)
	@$(MERGE_EXE)

# Remove duplicates
.PHONY: unique
unique: merge $(UNIQUE_SRC) $(MERGED_CSV)
	$(info Removing duplicate items)
	@$(UNIQUE_EXE)

# Building the database
.PHONY: buildDB
buildDB: unique $(INSERT_DATABASE_SRC) $(UNIQUE_CSV)
	$(info Creating and populating the database)
	@$(INSERT_DATABASE_EXE)

# Querying the database
.PHONY: queryDB
queryDB: buildDB $(QUERY_DATABASE_SRC)
	$(info Querying the database)
	@$(QUERY_DATABASE_EXE)

# Parsing Apache links
.PHONY: parseApache
parseApache: $(PARSE_APACHE_SRC)
	$(info Parsing Apache image links)
	@$(PARSE_APACHE_EXE)

# Pipeline
.PHONY: pipeline
pipeline: queryDB parseApache $(UPDATE_DATABASE_SRC)
	$(info Updating the Database)
	@$(UPDATE_DATABASE_EXE)
	$(info ***************************)
	$(info Pipeline ran successfully!!)
	$(info ***************************)

# Clean
.PHONY: clean
clean:
	rm -f $(RAW_CSV) $(CATEGORISED_CSV) $(EXTRACTED_CSV) $(ADDITIONAL_CSV) $(MERGED_CSV) $(UNIQUE_CSV) $(PARSED_IMAGE_LINKS)
