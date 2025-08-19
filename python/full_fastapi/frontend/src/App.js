import React, { useState, useEffect } from 'react';
import { getPhotos, likePhoto, loginUser, createPost } from './api';
import PhotoCard from './components/PhotoCard';
import LoginForm from './components/LoginForm';
import AdminPanel from './components/AdminPanel';

function App() {
  const [photos, setPhotos] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isAdmin, setIsAdmin] = useState(false);
  const [token, setToken] = useState(null);
  const [message, setMessage] = useState('');

  const fetchPhotos = async () => {
    try {
      const data = await getPhotos();
      setPhotos(data);
    } catch (error) {
      console.error("Error fetching photos:", error);
      setMessage('Failed to fetch photos.');
    }
  };

  useEffect(() => {
    fetchPhotos();
    const storedToken = localStorage.getItem('token');
    const storedIsAdmin = localStorage.getItem('isAdmin') === 'true';
    if (storedToken) {
      setToken(storedToken);
      setIsLoggedIn(true);
      setIsAdmin(storedIsAdmin);
    }
  }, []);

  const handleLike = async (photoId) => {
    try {
      await likePhoto(photoId);
      fetchPhotos(); // Refresh photos to show updated like count
    } catch (error) {
      console.error("Error liking photo:", error);
      setMessage('Failed to like photo.');
    }
  };

  const handleLogin = async (username, password) => {
    setMessage('');
    try {
      const data = await loginUser(username, password);
      if (data.access_token) {
        setToken(data.access_token);
        setIsLoggedIn(true);
        // Fetch user info to determine admin status
        const userInfoResponse = await fetch(`${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}/users/me/`, {
            headers: { 'Authorization': `Bearer ${data.access_token}` }
        });
        const userInfo = await userInfoResponse.json();
        if (userInfo.is_admin) {
            setIsAdmin(true);
            localStorage.setItem('isAdmin', 'true');
        } else {
            setIsAdmin(false);
            localStorage.setItem('isAdmin', 'false');
        }
        localStorage.setItem('token', data.access_token);
        setMessage('Login successful!');
      } else {
        setMessage('Login failed: Invalid credentials.');
      }
    } catch (error) {
      console.error("Error during login:", error);
      setMessage('Login failed. Please try again.');
    }
  };

  const handleLogout = () => {
    setToken(null);
    setIsLoggedIn(false);
    setIsAdmin(false);
    localStorage.removeItem('token');
    localStorage.removeItem('isAdmin');
    setMessage('Logged out successfully.');
  };

  const handleCreatePost = async (title, description, imageFile) => {
    setMessage('');
    try {
      await createPost(title, description, imageFile, token);
      fetchPhotos(); // Refresh photos after new post
      setMessage('Post created successfully!');
    } catch (error) {
      console.error("Error creating post:", error);
      setMessage('Failed to create post. Check console for details.');
    }
  };

  return (
    <div className="container mx-auto p-4 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-bold text-center mb-8 text-blue-700">Photo Sharing App</h1>
      
      <div className="flex justify-end mb-4">
        {isLoggedIn ? (
          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg shadow-md"
          >
            Logout
          </button>
        ) : (
          <LoginForm onLogin={handleLogin} />
        )}
      </div>

      {message && (
        <div className="bg-blue-100 border-l-4 border-blue-500 text-blue-700 p-4 mb-4 rounded-lg" role="alert">
          <p className="font-bold">Info</p>
          <p>{message}</p>
        </div>
      )}

      {isAdmin && (
        <AdminPanel onCreatePost={handleCreatePost} />
      )}

      <h2 className="text-3xl font-semibold mb-6 text-gray-800">Photos</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {photos.map((photo) => (
          <PhotoCard key={photo.id} photo={photo} onLike={handleLike} />
        ))}
      </div>
    </div>
  );
}

export default App;
