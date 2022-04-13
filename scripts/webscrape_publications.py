import requests as r
import yaml

def url(page=1):
    return ("https://gup-server.ub.gu.se/v1/public_publication_lists?locale=en&page=" + str(page) + "&indent=4sort_by=pubyear&publication_id=&person_id=127450%3B253733%3B4350%3B970600%3B664621%3B269050%3B85180%3B444205&department_id=1657&faculty_id=&serie_id=&project_id=&publication_type=&ref_value=&start_year=&end_year=")

data_tmp = r.get(url(1)).json()
pages=data_tmp['meta']['pagination']['pages']


pub_list=list()

for page in range(1,pages+1):
    data = r.get(url(page)).json()
    for pub_in in data['publications']:
        pub_list.append({k:pub_in[k] for k in ("authors","title","sourcetitle","pubyear","id","sourceissue","sourcevolume") if k in pub_in})


file = open("./_data/publications.yml", "w")
yaml.dump(pub_list, file)
file.close()
