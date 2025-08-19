import React from 'react';

const PhotoCard = ({ photo, onLike }) => {
  const imageUrl = photo.image_url.startsWith('http') 
    ? photo.image_url 
    : `${process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'}${photo.image_url}`;

  return (
    <div className="bg-white rounded-xl shadow-lg overflow-hidden transform transition-transform duration-300 hover:scale-105">
      <img 
        src={imageUrl} 
        alt={photo.title} 
        className="w-full h-48 object-cover rounded-t-xl" 
        onError={(e) => { e.target.onerror = null; e.target.src="https://placehold.co/600x400/CCCCCC/000000?text=Image+Error" }}
      />
      <div className="p-4">
        <h3 className="text-xl font-bold text-gray-800 mb-2">{photo.title}</h3>
        <p className="text-gray-600 mb-4">{photo.description}</p>
        <div className="flex items-center justify-between">
          <button
            onClick={() => onLike(photo.id)}
            className="flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 px-4 rounded-full shadow-md transition-colors duration-200"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fillRule="evenodd"
                d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"
                clipRule="evenodd"
              />
            </svg>
            <span>Like</span>
          </button>
          <span className="text-gray-700 font-medium">❤️ {photo.likes}</span>
        </div>
      </div>
    </div>
  );
};

export default PhotoCard;