import os

from pyformatjson.main import main_generate_md_files

if __name__ == "__main__":
    full_json_c = os.getenv("FULL_JSON_C", "")
    full_json_j = os.getenv("FULL_JSON_J", "")
    full_json_k = os.getenv("FULL_JSON_K", "")
    path_spidered_bibs = os.getenv("PATH_SPIDERED_BIBS", "")
    path_output = os.path.join(os.getenv("PATH_AILINKS", ""), "docs", "data")

    main_generate_md_files(full_json_c, full_json_j, full_json_k, path_output, path_spidered_bibs)
    main_generate_md_files(
        full_json_c, full_json_j, full_json_k, path_output, path_spidered_bibs, keywords_category_name="S"
    )
    main_generate_md_files(
        full_json_c, full_json_j, full_json_k, path_output, path_spidered_bibs, keywords_category_name="Y"
    )
