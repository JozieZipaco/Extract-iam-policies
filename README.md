# Extract-iam-policies

This Python script utilizes the `google-cloud` library to retrieve IAM policies of a GCP organization as well as its associated folders and projects, and save the results into csv file. 

## Dependencies
- `google-cloud-iam`: This library needs to be installed. It can be installed via `pip install google-cloud-iam`.
- `google-cloud-resourcemanager_v3`: This library needs to be installed. It can be installed via `pip install google-cloud-resourcemanager_v3`.

## Usage
1. Ensure you have Python installed on your system.
2. Install dependencies by running `pip install google-cloud-iam`.
3. Run the Python script `get_iam_policies.py`.
4. Enter the GCP organization ID when prompted.
5. The script will retrieve and save IAM policies of the organization, its folders, and associated projects.

## Caveats
- Appropriate permissions are required to access IAM policies of specified GCP resources.

For further information on using the script, please contact the author.
