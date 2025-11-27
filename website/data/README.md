# Team Data Management

The team member information is now managed through a JSON file for easy updates.

## How it Works

1. **Data File**: `data/team.json` contains all team member information
2. **JavaScript Loader**: `js/team-loader.js` reads the JSON and renders the HTML
3. **HTML Pages**: Both `index.html` and `people.html` load team data dynamically

## Adding or Updating Team Members

Edit `data/team.json` and add/modify entries in the `team_members` array:

```json
{
  "name": "Full Name",
  "photo": "filename.jpg",
  "role": "Lead PI",
  "title": "Associate Professor",
  "affiliation": "Department, Institution",
  "geo_expertise": "Primary geophysical expertise",
  "ai_expertise": "AI/ML expertise",
  "hazard_focus": "Specific hazards studied",
  "email": "email@uw.edu",
  "website": "https://personal-website.com",
  "github": "https://github.com/username",
  "scholar": "https://scholar.google.com/citations?user=USERID",
  "orcid": "https://orcid.org/0000-0000-0000-0000"
}
```

### Required Fields
- `name`
- `photo`
- `role`

### Optional Fields
All other fields are optional. Use empty string `""` if not applicable.

## Examples

### Principal Investigator
```json
{
  "name": "Marine Denolle",
  "photo": "marine-denolle.jpg",
  "role": "Lead PI",
  "title": "Associate Professor",
  "affiliation": "Earth and Space Sciences, University of Washington",
  "geo_expertise": "Seismology",
  "ai_expertise": "Physics-informed ML, Deep Learning",
  "hazard_focus": "Earthquakes, Seismic Hazards",
  "email": "mdenolle@uw.edu",
  "website": "https://denolle-lab.github.io",
  "github": "https://github.com/mdenolle",
  "scholar": "https://scholar.google.com/citations?user=jTLgRg8AAAAJ"
}
```

### Graduate Student
```json
{
  "name": "Student Name",
  "photo": "student-name.jpg",
  "role": "Graduate Student",
  "title": "PhD Student",
  "affiliation": "Earth and Space Sciences, University of Washington",
  "geo_expertise": "Seismic Imaging",
  "ai_expertise": "Data Science",
  "hazard_focus": "Earthquake Detection",
  "email": "student@uw.edu",
  "github": "",
  "website": ""
}
```

## Display on Pages

### Splash Page (`index.html`)
- Shows: Photo, Name, Role
- Links to people page or personal website

### People Page (`people.html`)
- Shows: Photo, Name, Expertise (combined geo + AI), Title/Affiliation, Hazard Focus
- Links: Email, GitHub, Google Scholar, ORCID, Website (if provided)

## Tips

1. **Photos**: Add team member photos to `images/team/` before adding to JSON
2. **Order**: Team members appear in the order listed in the JSON array
3. **Testing**: Use a local server (`python3 -m http.server`) to test changes
4. **Validation**: Use a JSON validator to ensure proper syntax
