// Photo Gallery and Lightbox Functionality

const activityPhotos = {
    'batu-caves': [
        { src: '/KL-trip/assets/images/activities/batu-caves/1.jpg', caption: 'Rainbow stairs and golden Lord Murugan statue' },
        { src: '/KL-trip/assets/images/activities/batu-caves/2.jpg', caption: 'Colorful 272 steps leading to the temple' },
        { src: '/KL-trip/assets/images/activities/batu-caves/3.jpg', caption: 'View from the entrance with limestone cliffs' },
        { src: '/KL-trip/assets/images/activities/batu-caves/4.jpg', caption: 'Ancient limestone caves and Hindu shrines' }
    ],
    'petronas': [
        { src: '/KL-trip/assets/images/activities/petronas/1.jpg', caption: 'Iconic Petronas Twin Towers at night' },
        { src: '/KL-trip/assets/images/activities/petronas/2.jpg', caption: 'Skybridge connecting the towers' },
        { src: '/KL-trip/assets/images/activities/petronas/3.jpg', caption: 'Observation deck with panoramic views' }
    ],
    'bukit-bintang': [
        { src: '/KL-trip/assets/images/activities/bukit-bintang/2.jpg', caption: 'Pavilion KL shopping mall' },
        { src: '/KL-trip/assets/images/activities/bukit-bintang/3.jpg', caption: 'Bukit Bintang shopping district' }
    ],
    'jalan-alor': [
        { src: '/KL-trip/assets/images/activities/jalan-alor/1.jpg', caption: 'Famous night food street with lanterns' },
        { src: '/KL-trip/assets/images/activities/jalan-alor/2.jpg', caption: 'Street food stalls and outdoor dining' },
        { src: '/KL-trip/assets/images/activities/jalan-alor/3.jpg', caption: 'Authentic Malaysian street food experience' }
    ]
};

let currentLightbox = null;
let currentPhotoIndex = 0;
let currentPhotos = [];

// Initialize gallery for an activity
function initGallery(activityId) {
    const photos = activityPhotos[activityId];
    if (!photos || photos.length === 0) return '';
    
    let galleryHTML = '<div class="activity-gallery">';
    
    photos.forEach((photo, index) => {
        galleryHTML += `
            <div class="gallery-item" onclick="openLightbox('${activityId}', ${index})">
                <img src="${photo.src}" alt="${photo.caption}" loading="lazy">
                ${index === 0 ? `<div class="gallery-count">📷 ${photos.length} photos</div>` : ''}
            </div>
        `;
    });
    
    galleryHTML += '</div>';
    return galleryHTML;
}

// Open lightbox
function openLightbox(activityId, photoIndex) {
    currentPhotos = activityPhotos[activityId];
    currentPhotoIndex = photoIndex;
    
    const lightbox = document.getElementById('lightbox');
    if (!lightbox) {
        createLightbox();
    }
    
    updateLightboxImage();
    document.getElementById('lightbox').classList.add('active');
    document.body.style.overflow = 'hidden';
}

// Close lightbox
function closeLightbox() {
    document.getElementById('lightbox').classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Navigate to previous photo
function prevPhoto() {
    currentPhotoIndex = (currentPhotoIndex - 1 + currentPhotos.length) % currentPhotos.length;
    updateLightboxImage();
}

// Navigate to next photo
function nextPhoto() {
    currentPhotoIndex = (currentPhotoIndex + 1) % currentPhotos.length;
    updateLightboxImage();
}

// Update lightbox image
function updateLightboxImage() {
    const photo = currentPhotos[currentPhotoIndex];
    document.getElementById('lightbox-image').src = photo.src;
    document.getElementById('lightbox-caption').textContent = photo.caption;
    document.getElementById('lightbox-counter').textContent = `${currentPhotoIndex + 1} / ${currentPhotos.length}`;
}

// Create lightbox HTML
function createLightbox() {
    const lightboxHTML = `
        <div id="lightbox" class="lightbox">
            <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
            <div class="lightbox-counter" id="lightbox-counter">1 / 1</div>
            <div class="lightbox-prev" onclick="prevPhoto()">&#10094;</div>
            <div class="lightbox-content">
                <img id="lightbox-image" class="lightbox-image" src="" alt="">
            </div>
            <div class="lightbox-next" onclick="nextPhoto()">&#10095;</div>
            <div class="lightbox-caption" id="lightbox-caption"></div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', lightboxHTML);
    
    // Keyboard navigation
    document.addEventListener('keydown', function(e) {
        const lightbox = document.getElementById('lightbox');
        if (lightbox && lightbox.classList.contains('active')) {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') prevPhoto();
            if (e.key === 'ArrowRight') nextPhoto();
        }
    });
    
    // Click outside to close
    document.getElementById('lightbox').addEventListener('click', function(e) {
        if (e.target === this) closeLightbox();
    });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    createLightbox();
});
