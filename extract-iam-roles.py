from google.oauth2 import service_account
from google.cloud import resourcemanager_v3
from google.cloud import iam_v2
import re
from google.auth import default
import csv


def get_projects_from_organizzation(organization_id,projects_and_folders):
    client = resourcemanager_v3.ProjectsClient()
    parent = f"organizations/{organization_id}"
    projects = client.list_projects(parent=parent)
    for project in projects: 
        projects_and_folders.append({"type": "project", "parent":parent, "id":project.project_id, "name":project.name,"folder_name": project.name})
    return projects_and_folders

def get_folder_from_organizzation(organization_id,projects_and_folders): 
    client = resourcemanager_v3.FoldersClient()
    parent = f"organizations/{organization_id}"
    folders = client.list_folders(parent=parent)
    for folder in folders:
        projects_and_folders.append({"type": "folder","parent":parent, "id":folder.name, "name":folder.name.strip('folders/'),"folder_name": folder.display_name })
    return projects_and_folders

def get_projects_from_folder(folder_id,projects_and_folders):
    client = resourcemanager_v3.ProjectsClient()
    parent= folder_id
    projects = client.list_projects(parent=parent)
    for project in projects: 
        projects_and_folders.append({"type": "project","parent":parent,"id":project.project_id, "name":project.name,"folder_name": project.name})
    return projects_and_folders

def get_prj_iam_policy(project_id):

    client = resourcemanager_v3.ProjectsClient()
    parent= project_id
    iam_policies = client.get_iam_policy(resource=parent)
    return iam_policies

def get_fld_iam_policy(folder_id):

    client = resourcemanager_v3.FoldersClient()
    parent= folder_id
    iam_policies = client.get_iam_policy(resource=parent)
    return iam_policies

def main(org_id):
    organization_id = org_id 
    projects_and_folders = []
    pattern = r'^folders/[0-9]+$'
    user_and_roles_dict=[]
    csv_file="iam_policy.csv"

    projects_and_folders=get_folder_from_organizzation(organization_id,projects_and_folders)

    for folder in projects_and_folders:
        if re.match(pattern, folder["id"]):
            projects_and_folders=get_projects_from_folder(folder["id"],projects_and_folders)

    projects_and_folders=get_projects_from_organizzation(organization_id,projects_and_folders)

    for prj in projects_and_folders:
        if prj["type"]=="project":
            iam_policy=get_prj_iam_policy(prj["name"])
            for plc in iam_policy.bindings:
                user_and_roles_dict.append({"parent":prj["id"], "role": plc.role, "member": plc.members})
        else:
            if re.match(pattern, prj["id"]):
                iam_policy=get_fld_iam_policy(prj["id"])
                for plc in iam_policy.bindings:
                    user_and_roles_dict.append({"parent":"folders/"+prj["folder_name"], "role": plc.role, "member": plc.members})

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Parent', 'Role', 'Member'])
        for element in user_and_roles_dict:
            for member in element['member']:
                writer.writerow([element['parent'], element['role'], member])

if __name__ == "__main__":
    org_id = input("Inserisci l'ID dell'organizzazione GCP: ")
    main(org_id)
