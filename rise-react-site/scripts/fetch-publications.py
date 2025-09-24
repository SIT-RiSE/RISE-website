#!/usr/bin/env python3
"""
Publication fetcher script for RISSE Lab website.
Fetches publications from Google Scholar and performs incremental updates.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add current directory to path for imports
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

try:
    from scholarly import scholarly
    from tqdm import tqdm
except ImportError as e:
    print(f"Error: Missing required packages. Please install: pip install scholarly tqdm")
    print(f"Import error: {e}")
    sys.exit(1)

def format_authors(authors):
    """Convert 'and' separated authors to comma separated format."""
    return authors.replace(" and ", ", ")

def get_year(pub):
    """Extract and normalize publication year."""
    year = pub.get('year', '')
    if isinstance(year, int):
        return year
    elif isinstance(year, str) and year.isdigit():
        return int(year)
    else:
        return 0

def format_venue(venue_raw):
    """Format venue information to show journal/conference/arXiv properly."""
    if not venue_raw:
        return ""
    
    venue = venue_raw.strip()
    
    # Handle arXiv papers
    if 'arxiv' in venue.lower() or 'arxiv preprint' in venue.lower():
        return "arXiv"
    
    # Handle IEEE publications
    if 'ieee' in venue.lower():
        if 'transactions on software engineering' in venue.lower():
            return "IEEE TSE"
        elif 'transactions' in venue.lower():
            # Extract the specific transaction type
            if 'reliability' in venue.lower():
                return "IEEE TR"
            else:
                return "IEEE Transactions"
        elif 'international conference' in venue.lower():
            if 'software engineering' in venue.lower():
                return "ICSE"
            elif 'software maintenance' in venue.lower():
                return "ICSME"
            else:
                return "IEEE Conference"
        elif 'software' in venue.lower() and 'engineering' in venue.lower():
            return "IEEE Software"
    
    # Handle ACM publications
    if 'acm' in venue.lower():
        if 'transactions' in venue.lower():
            if 'software engineering' in venue.lower():
                return "ACM TOSEM"
            else:
                return "ACM Transactions"
        elif 'sigsoft' in venue.lower() or 'foundations of software engineering' in venue.lower():
            return "ACM SIGSOFT FSE"
        elif 'software engineering' in venue.lower():
            return "ACM Software Engineering"
    
    # Handle Springer publications
    if 'springer' in venue.lower():
        if 'empirical software engineering' in venue.lower():
            return "Empirical Software Engineering"
        elif 'software quality' in venue.lower():
            return "Software Quality Journal"
    
    # Handle conference proceedings - clean up the format
    if 'proceedings' in venue.lower():
        # Remove common prefixes
        clean_venue = venue
        prefixes_to_remove = [
            'Proceedings of the ',
            'In Proceedings of the ',
            'In ',
            'Proc. of the ',
            'Proc. ',
        ]
        for prefix in prefixes_to_remove:
            if clean_venue.startswith(prefix):
                clean_venue = clean_venue[len(prefix):]
        
        # Handle specific conferences
        if 'international conference on software engineering' in clean_venue.lower():
            return "ICSE"
        elif 'international symposium on software testing' in clean_venue.lower():
            return "ISSTA"
        elif 'automated software engineering' in clean_venue.lower():
            return "ASE"
        else:
            return clean_venue[:50]  # Limit length
    
    # Handle journal names
    journal_mappings = {
        'Empirical Software Engineering': 'Empirical Softw. Eng.',
        'Journal of Systems and Software': 'JSS',
        'Information and Software Technology': 'IST',
        'Software Quality Journal': 'SQJ',
    }
    
    for full_name, abbrev in journal_mappings.items():
        if full_name.lower() in venue.lower():
            return abbrev
    
    # Default: return cleaned venue (limited length)
    return venue[:60] if venue else ""

def infer_venue_from_url_and_title(title, paper_url, venue_raw):
    """Infer venue from paper URL and title when venue info is missing."""
    title_lower = title.lower()
    url_lower = paper_url.lower() if paper_url else ""
    
    # First try the original venue if available
    if venue_raw and venue_raw.strip():
        return format_venue(venue_raw)
    
    # Infer from URL patterns
    if 'ieeexplore.ieee.org' in url_lower:
        if 'tse' in url_lower or 'software engineering' in title_lower:
            return "IEEE TSE"
        elif 'icse' in url_lower:
            return "ICSE"
        elif 'icsme' in url_lower:
            return "ICSME"
        elif 'ase' in url_lower:
            return "ASE"
        else:
            return "IEEE"
    
    elif 'dl.acm.org' in url_lower:
        if 'tosem' in url_lower:
            return "ACM TOSEM"
        elif 'fse' in url_lower or 'sigsoft' in url_lower:
            return "ACM SIGSOFT FSE"
        else:
            return "ACM"
    
    elif 'arxiv.org' in url_lower:
        return "arXiv"
    
    elif 'link.springer.com' in url_lower:
        if 'empirical' in title_lower and 'software' in title_lower:
            return "Empirical Software Engineering"
        elif 'software quality' in title_lower:
            return "Software Quality Journal"
        else:
            return "Springer"
    
    elif 'peer.asee.org' in url_lower:
        return "ASEE"
    
    # Infer from title patterns
    if 'empirical study' in title_lower and 'software' in title_lower:
        return "Empirical Study"
    elif 'conference' in title_lower:
        return "Conference"
    elif 'workshop' in title_lower:
        return "Workshop"
    
    return ""
    """Format venue information to show journal/conference/arXiv properly."""
    if not venue_raw:
        return ""
    
    venue = venue_raw.strip()
    
    # Handle arXiv papers
    if 'arxiv' in venue.lower() or 'arxiv preprint' in venue.lower():
        return "arXiv"
    
    # Handle IEEE publications
    if 'ieee' in venue.lower():
        if 'transactions on software engineering' in venue.lower():
            return "IEEE TSE"
        elif 'transactions' in venue.lower():
            # Extract the specific transaction type
            if 'reliability' in venue.lower():
                return "IEEE TR"
            else:
                return "IEEE Transactions"
        elif 'international conference' in venue.lower():
            if 'software engineering' in venue.lower():
                return "ICSE"
            elif 'software maintenance' in venue.lower():
                return "ICSME"
            else:
                return "IEEE Conference"
        elif 'software' in venue.lower() and 'engineering' in venue.lower():
            return "IEEE Software"
    
    # Handle ACM publications
    if 'acm' in venue.lower():
        if 'transactions' in venue.lower():
            if 'software engineering' in venue.lower():
                return "ACM TOSEM"
            else:
                return "ACM Transactions"
        elif 'sigsoft' in venue.lower() or 'foundations of software engineering' in venue.lower():
            return "ACM SIGSOFT FSE"
        elif 'software engineering' in venue.lower():
            return "ACM Software Engineering"
    
    # Handle Springer publications
    if 'springer' in venue.lower():
        if 'empirical software engineering' in venue.lower():
            return "Empirical Software Engineering"
        elif 'software quality' in venue.lower():
            return "Software Quality Journal"
    
    # Handle conference proceedings - clean up the format
    if 'proceedings' in venue.lower():
        # Remove common prefixes
        clean_venue = venue
        prefixes_to_remove = [
            'Proceedings of the ',
            'In Proceedings of the ',
            'In ',
            'Proc. of the ',
            'Proc. ',
        ]
        for prefix in prefixes_to_remove:
            if clean_venue.startswith(prefix):
                clean_venue = clean_venue[len(prefix):]
        
        # Handle specific conferences
        if 'international conference on software engineering' in clean_venue.lower():
            return "ICSE"
        elif 'international symposium on software testing' in clean_venue.lower():
            return "ISSTA"
        elif 'automated software engineering' in clean_venue.lower():
            return "ASE"
        else:
            return clean_venue[:50]  # Limit length
    
    # Handle journal names
    journal_mappings = {
        'Empirical Software Engineering': 'Empirical Softw. Eng.',
        'Journal of Systems and Software': 'JSS',
        'Information and Software Technology': 'IST',
        'Software Quality Journal': 'SQJ',
    }
    
    for full_name, abbrev in journal_mappings.items():
        if full_name.lower() in venue.lower():
            return abbrev
    
    # Default: return cleaned venue (limited length)
    return venue[:60] if venue else ""

def is_valid_paper(pub_data):
    """Filter out non-paper entries like project incubators, books, etc."""
    title = pub_data.get('title', '').lower()
    venue = pub_data.get('venue', '').lower()
    authors = pub_data.get('authors', '').lower()
    
    # Filter out non-paper types by title patterns
    exclude_title_keywords = [
        'new project incubator',
        'project incubator',
        'principal investigator',
        'organizing committee',
        'workshop organizers',
        'welcome from',
        'proceedings of',
        'book',
        'workshop abstract',
        'poster',
        'demo',
        'nsf report',
        'grant',
        'award',
        'committee',
        'organizer',
        'chair',
        'editorial',
        'foreword',
        'preface',
        'introduction to',
        'special issue',
    ]
    
    # Filter out if title contains exclude patterns
    for keyword in exclude_title_keywords:
        if keyword in title:
            return False
    
    # Filter out titles that start with specific patterns (NSF reports, boards, etc.)
    exclude_title_prefixes = [
        'board#',
        'due:',
        'nsf',
        'grant',
        'award',
        'committee',
    ]
    
    for prefix in exclude_title_prefixes:
        if title.strip().startswith(prefix):
            return False
    
    # Filter out entries with too many authors (likely committee listings)
    if authors:
        author_count = len(authors.split(','))
        if author_count > 10:  # More than 10 authors is suspicious for a regular paper
            return False
    
    # Filter out entries with very generic titles
    generic_titles = [
        'new project incubator',
        'proceedings',
        'workshop',
        'demo',
        'committee',
        'organizing committee',
        'welcome',
        'introduction',
        'foreword',
        'preface',
    ]
    
    for generic in generic_titles:
        if title.strip() == generic or title.strip().endswith(generic):
            return False
    
    # Filter out obvious non-papers by title length and content
    if len(title.strip()) < 10:
        return False
    
    # Filter out entries that are clearly administrative/organizational
    admin_patterns = [
        'organiz',  # organizing, organizer, organization
        'committee',
        'chair',
        'editorial',
        'welcome',
        'introduction to the',
        'proceedings of the',
    ]
    
    for pattern in admin_patterns:
        if pattern in title and len(title.split()) < 8:  # Short titles with admin words
            return False
    
    # Must have authors (papers should have authors)
    if not pub_data.get('authors', '').strip():
        return False
    
    return True

def load_existing_publications(file_path):
    """Load existing publications from JSON file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load existing publications: {e}")
    return []

