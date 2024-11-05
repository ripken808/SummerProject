import React, { useState, useEffect } from "react";

const TweetData = ({ tweet }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [maxImageHeight, setMaxImageHeight] = useState(null);

  // Extract image URLs from the tweet summary (assuming they are <img> tags)
  const extractImageUrls = (summary) => {
    const imgTags = summary?.match(/<img[^>]+src="([^">]+)"/g) || [];
    return imgTags.map((imgTag) => imgTag.match(/src="([^">]+)"/)[1]);
  };

  const images = extractImageUrls(tweet?.summary);

  // Function to remove <img> tags and any description content
  const removeImageTagsAndDescription = (summary) => {
    // Remove <img> tags
    let cleanedSummary = summary?.replace(/<img[^>]*>/g, "") || "";

    // Remove the <description><![CDATA[ ... ]]></description> block
    cleanedSummary = cleanedSummary.replace(
      /<description><!\[CDATA\[(.*?)\]\]><\/description>/,
      ""
    );

    // If there's a <title> tag, remove it too
    cleanedSummary = cleanedSummary.replace(/<title>(.*?)<\/title>/, "$1"); // Keep only the title text

    return cleanedSummary;
  };

  const cleanedSummary = removeImageTagsAndDescription(tweet?.summary);

  useEffect(() => {
    if (images.length > 0) {
      const img = new Image();
      img.src = images[currentImageIndex];
      img.onload = () => {
        setMaxImageHeight(img.height);
      };
    }
  }, [currentImageIndex, images]);

  // Function to go to the next image
  const nextImage = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === images.length - 1 ? 0 : prevIndex + 1
    );
  };

  // Function to go to the previous image
  const prevImage = () => {
    setCurrentImageIndex((prevIndex) =>
      prevIndex === 0 ? images.length - 1 : prevIndex - 1
    );
  };

  return (
    <div className="mb-8">
      {/* Margin to separate tweets */}
      <h3 className="text-lg font-bold mb-2">
        {tweet.title || "Untitled Tweet"}
      </h3>
      {/* Render the summary without images and description */}
      <p dangerouslySetInnerHTML={{ __html: cleanedSummary }}></p>

      {images.length > 0 && (
        <div className="relative">
          {/* Image with navigation buttons */}
          <div className="flex items-center justify-center">
            <img
              src={images[currentImageIndex]}
              alt="Tweet media"
              className="w-full h-auto object-contain rounded-md"
              style={{
                maxHeight: `${maxImageHeight}px`,
                maxWidth: "100%",
              }}
            />
          </div>

          {/* Left Arrow */}
          {images.length > 1 && (
            <button
              onClick={prevImage}
              className="absolute top-1/2 left-2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full hover:bg-gray-700"
            >
              &#9664;
            </button>
          )}

          {/* Right Arrow */}
          {images.length > 1 && (
            <button
              onClick={nextImage}
              className="absolute top-1/2 right-2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full hover:bg-gray-700"
            >
              &#9654;
            </button>
          )}
        </div>
      )}

      {/* Cool Separator */}
      <div className="flex justify-center items-center mt-6">
        <div className="w-2/3 border-t-2 border-gray-300 relative">
          <span className="absolute left-1/2 transform -translate-x-1/2 -top-3 bg-white px-2 text-gray-500">
            <i className="fas fa-circle"></i>
          </span>
        </div>
      </div>
    </div>
  );
};

export default TweetData;
