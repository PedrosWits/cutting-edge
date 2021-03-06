# Files created and used throughout the pipeline
RAW_CSV = dataset/raw.csv
CATEGORISED_CSV = categorise/categorised.csv
EXTRACTED_CSV = extract/extracted.csv
ADDITIONAL_CSV = additional/toadd.csv
MERGED_CSV = merge/merged.csv
UNIQUE_CSV = unique/unique.csv
DATABASE_DB = insertDB/cutting_edge.db
PARSED_IMAGE_LINKS = linking/parsedLinks.txt

# 0. Download Dataset 
GET_DATASET_SRC = dataset/dl_dataset.sh
GET_DATASET_EXE = bash $(GET_DATASET_SRC) $(RAW_CSV)

# 1. Categorise
CATEGORISE_SRC = categorise/categorise.sh
CATEGORISE_EXE = bash $(CATEGORISE_SRC) $(RAW_CSV) $(CATEGORISED_CSV)

# 2. Extract relevant columns
EXTRACT_SRC = extract/extract.sh
EXTRACT_EXE = bash $(EXTRACT_SRC) $(CATEGORISED_CSV) $(EXTRACTED_CSV)

# 3. Build additional files
ADDITIONAL_SRC = additional/includeAdditional.sh
ADDITIONAL_EXE = bash $(ADDITIONAL_SRC) $(ADDITIONAL_CSV)

# 4. Merge extracted and additional files
MERGE_SRC = merge/mergeFiles.sh
MERGE_EXE = bash $(MERGE_SRC) $(MERGED_CSV) $(EXTRACTED_CSV) $(ADDITIONAL_CSV) 

# 5. Remove duplicates
UNIQUE_SRC = unique/removeDuplicates.sh
UNIQUE_EXE = bash $(UNIQUE_SRC) $(MERGED_CSV) $(UNIQUE_CSV)

# 6. Building the database
INSERT_DATABASE_SRC = insertDB/createDB.py
INSERT_DATABASE_EXE = python $(INSERT_DATABASE_SRC) $(UNIQUE_CSV) $(DATABASE_DB)

# 7. Querying the database
QUERY_DATABASE_SRC = queryDB/queries.py
QUERY_DATABASE_EXE = python $(QUERY_DATABASE_SRC) $(DATABASE_DB)

# 8. Linking images to database
UPDATE_DATABASE_SRC = linking/updateDB.py
UPDATE_DATABASE_EXE = python $(UPDATE_DATABASE_SRC) $(DATABASE_DB)