def create_publication_key(pub):
    """Create a unique key for publication comparison."""
    title = pub.get('title', '').strip().lower()
    year = str(pub.get('year', ''))
    # Use first author as part of key
    authors = pub.get('authors', '')
    first_author = authors.split(',')[0].strip() if authors else ''
    return f"{title}_{year}_{first_author.lower()}"

def get_publications_from_scholar(author_id):
    """Fetch publications from Google Scholar."""
    try:
        print("Searching for author...")
        author = scholarly.search_author_id(author_id)
        
        print("Retrieving author's publications...")
        author = scholarly.fill(author, sections=['publications'])
        
        publications = []
        total_pubs = len(author['publications'])
        
        print(f"Found {total_pubs} publications. Fetching details...")
        
        for pub in tqdm(author['publications'], total=total_pubs, desc="Fetching publications"):
            try:
                # Fill publication details
                pub = scholarly.fill(pub)
                
                # Extract required information
                publication = {
                    "title": pub['bib'].get('title', ''),
                    "authors": format_authors(pub['bib'].get('author', '')),
                    "year": pub['bib'].get('pub_year', ''),
                    "venue": infer_venue_from_url_and_title(
                        pub['bib'].get('title', ''),
                        pub.get('pub_url', ''),
                        pub['bib'].get('venue', '')
                    ),
                    "paper_url": pub.get('pub_url', ''),
                    "citations": pub.get('num_citations', 0)
                }
                
                # Only include valid papers
                if is_valid_paper(publication):
                    publications.append(publication)
                else:
                    print(f"Filtered out: {publication['title'][:50]}...")
                
            except Exception as e:
                print(f"Warning: Could not fetch details for a publication: {e}")
                continue
        
        return publications
        
    except Exception as e:
        print(f"Error fetching publications from Scholar: {e}")
        return []

