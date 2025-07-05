document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const cityInput = document.getElementById('cityInput');
    const resultsContainer = document.getElementById('resultsContainer');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error');
    const searchBtn = searchForm.querySelector('button[type="submit"]');

    function showLoading(state) {
        loadingDiv.style.display = state ? 'block' : 'none';
        if (searchBtn) searchBtn.disabled = !!state;
        cityInput.disabled = !!state;
    }

    function showError(msg) {
        errorDiv.textContent = msg;
        errorDiv.style.display = 'block';
    }
    function hideError() {
        errorDiv.style.display = 'none';
    }

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const city = cityInput.value.trim();
        if (!city) return;
        showLoading(true);
        hideError();
        resultsContainer.innerHTML = '';
        try {
            const response = await fetch(`/representatives/${encodeURIComponent(city)}`);
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail || 'Failed to fetch representatives');
            }
            if (!Array.isArray(data) || data.length === 0) {
                resultsContainer.innerHTML = `<div style="text-align:center;color:#888;font-size:1.1rem;">No representatives found for <b>${city}</b>.</div>`;
                return;
            }
            resultsContainer.innerHTML = data.map(rep => `
                <div class="representative-card">
                    <h3><span class="material-icons" style="font-size:1.2em;vertical-align:middle;color:var(--primary-color);margin-right:0.2em;">person</span>${rep.name}</h3>
                    <p><strong>Designation:</strong> ${rep.designation}</p>
                    ${rep.phone ? `<p><strong>Phone:</strong> <a href="tel:${rep.phone}">${rep.phone}</a></p>` : ''}
                    ${rep.email ? `<p><strong>Email:</strong> <a href="mailto:${rep.email}">${rep.email}</a></p>` : ''}
                    <span class="badge ${rep.verified ? 'badge-verified' : 'badge-unverified'}">
                        <span class="material-icons" style="font-size:1em;vertical-align:middle;margin-right:0.2em;">${rep.verified ? 'verified' : 'auto_awesome'}</span>
                        ${rep.verified ? 'Verified' : 'AI Generated'}
                    </span>
                    <button onclick="editRepresentative('${rep.name.replace(/'/g, "&#39;")}', '${rep.designation.replace(/'/g, "&#39;")}')" class="edit-btn">
                        <span class="material-icons" style="font-size:1em;vertical-align:middle;margin-right:0.2em;">edit</span>
                        Edit
                    </button>
                </div>
            `).join('');
        } catch (error) {
            showError(error.message);
        } finally {
            showLoading(false);
        }
    });
});

async function editRepresentative(name, designation) {
    const newPhone = prompt('Enter new phone number:');
    const newEmail = prompt('Enter new email:');
    if (!newPhone && !newEmail) return;
    try {
        const response = await fetch('/update_representative', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name,
                designation,
                phone: newPhone || null,
                email: newEmail || null,
            }),
        });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.detail || 'Failed to update representative');
        }
        // Refresh the search results
        document.getElementById('searchForm').dispatchEvent(new Event('submit'));
    } catch (error) {
        const errorDiv = document.getElementById('error');
        errorDiv.textContent = error.message;
        errorDiv.style.display = 'block';
    }
}
