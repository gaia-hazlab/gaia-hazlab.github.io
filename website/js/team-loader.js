/**
 * Team Data Loader
 * Loads team member data from JSON and renders it to the page
 */

// GitHub icon SVG
const githubIcon = `<svg width="20" height="20" viewBox="0 0 16 16" fill="currentColor">
    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
</svg>`;

/**
 * Create team member card for splash page
 */
function createTeamPreviewCard(member) {
    const link = member.website || 'people.html';
    return `
        <div class="team-member-preview">
            <a href="${link}" ${member.website ? 'target="_blank"' : ''}>
                <img src="${member.photo}" alt="${member.name}">
            </a>
            <h3>${member.name}</h3>
            <div class="role">${member.role}</div>
        </div>
    `;
}

/**
 * Create full team member card for people page
 */
function createTeamMemberCard(member) {
    const expertise = [];
    if (member.geo_expertise) expertise.push(member.geo_expertise);
    if (member.ai_expertise) expertise.push(member.ai_expertise);
    
    const expertiseText = expertise.join(' & ') + (member.role === 'Lead PI' ? ', Lead PI' : '');
    
    const links = [];
    if (member.email) {
        links.push(`<a href="mailto:${member.email}" title="Email">✉️</a>`);
    }
    if (member.github) {
        links.push(`<a href="${member.github}" title="GitHub" target="_blank">${githubIcon}</a>`);
    }
    if (member.scholar) {
        links.push(`<a href="${member.scholar}" title="Google Scholar" target="_blank">📚</a>`);
    }
    if (member.orcid) {
        links.push(`<a href="${member.orcid}" title="ORCID" target="_blank">🟢</a>`);
    }
    if (member.website) {
        links.push(`<a href="${member.website}" title="Website" target="_blank">🔗</a>`);
    }

    const description = member.hazard_focus 
        ? `${member.title}, ${member.affiliation}<br>Focus: ${member.hazard_focus}`
        : `${member.title}, ${member.affiliation}`;

    return `
        <div class="team-member">
            <img src="${member.photo}" alt="${member.name}">
            <h3>${member.name}</h3>
            <div class="expertise">${expertiseText}</div>
            <p>${description}</p>
            <div class="links">
                ${links.join('\n                ')}
            </div>
        </div>
    `;
}

/**
 * Load and render team members
 */
async function loadTeamData() {
    try {
        const response = await fetch('data/team.json');
        const data = await response.json();
        const members = data.team_members;

        // Render for splash page
        const previewContainer = document.getElementById('team-preview');
        if (previewContainer) {
            previewContainer.innerHTML = members.map(createTeamPreviewCard).join('');
        }

        // Render for people page
        const fullContainer = document.getElementById('team-grid');
        if (fullContainer) {
            fullContainer.innerHTML = members.map(createTeamMemberCard).join('');
        }
    } catch (error) {
        console.error('Error loading team data:', error);
        // Fallback: show error message
        const previewContainer = document.getElementById('team-preview');
        const fullContainer = document.getElementById('team-grid');
        const errorMsg = '<p style="color: #666; text-align: center;">Team information is currently unavailable.</p>';
        if (previewContainer) previewContainer.innerHTML = errorMsg;
        if (fullContainer) fullContainer.innerHTML = errorMsg;
    }
}

// Load team data when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadTeamData);
} else {
    loadTeamData();
}