def merge_publications(existing_pubs, new_pubs):
    """Merge existing and new publications, updating citation counts."""
    # Filter existing publications to remove non-papers
    filtered_existing = [pub for pub in existing_pubs if is_valid_paper(pub)]
    
    # Create lookup dictionaries
    existing_dict = {create_publication_key(pub): pub for pub in filtered_existing}
    new_dict = {create_publication_key(pub): pub for pub in new_pubs}
    
    merged = {}
    updated_count = 0
    new_count = 0
    filtered_count = len(existing_pubs) - len(filtered_existing)
    
    # Add all existing publications, updating with new data if available
    for key, existing_pub in existing_dict.items():
        if key in new_dict:
            new_pub = new_dict[key]
            # Update citation count and other potentially changed fields
            merged_pub = existing_pub.copy()
            merged_pub['citations'] = new_pub['citations']
            merged_pub['venue'] = new_pub['venue']  # Update venue formatting
            # Update paper_url if it wasn't available before
            if not merged_pub.get('paper_url') and new_pub.get('paper_url'):
                merged_pub['paper_url'] = new_pub['paper_url']
            merged[key] = merged_pub
            updated_count += 1
        else:
            merged[key] = existing_pub
    
    # Add genuinely new publications
    for key, new_pub in new_dict.items():
        if key not in existing_dict:
            merged[key] = new_pub
            new_count += 1
    
    # Convert back to list and sort by year
    result = list(merged.values())
    result.sort(key=lambda x: get_year(x), reverse=True)
    
    print(f"Merge results: {updated_count} updated, {new_count} new publications")
    if filtered_count > 0:
        print(f"Filtered out {filtered_count} non-paper entries")
    return result

