document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const cityInput = document.getElementById('cityInput');
    const resultsContainer = document.getElementById('resultsContainer');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error');

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const city = cityInput.value.trim();
        if (!city) return;

        // Show loading state
        loadingDiv.style.display = 'block';
        errorDiv.style.display = 'none';
        resultsContainer.innerHTML = '';

        try {
            const response = await fetch(`/representatives/${city}`);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || 'Failed to fetch representatives');
            }

            // Display results
            resultsContainer.innerHTML = data.map(rep => `
                <div class="representative-card">
                    <h3>${rep.name}</h3>
                    <p><strong>Designation:</strong> ${rep.designation}</p>
                    ${rep.phone ? `<p><strong>Phone:</strong> ${rep.phone}</p>` : ''}
                    ${rep.email ? `<p><strong>Email:</strong> ${rep.email}</p>` : ''}
                    <span class="badge ${rep.verified ? 'badge-verified' : 'badge-unverified'}">
                        ${rep.verified ? 'Verified' : 'AI Generated'}
                    </span>
                    <button onclick="editRepresentative('${rep.name}', '${rep.designation}')" class="edit-btn">
                        Edit
                    </button>
                </div>
            `).join('');

        } catch (error) {
            errorDiv.textContent = error.message;
            errorDiv.style.display = 'block';
        } finally {
            loadingDiv.style.display = 'none';
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
