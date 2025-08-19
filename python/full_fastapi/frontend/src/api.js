const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const getPhotos = async () => {
    const response = await fetch(`${API_BASE_URL}/photos/`);
    return response.json();
};

export const likePhoto = async (photoId) => {
    const response = await fetch(`${API_BASE_URL}/photos/${photoId}/like`, {
        method: 'POST',
    });
    return response.json();
};

export const loginUser = async (username, password) => {
    const details = {
        username: username,
        password: password
    };
    const formBody = Object.keys(details).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(details[key])).join('&');

    const response = await fetch(`${API_BASE_URL}/token`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formBody
    });
    return response.json();
};

export const createPost = async (title, description, imageFile, token) => {
    const formData = new FormData();
    formData.append('title', title);
    if (description) {
        formData.append('description', description);
    }
    formData.append('file', imageFile);

    const response = await fetch(`${API_BASE_URL}/photos/`, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    });
    return response.json();
};