def save_publications(publications, file_path):
    """Save publications to JSON file."""
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Add metadata
    output_data = {
        "last_updated": datetime.now().isoformat(),
        "total_publications": len(publications),
        "publications": publications
    }
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(publications, f, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Error saving publications: {e}")
        return False

def main():
    """Main function to update publications."""
    # Configuration
    author_id = "s2Z7NFYAAAAJ"  # Lu Xiao's Google Scholar ID
    
    # File paths
    script_dir = Path(__file__).parent
    output_file = script_dir.parent / "public" / "data" / "publications.json"
    
    print("Starting publication update process...")
    print(f"Output file: {output_file}")
    
    # Load existing publications
    existing_pubs = load_existing_publications(output_file)
    print(f"Found {len(existing_pubs)} existing publications")
    
    # Fetch new publications from Scholar
    new_pubs = get_publications_from_scholar(author_id)
    
    if not new_pubs:
        print("No new publications fetched. Keeping existing data.")
        return False
    
    print(f"Fetched {len(new_pubs)} publications from Scholar")
    
    # Merge publications
    merged_pubs = merge_publications(existing_pubs, new_pubs)
    
    # Save updated publications
    if save_publications(merged_pubs, output_file):
        print(f"Successfully updated publications.json with {len(merged_pubs)} publications")
        return True
    else:
        print("Failed to save publications")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)