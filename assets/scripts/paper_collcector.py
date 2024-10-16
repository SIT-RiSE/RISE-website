import json
from scholarly import scholarly
from tqdm import tqdm

def format_authors(authors):
    # 将作者字符串中的 " and " 替换为 ", "
    return authors.replace(" and ", ", ")

def get_year(pub):
    year = pub.get('year', '')
    if isinstance(year, int):
        return year
    elif isinstance(year, str) and year.isdigit():
        return int(year)
    else:
        return 0  # 默认值为0，表示未知年份

def get_publications(author_id):
    try:
        # 搜索作者
        print("Searching for author...")
        author = scholarly.search_author_id(author_id)
        
        # 填充作者的所有出版物
        print("Retrieving author's publications...")
        author = scholarly.fill(author, sections=['publications'])
        
        publications = []
        total_pubs = len(author['publications'])
        
        print(f"Found {total_pubs} publications. Fetching details...")
        for pub in tqdm(author['publications'], total=total_pubs, desc="Fetching publications"):
            # 填充每个出版物的详细信息
            pub = scholarly.fill(pub)
            
            # 提取所需的信息
            publication = {
                "title": pub['bib'].get('title', ''),
                "authors": format_authors(pub['bib'].get('author', '')),
                "year": pub['bib'].get('pub_year', ''),
                "venue": pub['bib'].get('venue', ''),
                "paper_url": pub.get('pub_url', ''),
                "citations": pub.get('num_citations', 0)
            }
            publications.append(publication)
        
        # 按年份排序，从新到旧
        publications.sort(key=lambda x: get_year(x), reverse=True)
        
        return publications
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Google Scholar ID for Lu Xiao
author_id = "s2Z7NFYAAAAJ"

print("Starting to fetch publications...")

# 获取出版物
publications = get_publications(author_id)

print("Saving results to JSON file...")

# 将结果保存为 JSON 文件
with open('./assets/scripts/lu_xiao_publications.json', 'w', encoding='utf-8') as f:
    json.dump(publications, f, ensure_ascii=False, indent=4)

print(f"Saved {len(publications)} publications to lu_xiao_publications.json")
print("Process completed.")